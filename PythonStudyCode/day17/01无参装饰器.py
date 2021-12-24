# @time: 2021/12/20 11:27 AM
# Author: pan
# @File: 01无参装饰器.py
# @Software: PyCharm

"""
储备知识：
1、*args **kwargs的使用
2、名称空间与作用域
3、函数对象、函数嵌套、闭包函数

装饰器：
器：指的是工具，可以定义为函数等其他
装饰：为其他事物添加额外的点缀东西
装饰器：为其他函数添加额外的功能

为什么要使用装饰器？
装饰器可以在不修改源代码以及改变调用方式的前提下为被装饰对象添加新功能

如何用？
需求：在不修改index函数源代码的基础上 以及不修改调用方式的基础上
为index函数添加统计函数运行时间的功能。
"""

import time


# def index(x, y):
#     time.sleep(3)
#     print("index is {}, {}".format(x, y))


# 方案1： 失败
# 没有对调用方式进行修改，但是对源函数代码进行了修改
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print("index is {}, {}".format(x, y))
#     end = time.time()
#     print(end-start)
# index(10, 20)

# 方案二： 失败
# 没有对源函数进行修改  但是对调用方式进行修改了
# 如果调用的地方很多 要在很多地方添加代码  代码冗余
# def index(x, y):
#     time.sleep(3)
#     print("index is {}, {}".format(x, y))
#
# start = time.time()
# index(10, 20)
# end = time.time()
# print(end - start)


# 方案三： 失败
# 调用方式改变了  源函数没有进行修改
# def index(x, y):
#     time.sleep(1)
#     print("index is {}, {}".format(x, y))
#
#
# def wrapper(x, y):
#     start = time.time()
#     index(x, y)
#     end = time.time()
#     print(end - start)
#
# wrapper(10, 20)


# 方案三： 改版1  将参数写活
# *args **kwargs 的使用
# wrapper传入什么参数 index就会传入什么样的参数
# 这样index需要什么样的参数，wrapper就传入什么样的参数即可
# def index(x, y):
#     time.sleep(1)
#     print("index is {}, {}".format(x, y))
#
#
# def wrapper(*args, **kwargs):
#     start = time.time()
#     index(*args, **kwargs)
#     end = time.time()
#     print(end - start)
#
# wrapper(10, 20)


# 方案三： 改版2  将函数名也写活
# 上一个版本中wrapper中调用的函数只是index，想要wrapper函数可以对应任何函数 需要将函数写活
# def index(x, y):
#     time.sleep(1)
#     print("index is {}, {}".format(x, y))
#
# def home():
#     time.sleep(2)
#     print("welcome home")
#
# def outter(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#     return wrapper
#
# index = outter(index)
# index(10, 20)
#
# home = outter(home)
# home()


# 方案三： 改版3 将返回值也写活
# 即：func函数的是什么参数 wrapper也返回什么样的参数
# def index(x, y):
#     time.sleep(1)
#     print("index is {}, {}".format(x, y))
#     return 100
#
# def home():
#     time.sleep(2)
#     print("welcome home")
#
# def outter(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return res
#     return wrapper
#
#  # 偷梁换柱
# index = outter(index)
# res = index(10, 20)
# print(res)
#
# home = outter(home)
# res = home()
# print(res)


# 方案三： 终极版本  语法糖简化代码
# 添加wraps会将一些 方法自带的属性也进行修改
# 相当于给wrapper又添加了一个装饰器
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """新增了统计函数运行时间的方法"""
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        # 手动将index的属性设置为wrapper的属性
        # 应该在调用函数之前添加 不用是在调用函数之后添加
        # 因为调用函数的属性不需要调用函数 只需要知道函数地址即可
        # wrapper.__name__ = index.__name__
        # wrapper.__doc__ = index.__doc__
        return res
    return wrapper


# @语法糖
# 在被修饰函数的上方单独一行  @装饰器的名字
# @timer 等价于 index = timer(index)
@timer
def index(x, y):
    """index源函数"""
    time.sleep(1)
    print("index is {}, {}".format(x, y))
    return 100


res = index(10, 20)
print(res)
print(index)
print(type(index))
print(index.__doc__)
print(index.__name__)


# 不加 @wraps(func)  索引到time下的wrapper方法
# <function timer.<locals>.wrapper at 0x102e33940>
# <class 'function'>
# 新增了统计函数运行时间的方法
# wrapper

# 加 @wraps(func)  索引到index方法
# <function index at 0x10f00f940>
# <class 'function'>
# index源函数
# index


@timer
def home():
    print("welcome home")
home()


"""
总结：
装饰器的使用
def ouuter(func):
    def wrapper(*args, **kwargs):
        # 1 源函数的调用
        # 2 源函数的扩展
        res = func(*args, **kwargs)
        # 3 返回源函数的参数
        return res
    # 4 返回wrapper
    return wrapper
"""
