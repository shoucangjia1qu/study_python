# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:01:45 2018

@author: ecupl
"""

#解析网站
from urllib.parse import urlparse
url="http://www.pm25x.com/city/shanghai.htm"
o=urlparse(url)
print("scheme={}".format(o.scheme))     #通信协议
print("netloc={}".format(o.netloc))     #网站名称
print("port={}".format(o.port))         #通信端口
print("path={}".format(o.path))         #文件路径
print("query={}".format(o.query))       #GET的参数
print("fragment={}".format(o.fragment)) #框架名称
print("params={}".format(o.params))     #url查询参数params

#抓取网页数据，返回源代码
import requests
url='http://www.wsbookshow.com/'
html = requests.get(url)
html.encoding="GBK"
print(html.text)
#用in模式找到源代码中的内容
if "新概念" in html.text:
    print("找到了")
#逐行搜索,查看找到次数
html_text=html.text
html_lines=html_text.splitlines()        #将文本分行
n=0
for row in html_lines:
    if "新概念" in row:
        n+=1
print("找到%d次"%n)

#正则表达式抓取网页内容
import re
pat = re.compile('[a-z]+')
#match(string)方法：从首个字符开始
m = pat.match("abc345")
print(m)
print(m.group())    #返回符合正则的字符串
print(m.start())    #返回开始位置
print(m.end())      #返回结束位置
print(m.span())     #返回搜索结果位置
#直接调用match方法
m=re.match(r'[a-z]+',"tempo123")
print(m)

#search(string)方法：找到符合要求的，第一个不符合规则就结束
pat=re.compile("[a-z]+")
m = pat.search("123abcABC456abc")
print(m)

#findall(string)方法：找到所有符合表达式的结果并用列表返回
pat=re.compile("[a-z]+")
m=pat.findall("123abcABC456def")
print(m)


#%%
#案例1:爬取邮件
import requests,re
regex=re.compile('[a-zA-Z0-9-]+@[\w-]+\.[\w-]+')    #写好正则表达式
url="http://www.wsbookshow.com/"                    #需要爬取的网址
html=requests.get(url)                              #网址转成text
emails=regex.findall(html.text)                     #进行匹配 
print(emails)

#%%
#BeautifulSoup包
from bs4 import BeautifulSoup
url="https://www.baidu.com/"
html=requests.get(url)
html.encoding='utf-8'
#html_text=html.text
sp = BeautifulSoup(html.text,'html.parser')
sp.title  #<title>百度一下，你就知道</title>
sp.text   #去标签的文档内容
sp.find('a')         #找到符合要求的第一个标签
sp.find_all('a')     #找到符合要求的所有标签，并返回列表
sp.select('a')       #抓取a标签
sp.select("#u1")     #抓取id=u1的内容
sp.select(".bri")  #抓取class=title的内容
sp.select("html head title")    #抓取<html>下<head>下的<title>
sp.find_all("div",{'id':'u1'})  #通过find抓取对应的属性
sp.find_all('a').get('href')        #抓取属性内容
sp.find("a").get("name")
sp.find("a").get("class")

#%%
#案例2：抓取超链接
url="http://www.wsbookshow.com/"
html=requests.get(url)
html.encoding="GBK"
html_text=html.text
sp=BeautifulSoup(html_text,'html.parser')
sp.title
anames=sp.find_all('a')
print(anames)
for everyaname in anames:
    hrefname=everyaname.get("href")
    if hrefname != None and hrefname.startswith("http://"):
        print(hrefname)






