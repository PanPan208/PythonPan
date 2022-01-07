# @time: 2021/12/23 5:37 PM
# Author: pan
# @File: 04函数的递归调用.py
# @Software: PyCharm

"""
递归：
是函数嵌套调用的另一种方式
具体是：一个函数直接或间接的调用了其自身
"""

# 对于无限循环调用自身的函数 Python可以设置最多循环多少次
# [Previous line repeated 993 more times]
import sys
# 如果设置了10 那么递归调用最多调用10次
sys.setrecursionlimit(10)
print(sys.getrecursionlimit())
# 系统默认为1000次


# 直接调用其自身
def f1():
    print("是我是我还是我")
    f1()
f1()

# 间接调用的其自身
# def f1():
#     print("is me f1")
#     f2()
#
# def f2():
#     print("是我 f2")
#     f1()
# f1()


"""
一段代码循环执行的两种方式：
1、使用while、for循环
2、使用递归调用
"""

# 1、while、for循环 循环执行代码
# while True:
#     print("1111")
#     print("2222")
#     print(3333)


# 2、使用递归调用的方式
# def func():
#     print("1111")
#     print("2222")
#     print(3333)
#     func()
# func()


# 递归调用 不应该无限制的调用下去
# 要有中断循环调用的条件
n = 0
# while n < 10:
#     print(f"n = {n}")
#     n += 1

# def func(n):
#     if n >= 10:
#         return 10
#     print(f"n = {n}")
#     n += 1
#     func(n)
# func(n)


"""
def age(n):
    if n == 0:
        return 18
    
    return age(n - 1) + 10

res = age(5)
print(res)

age(5) = age(4) + 10
= age(3) + 10 + 10
= age(2) + 10 + 10 + 10
= age(1) + 10 + 30
= age(0) + 10 + 40
= 18 + 50 = 68
"""


# 实例： 打印下列列表中的数据
l = [1,2,[3,[4,[5,[6,[7,[8,[9,10,11,[12,[13,]]]]]]]]]]
def func(l):
    for line in l:
        # 如果元素还是一个列表 再次循环列表
        if type(line) is list:
            func(line)
        else:
            print(line)

func(l)