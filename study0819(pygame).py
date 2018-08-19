# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 21:32:24 2018

@author: ecupl
"""
import os
os.chdir("D:\\mywork\\test")
from pygame import mixer
#对象初始化
mixer.init()
#创建对象
sound1 = mixer.Sound("sounds\\Pic39.wav")
#播放音乐
sound1.play(loops=2)
#设置音量
sound1.set_volume(1)
#获取当前音量
sound1.get_volume()
sound1.set_volume(0.5)
sound1.get_volume()
#停止播放
sound1.stop()



#%%
#简易音效播放
#定义菜单
def menu(status):
    os.system('cls')
    print('wav 音效播放器 {}'.format(status))
    print('----------------------------')
    print(' 1. 播  放')
    print(' 2. 上一首')
    print(' 3. 下一首')
    print(' 9. 停止播放')
    print(' 0. 结束程序')
    print('----------------------------')

#定义播放音效
def playsounds():
    global sound, status, songname
    sound = mixer.Sound(wavfiles[index])
    sound.play(loops=0)
    pathname,songname = os.path.split(wavfiles[index])
    status = '正在播放{}'.format(songname)
    
    

import os, glob, time
from pygame import mixer
os.chdir("D:\\mywork\\test") 
mixer.init()

#读取本地音效资源
sound_dir = 'sounds/'
wavfiles = glob.glob(sound_dir+'*.wav')
index = 0
#sound = mixer.Sound(wavfiles[index])
status = ''
#sound.play()

while True:
    menu(status)
    choice = int(input("请输入您的选择："))
    if choice==1:
        playsounds()
    elif choice==2:
        index+=1
        if index==len(wavfiles):
            index=0
        sound.stop()
        playsounds()
    elif choice==3:
        index-=1
        if index==-1:
            index=len(wavfiles)-1
        sound.stop()
        playsounds()
    elif choice==9:
        sound.stop()
        status='暂停{}'.format(songname)
    else:
        break
sound.stop()
print('程序执行完毕')




