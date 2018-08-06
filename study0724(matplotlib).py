# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 22:04:30 2018

@author: ecupl
"""

import os
os.chdir("D:/mywork/test")
import matplotlib.pyplot as plt

#plot图
plt.figure(figsize=(15,10), dpi=80, facecolor='#ccffff', edgecolor='#ff3333')
listx1=[10,20,30,40,50,60,70,80]
listy1=[2,4,8,16,32,64,128,256]
barx1=[10,20,30,40,50,60,70,80]
bary1=[5,15,14,10,20,15,25,21]
plt.plot(listx1,listy1,linewidth=3.0,color='red',linestyle='-',label='line')
plt.plot(listx1,listy1,'g^',linewidth=5.0)

#另外的plot图
plot(listx1, listy1, color='blue', linestyle='-', marker='^',
         markerfacecolor='red', markersize=10)

#bar图
plt.bar(barx1,bary1,color='black',width=5,label='123')
plt.legend()    #出现label必需
plt.show()
#出现中文必需
from pylab import *
rcParams['font.sans-serif'] = ['SimHei']

#pie图
pie1=[10,20,30,40]
plt.pie(pie1,explode=[0,0.1,0,0],labels=['东','南','西','北'],labeldistance=1.1,
        shadow=True,autopct="%3.1f%%",startangle=90,pctdistance=0.6)
plt.axis('equal')       #图形呈正圆形
plt.legend()
plt.show()

















