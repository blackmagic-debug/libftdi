# SPDX-FileCopyrightText: 2024 L. E. Segovia <amy@amyspark.me>
# SPDX-License-Identifier: BSD-3-Clause

cpp_tests_sources = files(
	'basic.cpp',
	'baudrate.cpp',
)

test_libftdi1 = executable(
	'test_libftdi1',
	dependencies: [ftdi1_dep, boost_test]
)

test(
	'test_libftdi1',
	test_libftdi1,
)
