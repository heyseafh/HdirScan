# __author:heysea
# -*- coding: utf-8 -*-

import requests
from queue import Queue
import sys
import threading
import random

class DirScan(threading.Thread):
	
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while (not self._queue.empty()):	#只要队列不为空就继续从队列中取url路径
			url = self._queue.get()
			proxy = {}
			line = DirScan.enable_ip()
			ip,port,types = line.split(',',3)
			types = types.rstrip('\n')
			
			if types == "HTTPS" or types == "https":
				proxy[types.lower()] = '%s:%s' % (ip,port)		#这里分两种情况是因为用requests.get方式加载代理访问目标https不需要在value里加https
			else:
				proxy[types.lower()] = 'http://%s:%s' % (ip,port)		#用requests.get方式加载代理访问目标http需要在value里加http


			try :
				headers = {
					'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
					'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
					'Accept-Encoding':'gzip, deflate',
					'Connection':'keep-alive',
					'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
				# print(url)		#显示当前扫描的url
				r = requests.get(url=url,headers=headers,timeout=9,proxies=proxy,verify=False)

				# if r.status_code == 200 :
				# 	sys.stdout.write('[*] %s\n' % url)    #显示状态码为200的url
				print("URL:%s    status:%s" % (url,r.status_code))
			except Exception:
				# print(url+"     Error")		#显示哪些url错误出现异常，而这里会出现异常多半就是代理问题
				pass

	def enable_ip():
		ip = []
		fr =open("enable_ip\\enable_ip.txt",'r')
		lines = fr.readlines()
		for line in lines:
			ip.append(line)
		tag = random.randint(0,len(ip)-1)		#随机获取当前可用代理池的ip
		# print(ip[tag])
		return ip[tag]

def start(url,ext,count):
	queue = Queue()

	f = open('dict\\%s.txt' % ext,'r')  #根据当前目标语言类型加载字典
	for i in f:
		queue.put(url + i.rstrip('\n'))    #删除字典中每行末尾的换行符并将拼接的url字符串推入栈中

	threads = []
	thread_count = int(count)

	for i in range(thread_count):
		threads.append(DirScan(queue))

	for t in threads:
		t.start()

	for t in threads:
		t.join()


if __name__ == '__main__' :
	url = 'http://www.cscb.cc/'		#设置扫描目标
	ext = 'jsp'		#设置字典类型
	count = 5    #设定线程数
	start(url,ext,count)