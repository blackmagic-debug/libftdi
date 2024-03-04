# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

warning('''
	The EEPROM programmer is licensed under GPL 2 (not any later)''')

eeprom_major_version = 0
eeprom_minor_version = 17
eeprom_version = f'@eeprom_major_version@.@eeprom_minor_version@'

eeprom_include_directories = include_directories('.')

ftdi_eeprom_version = configure_file(
	input: 'ftdi_eeprom_version.h.in',
	output: 'ftdi_eeprom_version.h',
	configuration: {
		'EEPROM_MAJOR_VERSION': eeprom_major_version,
		'EEPROM_MINOR_VERSION': eeprom_minor_version,
		'EEPROM_VERSION_STRING': eeprom_version,
	}
)

ftdi_eeprom = executable(
	'ftdi_eeprom',
	files(
		'main.c',
	),
	dependencies: [confuse, libintl, ftdi1_dep],
	install: install_targets,
)

if install_targets
	install_data(
		files(
			'example.conf'
		),
		install_dir: get_option('datadir') / 'doc',
	)
endif
