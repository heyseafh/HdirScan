# __author:heysea
# -*- coding: utf-8 -*-

import requests
from queue import Queue
import sys
import threading
import telnetlib


class Check_IP(threading.Thread):


	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		global lines 
		lines = [] 

		while (not self._queue.empty()):	#只要队列不为空就继续从队列中取url路径
			url = self._queue.get()
			# print(url)

			ip,port,types = url.split(',',3)

			try :
				telnetlib.Telnet(ip,port,timeout=6)		#超过6秒则判定为无效IP代理

				# if r.status_code == 200 :
				# 	sys.stdout.write('[*] %s\n' % url)    #显示状态码为200的url
				print("%s可用" % (url))
				lines.append(url+'\n')
			except Exception:
				print("%s不可用" % (url))

	def write_enable_ip():
		fw = open("enable_ip\\enable_ip.txt",'w')
		for i in range(len(lines)):
			fw.write(lines[i])
		fw.close()			
	
		
def start(txt,count):
	queue = Queue()

	fr = open('%s' % txt,'r',encoding='utf-8')	#按行读取文件内容
	lines = fr.readlines()  
	fr.close()
	for line in lines:
		ip,port,types= line.split(',',3)	#将ip、端口和类型读取并分别赋值
		types = types.rstrip('\n')
		queue.put(ip+','+port+','+types) 

	threads = []
	thread_count = int(count)

	for i in range(thread_count):
		threads.append(Check_IP(queue))

	for t in threads:
		t.start()

	for t in threads:
		t.join()	

if __name__=="__main__":
	txt = 'HTTP_IP.txt'		#设置要验证的代理类型的文件
	count = 8    #设定线程数
	start(txt,count)
	Check_IP.write_enable_ip()
