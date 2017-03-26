#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request
from http import cookiejar

#创建MozillaCookieJar实例对象
cookie = cookiejar.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = request.Request("http://www.baidu.com")
#利用request的build_opener方法创建一个opener
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print (response.read().decode('utf-8'))