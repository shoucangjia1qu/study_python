# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:34:18 2019

@author: ecupl
"""

import numpy as np
import pandas as pd

'''lambda表达式'''
func1=lambda x :x**2
'''普通函数定义'''
def func2(x):
    return x*2
def func3(x,n):
    return x*n*2



df = pd.DataFrame(np.linspace(1,20,20).reshape(4,-1))

'''apply+lambda表达式'''
df.apply(func1)
df.apply(lambda x:x[0]+x[1], axis=1)         #跨列计算，也就是按行来
df.apply(lambda x,n : x[:2]*n, axis=1, args=((3,)))         #多个变量，可用args放置多余参数

'''apply+函数'''
df.apply(func2)
df.apply(func3, axis=1, args=((5,)))

