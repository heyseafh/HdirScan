# __author:heysea
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os

def get_ip_list(url):
	headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'Host':'zhannei.baidu.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
	web_data = requests.get(url=url,headers=headers)
	if '200' not in web_data:
		print("访问失败，可能是禁了ip，当前访问页面状态码:%s" % (web_data))
	soup = BeautifulSoup(web_data.text,'html.parser')
	ips = soup.find_all('tr')
	fhttp = open("HTTP_IP.txt",'a')
	fhttps = open("HTTPS_IP.txt",'a')
	fsocks = open("socks_IP.txt",'a')
	for i in range(1,len(ips)):
		ip_info = ips[i]
		tds = ip_info.find_all('td')
		print("IP:{}    port:{}    noun:{}".format(tds[1].text,tds[2].text,tds[5].text))
		item = str(tds[1].text) + ',' + str(tds[2].text) + ',' +str(tds[5].text) + '\n'
		if 'HTTP' in item and len(tds[5].text) == 4:
			fhttp.write(item)
		if 'HTTPS' in item:
			fhttps.write(item)
		if 'socks4/5' in item:
			fsocks.write(item)
	fhttp.close()
	fhttps.close()
	fsocks.close()




if __name__=="__main__":
	if (os.path.exists("HTTP_IP.txt")):  #判断文件是否存在，存在返回True，否则返回False
		os.remove("HTTP_IP.txt")  #删除存在的文件，为了追加的写入方式写入的数据不重复
	if (os.path.exists("HTTPS_IP.txt")):  
		os.remove("HTTPS_IP.txt")
	if (os.path.exists("socks_IP.txt")):  
		os.remove("socks_IP.txt")	  #突然想到直接在这里就以w方式打开文件，就不需要考虑以追加的写入方式写入的数据重复的问题
	for i in range(1,11):		#设爬取代理的范围
		target_url = "https://www.xicidaili.com/nn/" + str(i)
		get_ip_list(target_url)