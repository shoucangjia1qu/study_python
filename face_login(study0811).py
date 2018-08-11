# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:28:32 2018

@author: ecupl
"""

#用颜色直方图判断是否同张脸
from PIL import Image
from functools import reduce
import math, operator, cv2, os

os.chdir("D:\\mywork\\test")
#创建识别对象
faceCascade = cv2.CascadeClassifier("D:\\python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
loginface = 'face\\login.jpg'
recogface = 'face\\recog.jpg'

#定义抓取图片的函数
def makeface(filename):
    print('按任意键进入开始截图\n摄像头开启后按Z拍照')
    cv2.namedWindow('face')
    cv2.waitKey(0)
    cap = cv2.VideoCapture(0)       #调用摄像头
    while(cap.isOpened()):
        ret, img = cap.read()     #读取图像
        cv2.waitKey(30)
        #加入框框识别人脸
        peopleface = faceCascade.detectMultiScale(img,scaleFactor=1.2,minNeighbors=3,minSize=(10,10),flags=cv2.CASCADE_SCALE_IMAGE)
        for x,y,w,h in peopleface:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        if ret==True:
            cv2.imshow('face',img)
            k=cv2.waitKey(30)
            if k==ord('z') or k==ord('Z'):  #判断是否为按了Z
                cv2.imwrite(filename,img)
                break
    cv2.waitKey(500)
    face = Image.open(filename)
    face1 = face.crop((x,y,x+w,y+h))
    face2 = face1.resize((200,200),Image.ANTIALIAS)
    face2.save(filename)
    cap.release()
    cv2.destroyAllWindows()


if os.path.exists('face\\recog.jpg'):
    makeface(loginface)
    pic1 = Image.open('face\\recog.jpg')
    pic2 = Image.open('face\\login.jpg')
    h1=pic1.histogram()     #16等分，3组
    h2=pic2.histogram()
    diff = math.sqrt(reduce(operator.add, list(map(lambda a,b:(a-b)**2,h1,h2)))/len(h1))
    if diff<=100:
        print("检验通过。diff=%.2f"%diff)
    else:
        print("人脸错误，无法登录。diff=%.2f"%diff)
else:
    makeface(recogface)
    print('预测人脸图像拍摄成功。')
#import matplotlib.pyplot as plt
#plt.hist(h2,bins=50) 
#另一种diff计算方式
#diff2 = (sum(list(map(lambda a,b:(a-b)**2,h1,h2)))/len(h1))**0.5



