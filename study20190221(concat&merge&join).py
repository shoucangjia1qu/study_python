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

#选中需要的索引对应的行或者列
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

#%%
'''【merge用法】'''
'''(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, 
right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False)'''

#默认
pd.merge(df1,df2)           #只合并相同列，并做点乘，相当于sql中的"inner join"
'''data1 lkey rkey
0     2    b    c
1     2    b    a
2     2    c    c
3     2    c    a
4     3    a    e
5     4    d    d'''

pd.merge(df1,df2,how='left')    #左连接，以左边为主轴
'''data1 lkey rkey
0     1    a  NaN
1     2    b    c
2     2    b    a
3     3    a    e
4     6    b  NaN
5     2    c    c
6     2    c    a
7     4    d    d'''

pd.merge(df1,df2,how='right')    #右连接，以右边为主轴
'''data1 lkey rkey
0    2.0    b    c
1    2.0    c    c
2    2.0    b    a
3    2.0    c    a
4    3.0    a    e
5    4.0    d    d
6    5.0  NaN    b'''

pd.merge(df2,df1,how='left')
'''data1 rkey lkey
0     2    c    b
1     2    c    c
2     3    e    a
3     4    d    d
4     5    b  NaN
5     2    a    b
6     2    a    c'''

pd.merge(df1,df2,how='outer')   #外连接，全部保留
'''data1 lkey rkey
0    1.0    a  NaN
1    2.0    b    c
2    2.0    b    a
3    2.0    c    c
4    2.0    c    a
5    3.0    a    e
6    6.0    b  NaN
7    4.0    d    d
8    5.0  NaN    b'''

pd.merge(df1,df2,on='data1')    #可以指定合并的列

#没有相同列的情况
df2.columns=['data2','rkey']
pd.merge(df1,df2,how='left',left_on='data1',right_on='data2')
'''data1 lkey data2 rkey
0     1    a   NaN  NaN
1     2    b     2    c
2     2    b     2    a
3     3    a     3    e
4     6    b   NaN  NaN
5     2    c     2    c
6     2    c     2    a
7     4    d     4    d'''

#指定多个相同列的合并
pd.merge(df1,df2,how='left',left_on=['data1','lkey'],right_on=['data2','rkey'])
'''data1 lkey data2 rkey
0     1    a   NaN  NaN
1     2    b   NaN  NaN
2     3    a   NaN  NaN
3     6    b   NaN  NaN
4     2    c     2    c
5     4    d     4    d'''

#suffixes用法
df2.columns=['data2','lkey']        #指定一个字段合并，其余的用suffixes进行区分
pd.merge(df1,df2,how='left',left_on='data1',right_on='data2',suffixes=('123','456'))
'''data1 lkey123 data2 lkey456
0     1       a   NaN     NaN
1     2       b     2       c
2     2       b     2       a
3     3       a     3       e
4     6       b   NaN     NaN
5     2       c     2       c
6     2       c     2       a
7     4       d     4       d'''

#sort用法
pd.merge(df1,df2,how='left',left_on='data1',right_on='data2',suffixes=('123','456'),sort=True)
'''data1 lkey123 data2 lkey456
0     1       a   NaN     NaN
1     2       b     2       c
2     2       b     2       a
3     2       c     2       c
4     2       c     2       a
5     3       a     3       e
6     4       d     4       d
7     6       b   NaN     NaN'''

#根据index索引进行合并
pd.merge(df1,df2,how='left',left_index=True,right_index=True)
'''data1 lkey_x data2 lkey_y
0     1      a   NaN    NaN
1     2      b     2      c
2     3      a     3      e
3     6      b     4      d
4     2      c     5      b
5     4      d     2      a'''

#indicator用法，多一列标识出这组数据的合并情况
pd.merge(df1,df2,how='outer',left_on='data1',right_on='data2',indicator=True)
'''data1 lkey_x data2 lkey_y      _merge
0     1      a   NaN    NaN   left_only
1     2      b     2      c        both
2     2      b     2      a        both
3     2      c     2      c        both
4     2      c     2      a        both
5     3      a     3      e        both
6     6      b   NaN    NaN   left_only
7     4      d     4      d        both
8   NaN    NaN     5      b  right_only'''

#相同两个字段，相当于设置多个列合并
df2.columns=['data1','lkey']        #指定一个字段合并，其余的用suffixes进行区分
pd.merge(df1,df2,how='outer')
'''data1 lkey
0    1.0    a
1    2.0    b
2    3.0    a
3    6.0    b
4    2.0    c
5    4.0    d
6    3.0    e
7    5.0    b
8    2.0    a'''

#%%
'''【join用法】'''
'''(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)'''

#默认用法，不指定on，就是按照index索引来合并
df1.join(df2,lsuffix='_left', rsuffix='_right')
'''data1_left lkey_left data1_right lkey_right
0          1         a         NaN        NaN
1          2         b           2          c
2          3         a           3          e
3          6         b           4          d
4          2         c           5          b
5          4         d           2          a'''

#on指定左表中的列为新的索引，以和右表的索引合并
df2.columns=['data2','lkey']
df1.join(df2,on='data1',how='outer',lsuffix='_left', rsuffix='_right')
'''data1 lkey_left data2 lkey_right
0    1.0         a     2          c
1    2.0         b     3          e
4    2.0         c     3          e
2    3.0         a     4          d
3    6.0         b   NaN        NaN
5    4.0         d     5          b
5    5.0       NaN     2          a'''

df1.join(df2,on='data1',how='outer',lsuffix='_left', rsuffix='_right',sort=True)    #按照data1拍寻
'''data1 lkey_left data2 lkey_right
0    1.0         a     2          c
1    2.0         b     3          e
4    2.0         c     3          e
2    3.0         a     4          d
5    4.0         d     5          b
5    5.0       NaN     2          a
3    6.0         b   NaN        NaN'''

#对比
df1.set_index('data1',inplace=True)
df1.join(df2,how='outer',lsuffix='_left', rsuffix='_right',sort=True)
'''lkey_left data2 lkey_right
1         a     2          c
2         b     3          e
2         c     3          e
3         a     4          d
4         d     5          b
5       NaN     2          a
6         b   NaN        NaN'''

#重置index
df1.reset_index(drop=False,inplace=True)


