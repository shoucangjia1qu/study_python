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
'''2、datetime.date模块'''
from datetime import date
#2-1 date类方法和属性
date.max                #datetime格式的最大时间
'''datetime.date(9999, 12, 31)'''
date.min                #datetime格式的最小时间
'''datetime.date(1, 1, 1)'''
date.resolution         #datetime格式表示日期的最小单位
'''datetime.timedelta(1)'''
date.today()            #显示当天的日期
'''datetime.date(2019, 2, 20)'''
date.fromtimestamp(time.time()+24*3600)         #获取时间戳对应的datetime格式日期，输入时间戳
'''datetime.date(2019, 2, 21)'''

#2-2 datetime对象方法和属性
c = date(2019,2,19)            #datetime格式时间
c.year, c.month, c.day         #datetime格式的年，月，日
'''(2019, 2, 19)'''
c.replace(2020), c.replace(2020,1), c.replace(2020,1,20)     #datetime格式的替换
'''(datetime.date(2020, 2, 19),
 datetime.date(2020, 1, 19),
 datetime.date(2020, 1, 20))'''
c.timetuple()                   #datetime格式转换为struct_time格式
'''time.struct_time(tm_year=2019, tm_mon=2, tm_mday=19, tm_hour=0, 
                    tm_min=0, tm_sec=0, tm_wday=1, tm_yday=50, tm_isdst=-1)'''
c.toordinal()                   #从0001-01-01开始起的天数
'''737109'''
c.isocalendar()                 #datetime格式的年，周，星期几（isoweekday）
'''(2019, 8, 2)'''
c.isoweekday()                  #返回星期几，取值[1,7]，1表示星期一
'''2'''
c.weekday()                     #返回星期几，取值[0,6]，0表示星期一
'''1'''
c.isoformat()                   #datetime格式转为"YYYY-MM-DD"的格式
'''2019-02-19'''
c.ctime()                       #转为time标准字符串格式的日期
''''Tue Feb 19 00:00:00 2019''''
c.strftime('%d%b%Y')            #转为指定格式的字符串日期，此处为"%d%b%Y"格式
'''19Feb2019'''

#%%
'''3、datetime.time模块'''
from datetime import time
#3-1 time类方法和属性
time.max                        #time类能表示的最大时间
'''datetime.time(23, 59, 59, 999999)'''
time.min                        #time类能表示的最小时间
'''atetime.time(0, 0)'''
time.resolution                 #time类的最小单位
'''datetime.timedelta(0, 0, 1)'''

#3-2 time对象方法和属性
d=time(20,50,30,600)            #生成一个time对象
print(d)
'''20:50:30.000600'''
print(d.hour,d.minute,d.second,d.microsecond)           #time格式的时，分，秒，微妙
'''20 50 30 600'''
d.tzinfo                        #不懂
d.replace(21,51,31,999)         #time替换
d.isoformat()                   #time格式转为"HH:MM.SS%f"的格式
'''20:50:30.000600'''
d.strftime('%H-%M-%S-%f')       #time格式转为指定字符串格式，此处为"%H-%M-%S-%f"
'''20-50-30-000600'''
d.strftime('%H:%M:%S.%f')
'''20:50:30.000600'''

#%%
'''4、datetime.datetime模块'''
from datetime import datetime,timezone
#4-1 datetime类方法和属性
t1 = datetime.today()           #返回当前时间，（年，月，日，时，分，秒，微秒）
'''datetime.datetime(2019, 2, 20, 22, 18, 52, 846652)'''
t2 = datetime.now(timezone.utc)             #返回指定时区的时间，不指定参数就返回当前时间
'''datetime.datetime(2019, 2, 20, 14, 25, 37, 191126, tzinfo=datetime.timezone.utc)'''
t3 = datetime.utcnow()          #返回UTC时间
'''datetime.datetime(2019, 2, 20, 14, 23, 24, 743756)'''
t4 = datetime.fromtimestamp(time.time()+24*3600)         #时间戳转换为datetime格式，需输入时间戳
'''datetime.datetime(2019, 2, 21, 22, 27, 47, 720952)'''
t5 = datetime.utcfromtimestamp(time.time()+48*3600)      #时间戳转换为UTC的datetime格式，需输入时间戳
'''datetime.datetime(2019, 2, 22, 14, 30, 42, 281178)'''
import datetime
da = datetime.date(2019,2,19) 
ti = datetime.time(22,35,20,900)
datetime.datetime.combine(da,ti)          #将date和time合并起来
'''datetime.datetime(2019, 2, 19, 22, 35, 20, 900)'''
from datetime import datetime,timezone
t6 = datetime.strptime('2018/12/31 12:00:01','%Y/%m/%d %H:%M:%S')       #字符串转换为datetime格式
'''datetime.datetime(2018, 12, 31, 12, 0, 1)'''

#4-2 datetime对象的方法和属性
dt = datetime.today()           #生成一个datetime对象
dt = datetime(2019,2,20,23,9,50,680416)
'''datetime.datetime(2019, 2, 20, 23, 9, 50, 680416)'''
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
'''2019 2 20 23 9 50 680416'''
dt.tzinfo           #datetime对象的时区信息
dt.timestamp()          #datetime格式转换为时间戳
'''1550675390.680416'''
da = dt.date()          #获取date对象
ti = dt.time()          #获取time对象，tzinfo为None
ti2 = dt.timetz()       #获取time对象，tzinfo与datetime对象的tzinfo相同
'''datetime.time(23, 9, 50, 680416)'''
dt.timetuple()          #datetime格式转换为struct_time格式
'''time.struct_time(tm_year=2019, tm_mon=2, tm_mday=20, tm_hour=23, 
                    tm_min=9, tm_sec=50, tm_wday=2, tm_yday=51, tm_isdst=-1)'''
dt.utctimetuple()
dt.isocalendar()            #年，周，星期几
'''(2019, 8, 3)'''
dt.isoweekday()             #星期几,[1,7]
'''3'''
dt.weekday()                #星期几,[0,6]
'''2'''
dt.toordinal()              #0001-01-01距今的天数
'''737110'''
dt.ctime()                  #转为time.time对象的标准字符串格式
''''Wed Feb 20 23:23:58 2019''''
dt.isoformat()              #转为标准格式的字符串，可自行在date对象和time对象间加入分隔符
'''2019-02-20T23:23:58.112611'''
dt.isoformat('/')
'''2019-02-20/23:23:58.112611'''
dt.isoformat('-')
'''2019-02-20-23:23:58.112611'''
dt.strftime('%d%b%Y')       #datetime对象转为指定字符串格式
'''20Feb2019'''

#%%
'''5、datetime.timedelta'模块'''
from datetime import timedelta
#5-1 timedelta类方法和属性
timedelta.max               #内部值储存为天、秒、微妙，输入的任何参数都可转换为这几个值
'''datetime.timedelta(999999999, 86399, 999999)'''
timedelta.min
'''datetime.timedelta(-999999999)'''
timedelta.resolution
'''datetime.timedelta(0, 0, 1)'''

#5-2 timedelta对象方法和属性
deltax = timedelta(360)         #建立一个时差timedelta类
deltax.days
'''360'''
deltax = timedelta(hours=3)
deltax.seconds
'''10800'''
deltax = timedelta(days=10,hours=5,minutes=30)
print(deltax.days, deltax.seconds, deltax.microseconds)
'''10 19800 0'''
deltax.total_seconds()          #计算时差的总秒数
'''883800'''

#5-3 与datetime格式相加减
print(dt)
'''2019-02-20 23:23:58.112611'''
newdt = dt+deltax
print(newdt)
'''2019-03-03 04:53:58.112611'''
print(dt+timedelta(hours=-3))
'''2019-02-20 20:23:58.112611'''


