# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:24:54 2019

@author: ecupl
"""

import numpy as np
import pandas as pd
import os

os.chdir(r"D:\mywork\test")

######定制类######
#1、__str__和__repr__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)'%self.name
    __repr__ = __str__
    '''
    __str__可以改变打印出来的实例的文字
    __repr__可以改变直接显示实例的文字
    '''
    
print(Student('Bob'))
Student('Bob')

#2、__iter__和__next__可实现类循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
        self.li = []
    
    def __iter__(self):
        print('开始，只调用一次')
        return self
    
    def __next__(self):
        print('for循环不断迭代')
        self.a, self.b = self.b, self.a+self.b
        self.li.append(self.a)
        if self.a > 100000:
            raise StopIteration()
        return self.a

f = Fib()
for n in f:
    print(n)
f.li

#3、__getitem__可实现对类的切片
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
        self.li = []
    
    def __iter__(self):
        print('开始，只调用一次')
        return self
    
    def __next__(self):
        print('for循环不断迭代')
        self.a, self.b = self.b, self.a+self.b
        self.li.append(self.a)
        if self.a > 100000:
            raise StopIteration()
        return self.a
    
    def __getitem__(self,n):
        return self.li[n]
    
f = Fib()
for i in f:
    print(i)
f[:10]


class Fib(object):
    def __getitem__(self,n):
        if isinstance(n, int):
            a, b = 1, 1
            for i in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b =1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib()
f[10]
f[1:11]
f[:11]

#4、__getattr__调用不存在的属性
class Student(object):
    def __init__(self):
        self.name = 'Bob'
    def __getattr__(self,attr):
        print(attr,'不存在')

s = Student()
s.name      #Bob
s.score     #score 不存在

#链式调用
class Chain(object):
    
    def __init__(self, path=''):
        self.__path = path
    
    def __getattr__(self, attr):
        return Chain('%s/%s'%(self.__path, attr))
    
    def __str__(self):
        return self.__path
    
    __repr__ = __str__
    
c=Chain()
c.st.list._Chain__path

#5、__call__定义实例自己的属性和方法
class Student(object):
    def __init__(self,name):
        self.name = name
    
    def __call__(self,n):
        if n==0:
            self.gender = 'male'
            print(self.gender)
        elif n==1:
            self.gender = 'female'
            print(self.gender)
        else:
            raise ValueError('value must be 0 or 1!')
        
s = Student('Bob')
s(0)
s.gender


#callable查看对象是否能被调用
callable(max)               #True
callable(Student('Bob'))    #True
callable(1)                 #False
callable('str')             #False
callable([1,2,3])           #False
callable(None)              #False

###########使用枚举类###########
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


#unique帮助检查没有重复值
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#test
from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1
Gender.Male
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
#测试
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过')
else:
    print('测试失败')

########使用元类
class Hello(object):
    def hello(self, name='world'):
        print('Hello,%s'%name)

from oop import Hello    #载入模块，相当于依次执行该模块的所有语句
h = Hello()
h.hello()           #Hello,world
print(type(Hello))  #<class 'type'>，类型是个type
print(type(h))      #<class 'oop.Hello'>，类型是oop.Hello

#通过type()函数创建新的类
#先定义函数
def fn(self, name='world2'):
    print('Hello, %s'%name)
#再通过type创建类
Hello2 = type('Hello',(object,),dict(hello=fn))
'''参数：
class的名称
需要继承的父类
方法与函数绑定
'''
#测试
h = Hello2()
h.hello()       #Hello, world2
print(type(Hello2))     #<class 'type'>
print(type(h))          #<class '__main__.Hello'>



















