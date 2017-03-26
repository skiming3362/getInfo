#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request
from http import cookiejar

#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookiejar.MozillaCookieJar(filename)
#利用request的HTTPCookieProcessor对象来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = request.build_opener(handler)
#创建一个请求，原理同request的urlopen
req = request.Request('http://www.baidu.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

response = opener.open(req)
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)