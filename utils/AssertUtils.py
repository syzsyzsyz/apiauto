#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/5/14 16:43 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz
import logging
import pytest_check as check


class AssertUtils:

	def assert_equal(self, actual, expected):
		logging.debug("断言 %s 等于 %s" % (actual, expected))
		check.assert_equal(actual, expected)

	def assert_true(self, actual):
		logging.debug("断言 %s 是True" % actual)
		check.is_true(actual)

	def assert_false(self, actual):
		logging.debug("断言 %s 是True" % actual)
		check.is_false(actual)