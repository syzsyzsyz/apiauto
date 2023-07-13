#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/5/28 14:14 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

class Caps:
	# 自动选择涉设备不启动app
	caps_auto_device_notstart = {
		'platformName': 'Android',
	}

	#指定启动的app
	caps_for_calculators = {
		'platformName': 'Android',
		# "autoLaunch": True,
		'deviceName': '127.0.0.1:7555',
		# 'app': 'D:\自动化\计算器.apk',
		'appPackage': 'com.ibox.calculators',
		# 'appActivity': '.CalculatorActivity'
		'appActivity': '.SplashActivity'
	}

	caps_for_xiaomishop = {
		'platformName': 'Android',
		# "autoLaunch": True,
		'deviceName': '127.0.0.1:7555',
		'appPackage': 'com.xiaomi.shop',
		'appActivity': 'com.xiaomi.shop.activity.MainTabActivity'
}

	# 后续可以根据实际情况补充
