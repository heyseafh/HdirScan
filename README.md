要注意脚本运行次序，运行次序如下

1、request_ip.py    #爬取高匿代理IP并分类保存，这里设置爬取代理页面的范围可以访问西刺高匿代理页面有多少页，假设为n页，那么爬取代理的范围就是n+1，如果n=4055，那么设置的爬取范围就是for i in range(1,4056):

2、check_ip.py		#检验代理IP是否有用并将可用代理IP保存到enable_ip\enable_ip.txt

3、HdirScan.py		#加载可用代理IP，多线程扫目录

在使用HdirScan.py需要设置目标url、字典类型、线程数，具体如下：

if __name__ == '__main__' :
	url = 'http://www.Example.cc/'		#设置扫描目标
	ext = 'jsp'		#设置字典类型
	count = 5    #设定线程数
	start(url,ext,count)
	
自己把这三个脚本合成一个脚本吧，后期会搞个HdirScan.py  2.0，做一个GUI出来，使用起来更舒服
