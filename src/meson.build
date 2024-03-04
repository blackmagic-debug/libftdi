# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

ftdi1_includes = include_directories('.')

snapshot_version = 'unknown'

git_describe = run_command(
	find_program('git', required: false, disabler: true),
	'--git-dir',
	meson.project_source_root() / '.git',
	'describe',
	capture: true,
	check: false,
)

if git_describe.returncode() == 0
	snapshot_version = git_describe.stdout().strip()
	message('Detected git snapshot version: @0@'.format(snapshot_version))
endif

ftdi1_version = configure_file(
	input: 'ftdi_version_i.h.in',
	output: 'ftdi_version_i.h',
	configuration: {
		'MAJOR_VERSION': version[0].to_int(),
		'MINOR_VERSION': version[1].to_int(),
		'VERSION_STRING': meson.project_version(),
		'SNAPSHOT_VERSION': snapshot_version,
	}
)

ftdi1_sources = files(
	'ftdi.c',
	'ftdi_stream.c',
)

ftdi1_headers = files(
	'ftdi.h',
)

ftdi1_lib = library(
	'ftdi1',
	[ftdi1_sources, ftdi1_version],
	include_directories: ftdi1_includes,
	dependencies: libusb,
	version: version_fixup,
	soversion: 2,
	install: install_targets or build_shared,
	native: native,
)

ftdi1_dep = declare_dependency(
	link_with: ftdi1_lib,
	include_directories: ftdi1_includes,
)

meson.override_dependency('libftdi1', ftdi1_dep, native: native)

if install_targets
	install_headers(
		ftdi1_headers,
		subdir: meson.project_name()
	)
endif
