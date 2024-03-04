# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

ftdipp1_includes = include_directories('.')

ftdipp1_sources = files(
	'ftdi.cpp',
)

ftdipp1_headers = files(
	'ftdi.hpp',
)

ftdipp1_lib = library(
	'ftdipp1',
	ftdipp1_sources,
	include_directories: [ftdi1_includes, ftdipp1_includes],
	dependencies: [boost, libusb, ftdi1_dep],
	version: version_fixup,
	soversion: 3,
	install: install_targets or build_shared,
	native: native,
)

ftdipp1_dep = declare_dependency(
	link_with: ftdipp1_lib,
	include_directories: ftdipp1_includes,
	dependencies: [ftdi1_dep],
)

meson.override_dependency('libftdipp1', ftdipp1_dep, native: native)

if install_targets
	install_headers(
		ftdipp1_headers,
		subdir: 'libftdipp1',
	)
endif
