#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2023/6/11 14:52 
# @Author : 北京-瑛智
# @wechat : shiyingzhisyz
import pytest
import requests
from jsonpath import jsonpath
host = "https://newecshop.longtest.cn"
data = [
	{"user": "syz", "passwd": "123456"}
]
import jsonschema
schema = {
	"type": "object",
	"properties": {
		"msg": {"type": "string", "pattern": "登录成功"},
		"code": {"type": "string", "pattern": "[0-9]"},
		"data": {"type": "object"}
	}
}


def test_user_login():
	url_path = "https://newecshop.longtest.cn/shopapi/index.php/user/login"
	res = requests.post(url=url_path, data=data[0], verify=False)
	assert res.status_code == 200
	assert res.json()["code"] == "1"
	assert jsonpath(res.json(), "$.code")[0] == "1"
	assert jsonpath(res.json(), "$..user") is not None
	jsonschema.validate(instance=res.json(), schema=schema)
	return res.json().get("data").get("token")


def test_user_order(get_key):
	url = "https://newecshop.longtest.cn/shopapi/index.php/user/order"
	parmas = {
		"key": get_key
	}
	res = requests.get(url=url, params=parmas, verify=False)
	print(res.json())

def test_user_info(get_key):
	url = "https://newecshop.longtest.cn/shopapi/index.php/user/userinfo"
	parmas = {
		"key": get_key
	}
	res = requests.get(url=url, params=parmas, verify=False)
	print(res.json())
	assert res.status_code == 200
	assert res.json["code"] == "1"
	assert res.json["msg"] == "获取用户信息成功"