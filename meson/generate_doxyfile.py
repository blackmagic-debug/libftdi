#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023-2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations
from argparse import ArgumentParser, FileType
from io import StringIO
from pathlib import Path
import os

def with_trailing(p: Path) -> str:
	return f"{p.as_posix()}{'/' if p.is_dir() else ''}"

if __name__ == '__main__':
	parser = ArgumentParser(description='Create a Doxyfile for the whole project respecting Meson conventions')
	parser.add_argument('--prelude', nargs='+', type=Path, help='Templates that will be copied to the file')
	parser.add_argument('--strip', nargs='+', type=Path, help='Make paths inside this directory relative')
	parser.add_argument('--example-path', nargs='+', type=Path, help='Directory that contains example code fragments')
	parser.add_argument('--output', type=FileType('w', encoding='utf-8'), required=True, help='Write to this file')
	parser.add_argument('root', type=Path, help='Root for the Doxygen output')
	parser.add_argument('inputs', nargs='+', type=Path, help='Inputs for the Doxygen documentation')
	args = parser.parse_args()

	f = StringIO()

	if args.prelude:
		for file in args.prelude:
			f.write(file.open(encoding='utf-8').read())
	f.write('# MESON override OUTPUT_DIR\n')
	f.write(f'OUTPUT_DIRECTORY       = {args.root.as_posix()}\n')
	if args.strip:
		paths_to_strip: str = ' '.join([f.as_posix() for f in args.strip])
		f.write(f'STRIP_FROM_PATH += {paths_to_strip}\n')
	if args.inputs:
		inputs = ' '.join([f.as_posix() for f in args.inputs])
		f.write(f'INPUT += {inputs}\n')
	if args.example_path:
		example_paths = ' '.join(map(with_trailing, args.example_path))
		f.write(f'EXAMPLE_PATH += {example_paths}\n')

	with args.output as output:
		output.write(f.getvalue())
