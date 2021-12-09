# @time: 2021/12/8 6:34 下午
# Author: pan
# @File: 06文件操作x模式.py
# @Software: PyCharm

"""
r 模式 写入模式
类似w模式
和w模式的区别：
x模式
1、如果是文件不存在 会创建文件并写入内容
2、如果是文件存在那么 会报错
"""

# x 写入模式
# 如果文件 不存在 打开文件 写入内容
# 如果文件已经存在 那么会报错 文件已经存在 File exists: 'f.txt'
# with open("res/f.txt", mode="xt") as f:
#     # 因为是x模式 是写入模式 所有不能使用read
#     # f.read()
#     f.write("哈哈")
