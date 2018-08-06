# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 10:31:59 2018

@author: ecupl
"""

#判断文件是否有过更新
import hashlib
md5=hashlib.md5()
md5.update(b"Test String")
print(md5.hexdigest())
#另一种方法
md5_2=hashlib.md5(b"Test String").hexdigest()
#判断是否一致
md5.hexdigest()==md5_2          #True,结果一致

#检查网页是否更新
import os , requests , hashlib
os.chdir(r"D:/mywork/test")
url="http://news.sina.com.cn/"
html=requests.get(url)
html_text=html.text.encode('utf-8-sig')
md5 = hashlib.md5(html_text).hexdigest()
if os.path.exists("old_md5.txt"):
    with open("old_md5.txt","r") as f:
        old_md5=f.read()
    with open("old_md5.txt","w") as f:
        f.write(md5)
else:
    with open('old_md5.txt','w') as f:
        f.write(md5)
if md5 != old_md5:
    print("数据已更新。")
else:
    print('数据未更新，从数据库读取。')

