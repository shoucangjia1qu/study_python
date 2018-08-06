# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 22:26:13 2018

@author: ecupl
"""

import jieba
import pandas as pd
import numpy as np
data = pd.DataFrame(columns=['c1','c2'])
data=data.append({"c1":"10","c2":"相知无远近 万里尚为邻—2018年7月主席亚非行纪实"},ignore_index=True)
data=data.append({"c1":"20","c2":"商务部新闻发言人就中方拟对部分自美进口产品采取反制措施发表谈话"},ignore_index=True)
data=data.append({"c1":"30","c2":"处警民警赶达现场后，立即开展调查处置工作。在处置过程中，3名犯罪嫌疑人抗拒带离并逃窜，处警民警鸣枪示警并果断处置，现场无人员伤亡."},ignore_index=True)
data=data.append({"c1":"10","c2":"为什么是5%到10%的抽检率？除中检院外，七个省(市)级药品检验机构，为何极少承担疫苗批签发工作？百日咳的研究为何一直没有核心突破？百日咳发病人数为何逐月上涨？"},ignore_index=True)
data=data.append({"c1":"20","c2":"热血沸腾！看强军关键词 "},ignore_index=True)
data=data.append({"c1":"30","c2":"汇集更强动力——非洲各界积极评价主席访非成果 "},ignore_index=True)
cuts=[]
for i in list(data.c2):
    cuts = jieba.lcut(i)+cuts
#计算分词数量
countdata = pd.DataFrame(columns=["cut","count"])
for i in cuts:
    cutcount = cuts.count(i)
    countdata=countdata.append({"cut":i,"count":cutcount},ignore_index=True)
#去重
countdata.drop_duplicates(inplace=True)
#倒序排列
countdata.sort_values(by='count',ascending=False,inplace=True)
#%%



#关键词权重

words = jieba.analyse.textrank('处警民警赶达现场后，立即开展调查处置工作。在处置过程中，3名犯罪嫌疑人抗拒带离并逃窜，处警民警鸣枪示警并果断处置，现场无人员伤亡',withWeight=True) 
words2 = jieba.analyse.extract_tags('处警民警赶达现场后，立即开展调查处置工作。在处置过程中，3名犯罪嫌疑人抗拒带离并逃窜，处警民警鸣枪示警并果断处置，现场无人员伤亡') 
word=[]
weight=[]
for keyword in words:
    (i,j)=keyword
    print(i,j)
    word.append(i)
    weight.append(10000*j)


#词云图
from pyecharts import WordCloud

name = word
value = weight
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.render('abc.html')


#%%
#十九大报告
import requests,os,jieba
from bs4 import BeautifulSoup
from pyecharts import WordCloud
import jieba.analyse
os.chdir(r"D:/mywork/test")
with open("shijiuda.txt","r") as f:
    text = f.readlines()        #也可以直接read()

#去除格式生成新的文本
strs = ""
for i in text:
    i = i.strip()
    strs+=i
#开始分词
cuts = jieba.lcut(strs)
words = jieba.analyse.textrank(strs,topK=20,withWeight=True)
words2 = jieba.analyse.extract_tags(strs,topK=20,withWeight=True) 

listx = []
listy = []
for word,weight in words:
    cutcount = cuts.count(word)
    print(word+"出现{}次".format(cutcount),weight)
    listx.append(word)
    listy.append(weight*10000)

name = listx
value = listy
wordcloud = WordCloud(width=1500, height=1000)
wordcloud.add("十九大报告此图云", name, value, word_size_range=[50, 200])
wordcloud.render('shijiuda.html')

#统计分词数量
dicts={}
for i in cuts:
    dicts[i] = dicts.get(i,0)+1










