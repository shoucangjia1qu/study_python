# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:42:58 2018

@author: ecupl
"""

import os;
os.chdir(r"D:\mywork\test")
import numpy as np;
import pandas as pd;
#%%
#字符串切片
c1='1234567890'
c2=c1[0]
c2=c1[:3]
c3=c1[4:7]
c4=c1[-1]
c5=c1[-3:]
c6=c1[:-3]
c7=c4+c6

#%%
#列表
students=['小明','xiaoli',3,1.02,True]
students[len(students)-1]   #元素切片
students[-1]
students[1:4]
students[3]=10.2  #元素修改

#元组
students1=('小明','xiaoli',3,1.02,True)
#不支持修改

#集合
a=set("aabcdefgfg123456")
b=set("efghij123789")
set(a)  #去重
list1=[1,2,'d','w','h','s',1,'2','dq']
set(list1)
print(a|b)  #并集
print(a&b)  #交集
print(a-b)  #差集

#字典
dic={1:'one',2:'two'}
dic[1]
dic2={'爱好':'不详','身高':175}
dic2['姓名']='zhangsan'   #加入新的映射
dic2.keys()
dic2.values()
dic2.pop('爱好')   #删除

#%%
#Python面向对象
a='abcahdbahasa'
a.upper()
a.title()
a.split(sep='a')  #按照'a'进行切分
a.count('a')

b='abasdhwhdi1822dwaisnc12wqcnsbcihwqiucasn c1cbw\
asbcqbadqwba'
c='''
12e2qwdasx
asfjda123
'''
print(c)


#%%
#for循环
k=0
for i in range(0,3):
    print("*******")
    print ('i=%d'%i)
    print('k=%d'%k)
    k=k+1

k=0
for i in [1,3,5]:
    print("*******")
    print ('i=%d'%i)
    print('k=%d'%k)
    k=k+1

k=0
for i in range(0,10,2):
    print("*******")
    print ('i=%d'%i)
    print('k=%d'%k)
    k=k+1

#累加
a=0
for i in range(1,101,1):
    a=a+i
print('结果是：%d'%a)

#阶乘
b=1
for j in range(1,6,1):
    b=b*j
print('结果是：%d'%b)

#range不能使用float型
#range(0,5,1.5) IS Wrong

for k in 'abc100':
    print(k)

#while循环语句
b=0
a=5
while a :
    print (a)
    b=b+a
    print(b)
    a=a-1



#if条件语句
c='ha'
if c=='hungury':
    print('吃东西')
elif c=='thirsty':
    print('喝水')
elif c=='hot':
    print('吹空调')
else:
    print('其他')

#continue和break用法
s=0
for i in range(1,101):
    s=s+i
    if i==50:
        break
print(s)
#1275

s=0
for i in range(1,101):
    s=s+i
    if i==50:
        continue
print(s)
#5050

#%%
#函数
def area(length,width):
    area=length*width
    return area
mianji=area(4,5)

def ctof(c):
    f=c*1.8+32
    return f
inputc=float(input("请输入摄氏温度："))    #input输入是字符串格式
print("华氏温度是：%5.1f度" % ctof(inputc))

#参数缺省值
def area(length,width=10):
    area=length*width
    return area
area(5,5)
area(6)

#不定参数
def multi(*factors):
    result=1
    for factor in factors:
        result *= factor
    return result
multi(2,3)
multi(2,3,5)
multi(2,3,5,10)

#局部变量和全局变量
def scope():
    var1=1
    print(var1,var2)
var1 = 10
var2 = 20
scope()

#spilt分割
a="张三,李四,王五"
a.split(sep=',')
#spilt分割两次
a='今天天气真好，我们一起出去玩。天气又有点热了，我们回家了。'
b=a.split('。')
for i in [0,1]:
    print(b[i].split('，'))
    print('%d'%i)

#%%内置函数梳理
abs(-10)   #10,返回绝对值
chr(0x61)    #返回对应的字母
divmod(7,2)    #返回商和余数
float('100')    #转换成浮点型
hex(34)     #转换成十六进制,0x22
int(34.99)  #34,转换成整型
len([1,2,3,4,5,6]) #返回元素个数
len((1,2,3))
oct(34)     #转换为八进制
ord('我')    #返回unicode编码
pow(2,3)    #2的3次方
pow(2,3,7)  #2的3次方除以7的余数
round(1313.65,1) #
sorted([3,4,1,5,2,7,6]) #由小到大排序
str(35)     #转换为字符
sum((1,2,3,4,5))    #求和，元组或者列表
type('我')   #返回对象类型

#%%
#remove删除指定文件（相对路径、绝对路径）
file='test1.txt'
if os.path.exists(file):
    os.remove(file)
else:
    print(file+'文件未找到')     #用 + 连接字符串打印
#mkdir创建指定目录（相对路径）
dir='mydir'     
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print('%s目录已存在'%dir)    #用%s连接字符串打印
#mkdir创建绝对路径
os.mkdir('D:\\mywork\\test\\newdir\\new')
os.mkdir('newdir\\new1')
#rmdir删除指定目录（相对路径、绝对路径）
dir='mydir'
if os.path.exists(dir):
    os.rmdir(dir)
else:
    print(dir+"目录不存在")      #用 + 连接字符串打印
    

#os.system用法
file1='test1.txt'
file2='study0715.py'
filename=os.path.abspath('study0715.py')
os.path.dirname(filename)       #括号内要有路径，返回当前文件所在的路径
#取当前文件的路径
curr_path=os.getcwd()
#查看上级目录
os.path.dirname(curr_path)
#查看当前文件夹下所有文件
os.listdir(curr_path)
#文件名称
pathname=os.path.basename(file)
#文件绝对路径
abspath=os.path.abspath(file1)
#获取文件大小
os.path.getsize(file2)
#拆分路径和文件
a,b=os.path.split(abspath)
#拆分磁盘和路径名
c,d=os.path.splitdrive(abspath)
#组合路径和文件
a_b=os.path.join(a,b)
c_d=os.path.join(c,d)
#文件重命名
os.rename('mydir2','newdir')

#os.walk用法
sample=os.walk(curr_path)
for a,b,c in sample:
    print(a)
    print(b)
    print(c)
    print()

#%%
#shutil包用法，跨平台文件处理
import shutil
path2=curr_path+'\\newdir'
shutil.copy('test1.txt',path2)      #复制到目录下
path3=curr_path+'\\newdir\\new.txt'
shutil.copy('test2.txt',path3)      #复制到目标文件的目录下并改名

#%%
#glob包用法，返回指定的文件列表
import glob
#找到文件名
list_glob=glob.glob('new*')+glob.glob('study0715.py')+glob.glob('*.txt')
for i in list_glob:
    print(i)
    print('********')

glob.glob('abc\\new*')


#%%
#open()用法
#w模式，覆盖原文
f=open('test2.txt','w')
f.write('this is a test')
f.close()
#a模式，加到最后
f=open('test2.txt','a')
f.write('''
        this is endding test''')
f.close()
#r模式，可以打印出来
f=open('test2.txt','r')
for i in f:
    print(i)
    print('*')
#创建新的文件并写入信息
f=open('test2.xls','w')
f.write('''
        this is endding test
        a
        b
        ''')
f.close()
#with open用法无需close
with open('test2.xls','r') as f:
    for i in f:
        print(i)
        print('********')

#encoding用法
with open('test2.xls','w',encoding='utf-8') as f:
    f.write('''你好
        嗯
        很好''')
f=open('test2.txt','r')
f.readlines()
f.readline()        #一行行取数


#%%文本转字典
#写入文本
with open('password.txt','w',encoding='utf-8') as f:
    f.write("{'aodacat':'zw199256','qita':'123456'}")
#读入文本，将文本转变为dict
import ast
with open('password.txt','r',encoding='utf-8-sig') as rf:
    readf=rf.read()
    data=ast.literal_eval(readf)

#清除屏幕
os.system('cls')

