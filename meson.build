# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

project(
	'libftdi1',
	'c',
	version: '1.5',
	default_options: [
		'buildtype=debugoptimized',
		'c_std=c11',
		'cpp_std=c++11',
	],
	meson_version: '>= 0.59',
	license: 'LGPL-2.1 OR (LGPL-2.1 AND GPL-2.0)',
	subproject_dir: 'deps',
)

pkg = import('pkgconfig')

native = meson.is_cross_build() and get_option('build_native')
cc = meson.get_compiler('c', native: native)
add_languages('cpp', native: native)

version = meson.project_version().split('.')

version_fixup = '@0@.@1@.0'.format(version[0].to_int() + 1, version[1])

if get_option('optimization') == '0'
	add_project_arguments('-DDEBUG', language: ['c', 'cpp'], native: native)
endif

library_mode = get_option('default_library')
build_shared = library_mode in ['shared', 'both']
install_targets = get_option('install_targets')
ftdipp = get_option('ftdipp')
tests = get_option('tests')
ftdi_eeprom = get_option('ftdi_eeprom')
examples = get_option('examples')

libusb = dependency('libusb-1.0', native: native)
doxygen = find_program('doxygen', required: get_option('docs'), disabler: true, native: true)
generate_doxyfile = find_program('meson/generate_doxyfile.py', required: true, native: true)
boost = dependency('boost', required: ftdipp, disabler: true, native: native)
confuse = dependency('confuse', required: ftdi_eeprom, disabler: true, native: native)
libintl = dependency('intl', required: false, native: native)
boost_test = dependency('boost', modules: ['unit_test_framework'], required: tests, disabler: true, native: native)

subdir('doc')

subdir('src')

if ftdipp.allowed()
	# Meson does not allow subprojects in random directories
	subdir('ftdipp')
endif

# if python_bindings.allowed()
# 	subdir('python')
# endif

if ftdi_eeprom.allowed()
	subdir('ftdi_eeprom')
endif

# MSVC lacks unistd.h
if examples.require(host_machine.system() != 'windows',
					error_message: 'Examples cannot be built under Windows').allowed()
	subdir('examples')
endif

subdir('packages')

subdir('test')

pkg.generate(
	ftdi1_lib,
	url: 'Intra2net AG <libftdi@developer.intra2net.com>',
	description: 'Library to program and control the FTDI USB controller',
)

pkg.generate(
	ftdipp1_lib,
	url: 'Intra2net AG <libftdi@developer.intra2net.com>',
	description: 'C++ wrapper for libftdi1',
)

libftdi1_config = configure_file(
	input: 'libftdi1-config.in',
	output: 'libftdi1-config',
	configuration: {
		'prefix': get_option('prefix'),
		'exec_prefix': get_option('prefix') / get_option('bindir'),
		'includedir': get_option('prefix') / get_option('includedir'),
		'libdir': get_option('prefix') / get_option('libdir'),
		'VERSION': meson.project_version(),
		'LIBS': '',
	}
)

install_data(
	libftdi1_config,
	install_dir: get_option('bindir'),
	install_mode: 'rwxr-xr-x',
)
