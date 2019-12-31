# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:21:00 2019

@author: ecupl
"""

#生成器

g = (x*x for x in range(10))
#next(g)
for n in g:
    print(n)



def myYield(n):
    while n>0:
        print("开始生成。。。")
        yield n
        print("完成一次。。。")
        n -= 1

if __name__ == "__main__":
    a = myYield(3)
    a.__next__()
    a.__next__()


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return "well done"

f = fib(5)
print(f)
print(list(f))

f = fib(5)
print(f.__next__())
print(f.__next__())
print("something else")
print(f.__next__())
print(f.__next__())
print(f.__next__())



def iter_st(x):
    for xi in range(x):
        yield xi
  
re = iter_st(10)
for t in re:
    print(t)

#杨辉三角
def triangles():
    result = [1]
    while True:
        yield result
        result = [1] + [result[i] + result[i+1] for i in range(len(result)-1)] + [1]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break
results

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)  
o = odd()
next(o)
next(o)
next(o)
next(o)






#修饰器
def makebold(fn):  
    def wrapped():  
        return "<b>" + fn() + "</b>"  
    return wrapped  
   
def makeitalic(fn):  
    def wrapped():  
        return "<i>" + fn() + "</i>"  
    return wrapped

@makebold  
@makeitalic  
def hello():  
    return "hello world"  

hello()


#案例1
import time

def foo():
    print("in foo()")
    
def timeit(func):
    start = time.clock()
    func()
    end = time.clock()
    print("Time Elapsed:",end-start)

timeit(foo)

#案例1：另一种写法
import time  
   
def foo():  
    print('in foo()')
   
def timeit(func):
    def wrapper1():
        start = time.clock()
        func()
        end =time.clock()
        print('Time Elapsed:', end - start)
    return wrapper1

foo = timeit(foo)   #可以直接写成@timeit + foo定义，python的"语法糖"
foo()

#或者写成@形式
@timeit
def foo1():  
    print('in foo()')

foo1()

#有趣的汉堡了解顺序
def bread(func):
    def wrapper():
        print("</'''  '''\>")
        func()
        print("<\_______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food="--ham--"):
    print(food)

#1
sandwich()

#2
sandwich2 = bread(ingredients(sandwich))
sandwich2()

#3
@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)

sandwich()


#对有参函数进行修饰
##一个参数：如果原函数有参数，那闭包函数必须保持参数个数一致，并且将参数传递给原方法
def w1(func):
    def wrapper(name):
        print("this is wrapper head")
        func(name)
        print("this is wrapper tail")
    return wrapper

@w1
def hello(name):
    print("hello, "+name)

hello("AoDaCat")

##多个参数：
def w2(func):
    def wrapper(*args, **kwargs):
        print("this is wrapper head")
        func(*args, **kwargs)
        print("this is wrapper tail")
    return wrapper

@w2
def hello(name1, name2, name3):
    print("hello, "+name1+" and "+name2+" and "+name2)

hello("AoDaCat", "aodadou", "xiaotudou")


#有返回值的函数
def w3(func):
    def wrapper(name):
        print("this is wrapper head")
        hello = func(name)
        print("this is wrapper tail")
        return hello                    #要把值传回去
    return wrapper

@w3
def hello(name):
    print("hello, "+name)
    return "I am fine!"

hello("AoDaCat")


#有参数的修饰器
def func_args(pre="xiaoqiang"):
    def w4(func):
        def inner(name):
            print("日志记录人：", pre)
            hello = func(name)
            return hello
        return inner
    return w4

@func_args()
def hello(name):
    print("hello, "+name)
    return "I am fine!"

hello("AoDaCat")


@func_args('wangcai')
def hello(name):
    print("hello, "+name)
    return "I am fine!"

hello("AoDaCat")


#通用修饰器
def w_test(func):
    def wrapper(*args, **kwargs):
        ret1 = func(*args, **kwargs)
        return ret1
    return wrapper

#1
@w_test
def test():
    print('test1')

test()

#2
@w_test
def test():
    print("test2")
    return "Python"

test()

#3
@w_test
def test(a):
    print("test+"+a)
    return ("hello, "+a)

test("AoDaCat")



#类修饰器
class Test(object):
    def __call__(self, *args, **kwargs):
        print('call called')


t = Test()
print(t())


#直接对类进行修饰
class Test(object):
    def __init__(self, func):
        print('test init')
        print('func name is %s ' % func.__name__)
        self.abc = func

    def __call__(self, *args, **kwargs):
        print('this is wrapper')
        print(*args[0])
        self.abc()


@Test
def test():
    print('this is test func')

test('a')


######测试程序运行时长
import time, functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.clock()
            print("%s call %s()"%(text, func.__name__))
            ret = func(*args, **kwargs)
            end = time.clock()
            print("函数运行时长：%fs"%(end-start))
            return ret
        return wrapper
    return decorator

@log("execute")
def now():
    print("2019-12-31")


now()
now.__name__




