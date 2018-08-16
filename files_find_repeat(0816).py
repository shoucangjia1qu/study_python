# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:00:27 2018

@author: ecupl
"""

import os, hashlib
os.chdir("D:\\mywork\\test")
cur_path = os.getcwd()
trees = os.walk(cur_path)

allmd5 = dict()
for dirname, subdir, files in trees:
    allpics = []
    #图片存入字典
    for file in files:
        ext = file.split(".")[-1]
        if ext == 'jpg' or ext == 'png':
            allpics.append(dirname+"\\"+file)
    
    if len(allpics) > 0:
        for pic in allpics:
            text = open(pic,"rb").read()
            md5 = hashlib.md5(text).digest()
            if md5 in allmd5:
                print("当前文件为：{}".format(os.path.abspath(pic)))
                print("重复文件为：{}".format(allmd5[md5]))
            else:
                allmd5[md5] = os.path.abspath(pic)