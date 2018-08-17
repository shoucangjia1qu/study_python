# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:40:38 2018

@author: ecupl
"""

import os
from PIL import Image
os.chdir("D:/mywork/test")

cur_path = os.getcwd()
target_dir = "resize_image"
width = 200

pathfiles = os.walk(cur_path)
for dirname, subdir, files in pathfiles:
    #判断是否目标文件夹
    basename = os.path.basename(dirname)
    if basename ==target_dir:
        continue
    #保存文件
    ori_files = []
    for file in files:
        ext = file.split(".")[-1]
        if ext=='jpg' or ext=='png':
            ori_files.append(dirname+"\\"+file)
    #更改尺寸并复制文件
    if len(ori_files)>0:
        #创建文件夹
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        for imgfile in ori_files:
            #拆分文件路径和文件名，用于保存
            path,img = os.path.split(imgfile)
            image = Image.open(imgfile)
            wth,hth = image.size
            image = image.resize((width,int(hth*width/wth)))
            #文件保存在母目录下的指定文件夹内
            image.save(cur_path+"\\"+target_dir+"\\"+img)
            print('成功')
            image.close()
    






