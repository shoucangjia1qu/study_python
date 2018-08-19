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
sound1.play(loops=0)
#设置音量
sound1.set_volume(1)
#获取当前音量
sound1.get_volume()
sound1.set_volume(0.5)
sound1.get_volume()
#停止播放
sound1.stop()

    






