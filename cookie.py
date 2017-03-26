#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request
import http.cookiejar

#声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = request.build_opener(handler)
#此处的open方法同request的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
	print ('Name = ' + item.name)
	print ('Value = ' + item.value)