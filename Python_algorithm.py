# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:00:48 2019

@author: ecupl
"""

######Python算法

###一、双指针问题
##1、单链表，按顺序遍历
listValue = [1, 5, 6, 2, 4, 3]          #数组
listPointer = [3, 2, -1, 5, 1, 4]       #指针
head = 1                        #初始数值的指针
print(listValue[head])          #输出第一个元素
nextP = listPointer[head]       #第一个元素的指针
while nextP != -1:
    print(listValue[nextP])     #输出下一个元素
    nextP = listPointer[nextP]  #变为下一个指针

##2、双链表，按顺序遍历
listValue = [1, 5, 6, 2, 7, 3]          #数组
listRight = [3, 2, 4, 5, -1, 1]         #正序数组指针
listLeft = [-1, 5, 1, 0, 2, 3]          #逆序数组指针
#顺序打印
head = listLeft.index(-1)
print(listValue[head])
nextP = listRight[head]
while nextP > -1:
    print(listValue[nextP])
    nextP = listRight[nextP]
#逆序打印
tail = listRight.index(-1)
print(listValue[tail])
lastP = listLeft[tail]
while lastP > -1:
    print(listValue[lastP])
    lastP = listLeft[lastP]

##3、单链表中添加元素
listValue = [1, 5, 6, 2, 7, 3]          #数组
listRight = [3, 2, 4, 5, -1, 1]         #正序数组指针
addNum = 2.5                            #需要添加的数值
addIdx = 3                              #需要添加数值前一个数值的指针位置
listValue.append(addNum)
listRight.append(listRight[addIdx])
listRight[addIdx] = len(listValue) - 1
#按顺序打印
head = 0
print(listValue[head])
nextP = listRight[head]
while nextP != -1:
    print(listValue[nextP])
    nextP = listRight[nextP]

##4、双链表中添加元素
listValue = [1, 5, 6, 2, 7, 3]          #数组
listRight = [3, 2, 4, 5, -1, 1]         #正序数组指针
listLeft = [-1, 5, 1, 0, 2, 3]          #逆序数组指针
addNum = 4                              #需要添加的数值
addIdx = 5                              #需要添加数值前一个数值的指针位置
listValue.append(addNum)
#顺序指针改变加入指针的指向
listRight.append(listRight[addIdx])
#逆序指针改变加入指针的指向
listLeft.append(addIdx)
#逆序指针
listLeft[listRight[addIdx]] = len(listValue) - 1
#顺序指针
listRight[addIdx] = len(listValue) - 1
#顺序打印
head = listLeft.index(-1)
print(listValue[head])
nextP = listRight[head]
while nextP > -1:
    print(listValue[nextP])
    nextP = listRight[nextP]
#逆序打印
tail = listRight.index(-1)
print(listValue[tail])
lastP = listLeft[tail]
while lastP > -1:
    print(listValue[lastP])
    lastP = listLeft[lastP]

#逆序指针换种方法
listValue = [1, 5, 6, 2, 7, 3]          #数组
listRight = [3, 2, 4, 5, -1, 1]         #正序数组指针
listLeft = [-1, 5, 1, 0, 2, 3]          #逆序数组指针
addNum = 7.5                              #需要添加的数值
addIdx = 4                              #需要添加数值前一个数值的指针位置
listValue.append(addNum)
listLeft.append(listLeft[addIdx])
listLeft[addIdx] = len(listValue) - 1
#逆序打印
tail = listRight.index(-1)
print(listValue[tail])
lastP = listLeft[tail]
while lastP > -1:
    print(listValue[lastP])
    lastP = listLeft[lastP]
   
##单链表中删除元素
listValue = [1, 5, 6, 2, 7, 3]          #数组
listRight = [3, 2, 4, 5, -1, 1]         #正序数组指针
head = 0
delIdx = 1                              #要删除的前一个元素的下标，比如：要删除6，故前一个元素为下标为1
#删除前打印
print(listValue[head])
nextP = listRight[head]
while nextP > -1:
    print(listValue[nextP])
    nextP = listRight[nextP]
#删除，并打印
listRight[delIdx] = listRight[listRight[delIdx]]
print(listValue[head])
nextP = listRight[head]
while nextP > -1:
    print(listValue[nextP])
    nextP = listRight[nextP]

##双链表中删除元素
listValue = [1, 5, 6, 2, 7, 3]          #数组
listRight = [3, 2, 4, 5, -1, 1]         #正序数组指针
listLeft = [-1, 5, 1, 0, 2, 3]          #逆序数组指针
head = 0
delIdx = 1                              #要删除的前一个元素的下标，比如：要删除6，故前一个元素为下标为1
tempa = listRight[listRight[delIdx]]
#顺序删除
listRight[delIdx] = listRight[listRight[delIdx]]
#逆序删除
listLeft[tempa] = delIdx
#顺序打印
head = listLeft.index(-1)
print(listValue[head])
nextP = listRight[head]
while nextP > -1:
    print(listValue[nextP])
    nextP = listRight[nextP]
#逆序打印
tail = listRight.index(-1)
print(listValue[tail])
lastP = listLeft[tail]
while lastP > -1:
    print(listValue[lastP])
    lastP = listLeft[lastP]



###二、哈希算法


















