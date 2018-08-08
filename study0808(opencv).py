# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:59:06 2018

@author: ecupl
"""

import cv2,os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir("D:\\mywork\\test")
#打开窗口
cv2.namedWindow('img1')
cv2.namedWindow('img2',cv2.WINDOW_FREERATIO)    #可改变图像和窗口大小
#读取图像
image1 = cv2.imread(r'D:\mywork\test\images\test1.jpg',1)
image2 = cv2.imread('images\\test2.jpg',0)      #以灰度模式读取图像
#在窗口中显示图像
cv2.imshow('img1',image1)
cv2.imshow('img2',image2)
#程序等待，必须加上，不然未响应
cv2.waitKey(0)      #按任意键执行下面程序

#关闭窗口
#cv2.destroyWindow('img1')
cv2.destroyAllWindows()



