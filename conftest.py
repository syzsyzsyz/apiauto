#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/5/28 14:08 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

import os,pytest
from pathlib import Path
from datetime import datetime
from appium import webdriver

from utils.Caps import Caps
from utils.GetYaml import DataUtils
from utils import send_email


from testcase import test_user_api
@pytest.fixture()
def get_key():
	return test_user_api.test_user_login()
class BASE_DIR:
	PROJECT_DIR = Path(__file__).parent
	LOGS_DIR = PROJECT_DIR / "logs"
	REPORTS_DIR = PROJECT_DIR / "reports"
	REPORTS_DATA_DIR = REPORTS_DIR / "report_data"
	REPORTS_HTML_DIR = REPORTS_DIR / "report_html"
	SCREENSHOT = REPORTS_DIR / "screenshot"
	TEST_DATA_DIR = PROJECT_DIR / "testdata"

@pytest.fixture
def setup_teardown():
	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Caps.caps_for_xiaomishop)
	# driver.launch_app()
	yield driver
	# driver.close_app()
	driver.quit()

@pytest.fixture
def logs_dir():
	return BASE_DIR.LOGS_DIR

@pytest.fixture
def datautils():
	return DataUtils

def pytest_addoption(parser):
	#添加ini配置项
	parser.addini('send_email', help='auto send email or not')
	parser.addini('gen_report', help="allure generate html or not")

#读取ini配置文件钩子函数
def pytest_configure(config):
	NOW = datetime.now()
	log_file = config.getini('log_file')
	if log_file:
		log_file = NOW.strftime("%Y-%m-%d_%H-%M-%S")
		config.option.log_file = BASE_DIR.LOGS_DIR / (log_file + ".log")
	if config.getini("gen_report"):
		config.option.allure_report_dir = BASE_DIR.REPORTS_DATA_DIR

#在用例执行完后执行
def pytest_terminal_summary(terminalreporter,exitstatus,config):
	if config.getini("gen_report"):
		#report_cmd = "allure generate %s -o  %s --clean"%(BASE_DIR.REPORTS_DATA_DIR,BASE_DIR.REPORTS_HTML_DIR)
		#report_cmd = "allure generate {0} -o  {1} --clean".format(BASE_DIR.REPORTS_DATA_DIR,BASE_DIR.REPORTS_HTML_DIR)
		os.system(f"allure generate {BASE_DIR.REPORTS_DATA_DIR}"
				  f" -o {BASE_DIR.REPORTS_HTML_DIR} --clean")
	# if config.getini("send_email"):
	# 	send_email.send_report()

