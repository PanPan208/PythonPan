# @time: 2021/12/27 5:36 PM
# Author: pan
# @File: foo.py
# @Software: PyCharm

print("我是模块foo")

# 控制使用 * 导入模块可以导入的名称
# __all__ = ['x']


x = 1000

print(f"foo内部的x的地址{id(x)}")

def get():
    print(f"x is {x}")
    return x


def change_x():
    global x
    x = 666
