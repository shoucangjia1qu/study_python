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
import cv2,os
import numpy as np
import pandas as pd

image = cv2.imread("images\\test1.jpg")
#直线
cv2.line(image,(0,300),(140,150),(0,0,255),3)
#矩形
cv2.rectangle(image,(10,10),(60,60),(0,255,0),1)
cv2.rectangle(image,(280,280),(200,200),(0,255,0),-1)
#圆形
cv2.circle(image,(200,200),50,(255,0,0),2)
#多边形
pts =np.array([[50,20],[80,80],[110,20]])
cv2.polylines(image,[pts],1,(0,50,255),2)
#加入文本
cv2.putText(image,"this is a test!",(60,280),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

cv2.imshow('plot',image)
cv2.waitKey(0)

cv2.destroyAllWindows()

#%%
#实现人脸识别
import cv2,os
import numpy as np
import pandas as pd
os.chdir("D:\\mywork\\test")

image = cv2.imread("images\\gyy2.jpg")
faceCascade = cv2.CascadeClassifier("D:\\python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
peopleface = faceCascade.detectMultiScale(image,scaleFactor=1.2,minNeighbors=3,minSize=(10,10),flags=cv2.CASCADE_SCALE_IMAGE)
image.shape     #形状
#加入黑框和文字
cv2.rectangle(image,(10,image.shape[0]-30),(110,image.shape[0]),(0,0,0),-1)
cv2.putText(image,"there are {}".format(len(peopleface)),(10,image.shape[0]-12),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
#加入面部定位
for x,y,w,h in peopleface:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('facedetect',image)
cv2.waitKey(0)
cv2.imwrite("images\\gyy2detect.jpg",image,[int(cv2.IMWRITE_JPEG_QUALITY),80])
cv2.destroyAllWindows()


#抓取脸部图形并保存
from PIL import Image
cutimg = Image.open("images\\gyy2.jpg")
n=1
for x,y,w,h in peopleface:
    face = cutimg.crop((x,y,x+w,y+h))
    face2 = face.resize((100,100),Image.ANTIALIAS)
    face2.save("images\\face\\face%d.jpg"%n)
    n+=1


#合并起来就是
import cv2,os
import numpy as np
import pandas as pd
from PIL import Image
os.chdir("D:\\mywork\\test")

image = cv2.imread("images\\gyy1.jpg")
faceCascade = cv2.CascadeClassifier("D:\\python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
peopleface = faceCascade.detectMultiScale(image,scaleFactor=1.2,minNeighbors=3,minSize=(10,10),flags=cv2.CASCADE_SCALE_IMAGE)
image.shape     #形状
#加入黑框和文字
cv2.rectangle(image,(10,image.shape[0]-30),(110,image.shape[0]),(0,0,0),-1)
cv2.putText(image,"there are {}".format(len(peopleface)),(10,image.shape[0]-12),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
#加入面部定位和截取图片
cutimg = Image.open("images\\gyy1.jpg")
n=1
for x,y,w,h in peopleface:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    face = cutimg.crop((x,y,x+w,y+h))
    face2 = face.resize((100,100),Image.ANTIALIAS)
    face2.save("images\\face\\face%d.jpg"%n)
    n+=1

cv2.imshow('facedetect',image)
cv2.waitKey(0)
cv2.imwrite("images\\gyy1detect.jpg",image,[int(cv2.IMWRITE_JPEG_QUALITY),80])
cv2.destroyAllWindows()

#%%
#抓取摄像头视频图像
cap = cv2.VideoCapture(0)
cap.isOpened()
ret,img = cap.read()
cap.release()
cv2.imwrite("images\\img.jpg",img)








