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

#%%
#保存图像
import cv2,os
import numpy as np
import pandas as pd

os.chdir("D:\\mywork\\test")
cv2.namedWindow('SaveImage')
image = cv2.imread('images\\test2.jpg')
cv2.imshow('SaveImage',image)
#cv2.waitKey(0)
cv2.imwrite('images\\test2_copy1.jpg',image)    #图片质量默认为95
cv2.imwrite('images\\test2_copy2.jpg',image,[int(cv2.IMWRITE_JPEG_QUALITY),50])     #图片质量设置为50
cv2.waitKey(0)      #这个等待时间放哪里都行
cv2.destroyWindow('SaveImage')

#%%
#基本绘图








