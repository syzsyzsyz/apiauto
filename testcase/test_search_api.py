#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/6/11 17:01 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz
import pytest, requests
import random
from jsonpath import jsonpath



def test_search():
	url = "https://newecshop.longtest.cn/shopapi/index.php/first/index"
	params = {
		"order": random.randint(0, 4),
		"filtrate": [],
		"keyword": "手机",
		"type": "search",
		"page":  random.randint(0, 5)
	}
	res = requests.get(url=url, params=params, verify=False)
	print(res.headers)
	print(res.json())
	# assert "手机" in res.json()["data"]["goods"]["title"]
	ls = jsonpath(res.json(), "$..goods[*].title")
	for i in ls:
		assert "手机" in i;