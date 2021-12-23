# @time: 2021/12/16 2:30 PM
# Author: pan
# @File: 03闭包函数.py
# @Software: PyCharm

"""
大前提：
闭包函数 = 命名空间和作用域 + 函数嵌套 + 函数对象的综合应用

什么是闭包函数？：
闭： 包围 指函数是内嵌函数  （闭包函数定义在一个函数内部）
包：内部函数包含对外层函数作用域内名称的引用 （并且是非全局名称作用域）
"""


# 实例1
# def f1():
#     x = 100000
#     def f2():
#         print(x)
#
#     f2()
#
# x = 1
# def bar():
#     f1()
#
# def foo():
#     bar()
#
# foo()


# # 实例2
# def f1():
#     x = 100000
#     def f2():
#         print(x)
#     # 返回这个函数的对象 而不是返回这个函数的调用
#     return f2
#
# # 直接将函数f1的调用 赋值给f 也就是将f2的内存地址 赋值给f
# f = f1()
#
# # <function f1.<locals>.f2 at 0x1015a2a60>
# # f 是函数f1内部的f2函数的地址
# print(f)
# # 相当于直接调用 f2()
# f()
# f1()()


# 函数调用的两种方式：
# 1、直接定义一个函数 直接调用
# def func1(x):
#     print(x)
#
# func1(10)
# func1(20)
# func1(30)

# 2、使用闭包函数进行调用
def func1(x):
    def func2():
        print(x)
    return func2

f = func1(10)
f()

f = func1(20)
f()

f = func1(30)
f()


# 实例3
import requests

# 1111 可以直接定义到一个函数中进行调用
# res = requests.get("http://www.baidu.com")
# print(res.text)
# def request_get(url):
#     res = requests.get(url)
#     return len(res)
# baidu = request_get("http://www.baidu.com")

# 2222 使用闭包函数的方式
def outter(url):
    def inner():
        res = requests.get(url)
        print(res.text)
    return inner

baidu = outter("http://www.baidu.com")
baidu()

jianshu = outter("https://www.jianshu.com/u/85171c38b17d")
jianshu()

