# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:54:18 2018

@author: ecupl
"""

#tesseract数字识别
import subprocess, os
os.chdir("D:\\mywork\\test")
ocr = subprocess.Popen("tesseract  images\\ocr\\code1.jpg  images\\ocr\\code1")
ocr.wait()
with open("images\\ocr\\code1.txt","r") as f:
    text = f.read()
print(text)

#%%
import subprocess, os, cv2
code1 = cv2.imread("images\\ocr\\code1.jpg")

#图片转成灰度模式
cv2.cvtColor(code1,cv2.COLOR_BGR2GRAY)

#转换为黑白
cv2.threshold(code1,150,255,cv2.THRESH_BINARY_INV)

cv2.imwrite('codeheibai.jpg',code1)

cv2.imshow('code',code1)
cv2.waitKey(0)

cv2.destroyAllWindows()










