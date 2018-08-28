# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:02:48 2018

@author: ecupl
"""

import pygame

pygame.init()
window=pygame.display.set_mode((640,320))
pygame.display.set_caption("这是设置的标题")
#获取窗口大小，并创建画布
bg = pygame.Surface(window.get_size())
bg = bg.convert()   #创建副本，加快显示速度
bg.fill((0,0,255))  #填充画布颜色
#在窗口中显示画布
window.blit(bg,(0,0))
pygame.display.update()     #更新窗口
#侦测并关闭绘图窗口
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

#%%
#创建绘图窗口，并且绘制图形
import pygame
pygame.init()
screen = pygame.display.set_mode((640,320))
pygame.display.set_caption("基本框架")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
#绘制图形
pygame.draw.rect(background,(255,50,50),[10,10,50,50],2)            #矩形
pygame.draw.circle(background,(50,50,255),(100,100),50,0)           #圆形
pygame.draw.ellipse(background,(50,255,50),[200,200,100,50],5)      #椭圆
pygame.draw.arc(background,(0,0,100),[300,150,80,50],1.2,3.14,3)    #弧度
pygame.draw.line(background,(100,100,100),(0,320),(600,20),2)       #直线
points=[(50,50),(60,70),(70,50),(70,30),(10,20)]
pygame.draw.polygon(background,(0,0,0),points,0)                    #多边形
#展示背景
screen.blit(background,(0,0))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

#%%
#绘制人脸
import pygame
pygame.init()

win=pygame.display.set_mode((300,300))
pygame.display.set_caption("绘制人脸")
bg=pygame.Surface(win.get_size())
bg=bg.convert()
bg.fill((255,255,255))
pygame.draw.circle(bg,(0,0,0),(150,150),135,2)
pygame.draw.circle(bg,(150,100,100),(90,105),25,0)
pygame.draw.circle(bg,(150,100,100),(210,105),25,0)
pygame.draw.ellipse(bg,(0,0,120),[140,130,20,60],0)
pygame.draw.arc(bg,(150,50,50),[90,169,120,80],3.4,6.1,8)
win.blit(bg,(0,0))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

#%%
#加载图片
import pygame
pygame.init()

win = pygame.display.set_mode((640,320))
pygame.display.set_caption("加载图片")
bg = pygame.Surface(win.get_size())
bg = bg.convert()
bg.fill((0,255,255))
#加载图片
pic = pygame.image.load("images\\ccbsite2.jpg")
#图片剪裁
pic=pygame.transform.chop(pic,(0,0,200,200))
pic.convert()
#背景上放置图片
bg.blit(pic,(20,10))
#窗口上放背景
win.blit(bg,(0,0))
#更新窗口
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

#%%
#插入文本
import pygame
pygame.init()

win = pygame.display.set_mode((640,320))
pygame.display.set_caption("插入文本")
bg = pygame.Surface(win.get_size())
bg = bg.convert()
bg.fill((255,255,255))
#设置字体格式
font1 = pygame.font.SysFont("simhei",24)
text1 = font1.render("第一行测试：背景同色，设置平滑",True,(0,0,255),(255,255,255))
bg.blit(text1,(20,20))
text2 = font1.render("第二行测试：背景不同色，设置平滑",True,(0,0,255),(100,150,100))
bg.blit(text2,(20,50))
text3 = font1.render("第三行测试，背景无色，设置不平滑",False,(0,0,255))
bg.blit(text3,(20,80))
win.blit(bg,(0,0))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

#%%
#制作动画
import pygame
pygame.init()

win=pygame.display.set_mode((640,320))
pygame.display.set_caption("插入动画")
bg=pygame.Surface(win.get_size())
bg=bg.convert()
bg.fill((200,200,255))

#球背景区域
ballbg=pygame.Surface((30,30))
ballbg.fill((200,200,255))
pygame.draw.circle(ballbg,(0,0,255),(15,15),15,0)
rect1 = ballbg.get_rect()
rect1.center=(200,100)
x,y=rect1.topleft
dx=3

#创建时间组建
clock = pygame.time.Clock()
#win.blit(bg,(0,0))
#win.blit(ballbg,rect1.topleft)
#pygame.display.update()

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #上背景
    win.blit(bg,(0,0))
    #设置位置并上球
    x+=dx
    rect1.center=(x,y)
    win.blit(ballbg,rect1.topleft)
    #更新窗口
    pygame.display.update()

pygame.quit()

#%%
#制作会自动反弹的小球
import pygame,random
import numpy as np
pygame.init()
#窗口
win=pygame.display.set_mode((640,480))
pygame.display.set_caption("弹球")
#背景
bg=pygame.Surface(win.get_size())
bg=bg.convert()
bg.fill((255,255,255))
#球
ball=pygame.Surface([30,30])
ball.fill((255,255,255))
pygame.draw.circle(ball,(50,50,255),(15,15),15,0)
#创建起始角度
angle = random.randint(20,90)
orc = np.math.radians(angle)
dx = 5*np.math.cos(orc)
dy = -5*np.math.sin(orc)
#获取球位置信息
rect1 = ball.get_rect()
x,y=(200,100)
#设置时间组件
clock=pygame.time.Clock()
#设置点击事件
running=True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.blit(bg,(0,0))
    x+=dx
    y+=dy
    rect1.center=(x,y)
    if rect1.left<0:
        rect1.left=0
        dx*=-1
    elif rect1.right>bg.get_width():
        rect1.right=bg.get_width()
        dx*=-1
    elif rect1.top<0:
        rect1.top=0
        dy*=-1
    elif rect1.bottom>bg.get_height():
        rect1.bottom=bg.get_height()
        dy*=-1
    win.blit(ball,rect1.topleft)
#    print(rect1.topleft)
    pygame.display.update()
pygame.quit()

#%%
#面向对象
import pygame,random,math

#创建类
class Ball(pygame.sprite.Sprite):
    #设置属性
    x=0
    y=0
    dx=0
    dy=0
    #设置动作
    def __init__(self, speed, sx, sy, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = sx
        self.y = sy
        self.image = pygame.Surface([radium*2,radium*2])        #设置球背景
        self.image.fill((255,255,255))      #背景设为白色
        pygame.draw.circle(self.image,color,(radium,radium),radium,0)   #画实心圆
        self.rect = self.image.get_rect()       #获取球背景区域
        self.rect.center=(sx,sy)        #把初始位置作为球的中心
        angle=random.randint(20,70)     #设置角度
        orc=math.radians(angle)     #转化为弧度
        self.dx = speed*math.cos(orc)    #水平移动速度
        self.dy = -speed*math.sin(orc)   #垂直移动速度
    
    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        self.rect.center = (self.x,self.y)
        if self.rect.left<0:
            self.rect.left=0
            self.dx*=-1
        elif self.rect.right>bg.get_width():
            self.rect.right=bg.get_width()
            self.dx*=-1
        elif self.rect.top<0:
            self.rect.top=0
            self.dy*=-1
        elif self.rect.bottom>bg.get_height():
            self.rect.bottom=bg.get_height()
            self.dy*=-1
        
        
pygame.init()
#窗口
win=pygame.display.set_mode((640,480))
pygame.display.set_caption("弹球-对象")
#背景
bg=pygame.Surface(win.get_size())
bg=bg.convert()
bg.fill((255,255,255))
#创建角色组
allsprite = pygame.sprite.Group()
blueball = Ball(6,20,20,15,(0,0,255))
allsprite.add(blueball)
redball = Ball(10,250,250,15,(255,0,0))
allsprite.add(redball)
#设置时间组件
clock=pygame.time.Clock()
#设置点击事件
running=True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.blit(bg,(0,0))
    blueball.update()
    redball.update()
    #绘制角色组到画布中
    allsprite.draw(win)
    pygame.display.update()
pygame.quit()
    












