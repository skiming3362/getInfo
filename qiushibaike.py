#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import re

class QSBK:
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
		self.headers = {'User-Agent': self.user_agent}
		self.stories =[]
		self.enable = False

	def getPage(self,pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)	
			req = request.Request(url, headers = self.headers)
			resp = request.urlopen(req)
			pageCode = resp.read().decode('utf-8')
			return pageCode

		except request.URLError as e:
			if hasattr(e,"code"):
				print (e.code)
			if hasattr(e,"reason"):
				print (e.reason)

	def getPageItems(self,pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print ("页面加载失败...")
			return None
		pattern = re.compile(r'<div.*?author clearfix">.*?<a.*?<h2>(.*?)</h2>'+
			r'.*?<div class="content">.*?<span>(.*?)</span>'+
			r'.*?</div>.*?</a>(.*?)'+
			r'<div class="stats">.*?<i class="number">(.*?)</i>',re.S)
		items = re.findall(pattern,pageCode)
		pageStories = []
		for item in items:
			haveImg = re.search("img",item[2])
			if not haveImg:
				replaceBR = re.compile('<br/>')
				text = re.sub(replaceBR,"\n",item[1])
				pageStories.append([item[0].strip(),text.strip(),item[3].strip()])
		return pageStories

	def loadPage(self):
		if self.enable:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1

	def getOneStory(self,pageStories,page):
		for story in pageStories:
			value = input()
			self.loadPage()
			if value == "Q":
				self.enable = False
				return
			result = "第%d页\t作者：%s\t赞：%s\n%s" %(page,story[0],story[2],story[1])
			try:
				print (result)
			except UnicodeEncodeError as e:
				print (e)
			
	def start(self):
		print ("正在读取，按回车查看下一个，Q退出")
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories)>0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()