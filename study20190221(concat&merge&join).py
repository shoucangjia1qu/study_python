# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:02:48 2018

@author: ecupl
"""

import numpy as np
import pandas as pd
import os

os.chdir(r"D:\mywork\test")

df1 = pd.DataFrame([[1,2,3,6,2,4],['a','b','a','b','c','d']])
df1=df1.T
df1.columns = ['data1','lkey']
print(df1)
'''
    data1 lkey
0     1    a
1     2    b
2     3    a
3     6    b
4     2    c
5     4    d
'''

df2 = pd.DataFrame([[2,3,4,5,2],['c','e','d','b','a']])
df2=df2.T
df2.columns = ['data2','rkey']
print(df2)
'''
    data2 rkey
0     2    c
1     3    e
2     4    d
3     5    b
4     2    a
'''

#%%
'''【concat用法】'''
'''(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, 
levels=None, names=None, verify_integrity=False, copy=True)'''

pd.concat([df1,df2])        #默认状态(跨行合并，外连接，且没有相同列)
'''
   data1 data2 lkey rkey
0     1   NaN    a  NaN
1     2   NaN    b  NaN
2     3   NaN    a  NaN
3     6   NaN    b  NaN
4     2   NaN    c  NaN
5     4   NaN    d  NaN
0   NaN     2  NaN    c
1   NaN     3  NaN    e
2   NaN     4  NaN    d
3   NaN     5  NaN    b
4   NaN     2  NaN    a
'''
pd.concat([df1,df2],join='inner')        #改成内连接，为空

df2.columns = ['data1','rkey']
pd.concat([df1,df2])
'''
   data1 lkey rkey
0     1    a  NaN
1     2    b  NaN
2     3    a  NaN
3     6    b  NaN
4     2    c  NaN
5     4    d  NaN
0     2  NaN    c
1     3  NaN    e
2     4  NaN    d
3     5  NaN    b
4     2  NaN    a
'''
pd.concat([df1,df2],join='inner')
'''
    data1
0     1
1     2
2     3
3     6
4     2
5     4
0     2
1     3
2     4
3     5
4     2
'''

pd.concat([df1,df2],axis=1)
'''
data1 lkey data1 rkey
0     1    a     2    c
1     2    b     3    e
2     3    a     4    d
3     6    b     5    b
4     2    c     2    a
5     4    d   NaN  NaN
'''
pd.concat([df1,df2],axis=1,join='inner')
'''
data1 lkey data1 rkey
0     1    a     2    c
1     2    b     3    e
2     3    a     4    d
3     6    b     5    b
4     2    c     2    a
'''

#当有多个字段相同时
df2.columns = ['data1','lkey']
pd.concat([df1,df2])
'''
data1 lkey
0     1    a
1     2    b
2     3    a
3     6    b
4     2    c
5     4    d
0     2    c
1     3    e
2     4    d
3     5    b
4     2    a
'''
pd.concat([df1,df2],axis=1,on='data1')      #按原顺序合并

a=pd.concat([df1,df2],axis=1,keys=['s1','s2'])      #加了keys，相当于改变了index和columns
'''
data1 lkey data1 rkey
0     1    a     2    c
1     2    b     3    e
2     3    a     4    d
3     6    b     5    b
4     2    c     2    a
'''

a=pd.concat([df1,df2],axis=1,keys=['s1','s2'],names=['hang','lie'])      #加了names，相当于给行和列取了名字
print(a)
'''
hang    s1         s2     
lie  data1 lkey data1 rkey
0        1    a     2    c
1        2    b     3    e
2        3    a     4    d
3        6    b     5    b
4        2    c     2    a
5        4    d   NaN  NaN
'''

df2.columns = ['data1','rkey']
df2.index = [1,2,3,4,5]
pd.concat([df1,df2],axis=1,join='outer')

#选中需要的行或者列
pd.concat([df1,df2],axis=1,join='outer',join_axes=[pd.Series([1,2,3])])
'''
data1 lkey data1 rkey
1     2    b     2    c
2     3    a     3    e
3     6    b     4    d
'''
pd.concat([df1,df2],axis=0,join='outer',join_axes=[pd.Series(['lkey','data1'])])
'''
lkey data1
0    a     1
1    b     2
2    a     3
3    b     6
4    c     2
5    d     4
1  NaN     2
2  NaN     3
3  NaN     4
4  NaN     5
5  NaN     2
'''









