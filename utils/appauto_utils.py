#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/6/4 11:37 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

from appium import webdriver

class appauto():
	def __init__(self, driver):
		# self.driver = webdriver.Remote()
		self.driver = driver
	def swipe_utils(self, k = 1, defult = "top_bottom"):
		self.size = self.driver.get_window_size()
		self.width, self.height = self.size['width'], self.size['height']
		if defult == "top_bottom":
			self.startx, self.starty =  0.5 * self.width,0.2 * self.height
			self.endx, self.endy = self.startx, 0.8 * self.height
		elif defult == "bottom_top":
			self.startx, self.starty = 0.5 * self.width, 0.8 * self.height
			self.endx, self.endy = self.startx, 0.2 * self.height
		elif defult == "left_right":
			pass
		elif defult == "right_left":
			pass
		self.driver.swipe(self.startx, self.starty, self.endx, self.endy, k)
