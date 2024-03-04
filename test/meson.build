# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

cpp_tests_sources = files(
	'basic.cpp',
	'baudrate.cpp',
)

test_libftdi1 = executable(
	'test_libftdi1',
	cpp_tests_sources,
	dependencies: [ftdi1_dep, boost_test],
	install: false,
)

test(
	'test_libftdi1',
	test_libftdi1,
)
