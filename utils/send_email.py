#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/5/21 14:42 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz

import yagmail


def send_report():
	to = [
		"471674181@qq.com",
		"sssss@163.com"
	]
	subject = "测试报告"
	body = "hi,all,vxxx版本测试完成，可以提交发版~测试报告详见附件"
	# attachments = [
	# 	conftest.BASE_DIR.REPORTS_HTML_DIR
	# ]
	yag = yagmail.SMTP(user='syz_stone@163.com', password="AESZHBYQVSZGNUCU", host="smtp.163.com",
					   )
	yag.send(to=to, subject=subject, contents=body)
