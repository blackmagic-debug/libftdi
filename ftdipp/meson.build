# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

include_directories = include_directories('.')

ftdipp1_sources = files(
	'ftdi.cpp',
)

ftdipp1_headers = files(
	'ftdi.hpp',
)

ftdipp1_lib = library(
	'ftdipp1',
	ftdipp1_sources,
	dependencies: [boost, libusb, ftdi1_dep],
	version: version_fixup,
	soversion: 3,
	install: true,
)

ftdipp1_dep = declare_dependency(
	link_with: ftdipp1_lib,
	include_directories: include_directories,
)

meson.override_dependency('libftdipp1', ftdipp1_dep)

install_headers(
	ftdipp1_headers,
	subdir: 'libftdipp1',
)

