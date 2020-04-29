要注意脚本运行次序，运行次序如下

1、request_ip.py    #爬取高匿代理IP并分类保存

2、check_ip.py		#检验代理IP是否有用并将可用代理IP保存到enable_ip\enable_ip.txt

3、HdirScan.py		#加载可用代理IP，多线程扫目录

在使用HdirScan.py需要设置目标url、字典类型、线程数，具体如下：

if __name__ == '__main__' :
	url = 'http://www.cscb.cc/'		#设置扫描目标
	ext = 'jsp'		#设置字典类型
	count = 5    #设定线程数
	start(url,ext,count)
	
自己把这三个脚本合成一个脚本吧，后期会搞个HdirScan.py  2.0，做一个GUI出来，使用起来更舒服