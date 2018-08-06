# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 11:12:09 2018

@author: ecupl
"""

import os
import pandas as pd
#第一种创建方法：直接字典创建
df1 = pd.DataFrame({'小明':[90,80,70,85],"小红":[90,95,75,85],"小光":[100,90,90,100]})
#第二种：设置data,columns,index
data = [[90,80,70,85],[90,95,75,85],[100,90,90,100]]
columns = ["语文","数学","英语","综合"]
index = ["小明","小红","小光"]
df2 = pd.DataFrame(data,columns = columns,index = index)
#修改行列标签
df2.index = [1,2,3]
df2.columns = range(1,8,2)
df1.index = range(2,10,2)

#%%
#数据选取
df2[['数学','语文']]        #选列
df2[df2.数学>=90]         #选行
df2[df2['综合']==100]         #选行
df2.values          #获取值，以列表形式返回
df2.values[1]       #获取第二行值

#数据切片
#loc选名称
df2.loc["小明","数学"]
df2.loc["小明",:]
df2.loc["小明","语文":"英语"]
df2.loc["小明",["语文","英语"]]
df2.loc["小明":"小光",["语文","英语"]]
df2.loc[("小明","小光"),["语文","英语"]]        #用()者[]都可以
df2.loc["小明":"小光","语文":"英语"]            #选标签名字的时候，前包后也包

#iloc选位置
df2.iloc[0:2,0:2]           #选位置的时候，前包后不包

#ix选名称或者位置

df2.ix["小明":"小光",0:2]   #选标签和选位置混合用法

#%%
#数据修改和排序
df2.ix["小明",:] = 100    #把“小明”这一行全部改成100

df3 = df2.sort_values(["综合","语文"],ascending = False)    #按值降序排序
df4 = df2.sort_index(axis=0,ascending = False)          #按行标签降序排序
df4 = df2.sort_index(axis=1)                        #按列标签升序排序

#删除连续多行
df2.index[1:3]
df2.drop(df2.index[1:3])
#删除连续多列
df2.columns[1:3]
df2.drop(df2.columns[1:3],axis=1)
#删除指定多列
df2.columns[[1,3]]
df2.drop(df2.columns[[1,3]],axis=1)

#绘图
#显示中卫
from pylab import *
rcParams['font.sans-serif'] = ['SimHei']
#DataFrame绘图
df2.plot()


#%%
#导入数据
tables = pd.read_html("http://value500.com/M2GDP.html")
n=1
for table in tables:
    print("第%d个表格"%n)
    print(table.head())
    print("\n")
    n+=1

table = tables[18]
#删除原标签行
table.drop(0,inplace=True)
#修改列名
table.columns=["年份","M2指标","GDP绝对额","M2/GDP"]
#修改行名
table.index = range(len(table.index))           #修改
table.reset_index(drop=True,inplace=True)       #重设












