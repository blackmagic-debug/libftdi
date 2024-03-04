# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

examples = [
	'simple',
	'bitbang',
	'bitbang2',
	'bitbang_cbus',
	'bitbang_ft2232',
	'find_all',
	'serial_test',
	'baud_test',
	'stream_test',
	'eeprom',
	'async',
	'purge_test',
]

examples_include_directories = include_directories('.')

foreach example : examples
	executable(
		example,
		files(
			'@0@.c'.format(example),
		),
		# Make sure getopt and friends work and will be defined
		c_args: ['-D_POSIX_SOURCE', '-D_GNU_SOURCE'],
		include_directories: examples_include_directories,
		dependencies: ftdi1_dep,
		install: false,
		native: native,
	)
endforeach

examples_pp = [
	'find_all_pp'
]

foreach example : examples_pp
	executable(
		example,
		files(
			'@0@.cpp'.format(example),
		),
		include_directories: examples_include_directories,
		dependencies: ftdipp1_dep,
		install: false,
		native: native,
	)
endforeach
