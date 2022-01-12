# @time: 2021/12/23 4:13 PM
# Author: pan
# @File: 作业.py
# @Software: PyCharm


# 1、基于迭代器的方式，用while循环迭代取值字符串、列表、元组、字典、集合、文件对象
"""
my_str = "Hello"
str_iterator = my_str.__iter__()
while True:
    try:
        print(str_iterator.__next__())
    except StopIteration:
        break


# 迭代取值
def iter_obj(obj):
    obj_iterator = iter(obj)
    while True:
        try:
            print(next(obj_iterator))
        except StopIteration:
            break


# iter_obj("nihao")
# iter_obj([1, 2, 3, 4, 100])

"""


# 2、自定义迭代器实现range功能
"""
def my_range(start, end, step):
    while start < end:
        yield start
        start += step

  
for i in my_range(1, 20, 2):
    print(i)
"""



