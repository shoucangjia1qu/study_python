# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:02:48 2018

@author: ecupl
"""

import time
import datetime
import numpy as np
import pandas as pd
import os

os.chdir(r"D:\mywork\test")

'''【名词解释】
1、UTC time:格林尼治天文时间、世界标准时间。
2、epoch time:表示时间开始的起点，不同平台上这个时间点的值不太相同。
3、timestamp:时间戳，表示从1970年1月1日0时0分0秒开始到现在所经过的毫秒数。Python返回的时秒数。
'''
'''【常用时间表示形式】
1、时间戳
2、格式化的时间字符串
3、time.struct_time
4、datetime中的datetime类
'''
#%%
'''1、time模块'''
#1-1 获取时间戳
time.time()
'''1550586114.694915'''

#1-2 获取time.struct_time
time.gmtime()       #获取当前的UTC标准时间
time.gmtime(time.time()+24*3600)        #获取下一天的UTC标准时间，输入时间戳
'''time.struct_time(tm_year=2019, tm_mon=2, tm_mday=20, tm_hour=14, 
                    tm_min=22, tm_sec=10, tm_wday=2, tm_yday=51, tm_isdst=0)'''
time.localtime()    #获取当地的UTC时间
time.localtime(time.time()+24*3600)     #获取下一天的当地UTC时间，输入时间戳
'''time.struct_time(tm_year=2019, tm_mon=2, tm_mday=20, tm_hour=22, 
                    tm_min=22, tm_sec=10, tm_wday=2, tm_yday=51, tm_isdst=0)'''

#1-3 获取字符串格式时间
time.ctime()        #获取当前时间的字符串
'''Tue Feb 19 22:25:45 2019'''
time.ctime(time.time()+24*3600)         #获取下一天的当前时间的字符串，输入时间戳
'''Wed Feb 20 22:33:38 2019'''
time.asctime()      #获取当前时间的字符串
time.asctime(time.localtime())          #获取当前时间的字符串，输入struct_time类
'''Tue Feb 19 22:46:43 2019'''
t=(2019,2,19,22,46,45,1,0,0)
time.asctime(t)         #获取当前时间的字符串，输入9个元素的元组，和struct_time一致
'''Tue Feb 19 22:46:45 2019'''

#1-4 字符串转struct_time，格式要完全匹配
time.strptime(time.ctime())         #标准格式的字符串可直接转换为struct_time
time.strptime('Tue Feb 19 22:25:45 2019')
'''time.struct_time(tm_year=2019, tm_mon=2, tm_mday=19, tm_hour=22, 
                    tm_min=25, tm_sec=45, tm_wday=1, tm_yday=50, tm_isdst=-1)'''
time.strptime('2019-02-19 22:55:55','%Y-%m-%d %H:%M:%S')
'''time.struct_time(tm_year=2019, tm_mon=2, tm_mday=19, tm_hour=22, 
                    tm_min=55, tm_sec=55, tm_wday=1, tm_yday=50, tm_isdst=-1)'''
time.strptime('31DEC2018','%d%b%Y')
'''time.struct_time(tm_year=2018, tm_mon=12, tm_mday=31, tm_hour=0, 
                    tm_min=0, tm_sec=0, tm_wday=0, tm_yday=365, tm_isdst=-1)'''

#1-5 struct_time转换字符串
time.strftime('%Y-%b-%d %H',time.gmtime())      #输入struct_time格式转换
'''2019-Feb-19 15'''
t=(2019,2,19,22,46,45,1,0,0)
time.strftime('%d%b%Y',t)       #输入9个元素的元组，和struct_time一致
'''19Feb2019'''

#1-6 struct_time转换时间戳
time.mktime(time.localtime())       #输入struct_time格式转换
'''1550589397.0'''
t=(2019,2,19,22,46,45,1,0,0)
time.mktime(t)       #输入9个元素的元组，和struct_time一致
'''1550587605.0'''

#%%
'''datetime模块'''












'''calendar模块'''








