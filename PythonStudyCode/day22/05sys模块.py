# @time: 2022/1/12 5:54 PM
# Author: pan
# @File: 05sys模块.py
# @Software: PyCharm
"""
sys系统模块
"""
import sys

# 项目环境变量
# print(sys.path)

# 获取系统的平台
# darwin
# print(sys.platform)


# 获取python解释器的版本
# print(sys.version)
# 3.8.2 (default, Jun  8 2021, 11:59:35)
# [Clang 12.0.5 (clang-1205.0.22.11)]


# 获取一个变量的引用计数
# a = 10
# b = a
# print(sys.getrefcount(a))


# # 设置和获取递归函数最大递归的次数
# sys.setrecursionlimit(100)
# print(sys.getrecursionlimit())


# 获取系统中的模块
# print(sys.modules.keys())


# 获取执行文件的传入的参数
# 第一个参数是文件名  第二个/第三个是传入文件的参数
print(sys.argv)
