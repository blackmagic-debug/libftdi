# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

doxyfile_cfg = {
	'PACKAGE': meson.project_name(),
	'VERSION': meson.project_version(),
	'top_srcdir': meson.project_source_root(),
}

doxyfile = configure_file(
	input: files(
		'Doxyfile.in'
	),
	output: 'libftdi.dox',
	configuration: doxyfile_cfg
)

doxyfile = configure_file(
	command: [
		generate_doxyfile,
		'--strip', meson.current_source_dir(), meson.current_build_dir(),
		'--output', '@OUTPUT@',
		'@OUTDIR@',
		'@INPUT@',
	],
	input: doxyfile,
	output: 'Doxyfile',
)

doxyfile_xml = configure_file(
	input: files(
		'Doxyfile.xml.in'
	),
	output: 'Doxyfile.xml',
	configuration: doxyfile_cfg
)

docs = custom_target(
	'docs',
	input: doxyfile,
	output: 'html',
	command: [
		doxygen, '@INPUT@'
	],
	depend_files: doxyfile_xml,
	console: true,
	install: true,
	install_dir: get_option('datadir') / meson.project_name(),
)
