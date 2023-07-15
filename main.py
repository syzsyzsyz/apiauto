#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/5/28 14:08 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

import os
from conftest import BASE_DIR
import threading
def run():
	file_list = os.listdir(BASE_DIR.LOGS_DIR)
	for i in file_list:
		os.remove(BASE_DIR.LOGS_DIR / i)
	os.system("python3 -m pytest")
if __name__ == "__main__":
	run()
