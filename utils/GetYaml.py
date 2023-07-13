#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/5/14 15:19 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz
import logging
import yaml


class DataUtils:
	def __init__(self, filedir):
		self.path = filedir
		self.data = 1
	def load_yaml(self):
		try:
			f = open(self.path, encoding="utf-8")
			self.data = yaml.full_load(f)
			f.close()
			return self.data
		except Exception as msg:
			logging.debug("文件打开异常->{0}".format(msg))

