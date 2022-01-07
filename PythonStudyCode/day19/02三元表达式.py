# @time: 2021/12/23 5:34 PM
# Author: pan
# @File: 02三元表达式.py
# @Software: PyCharm


"""
三元表达式 《==》 类似OC中三目运算符
OC语法：
x = 表达式 ? 为真返回的值 ： 为假返回的值
Python语法：
x = 表达式为真返回的值 if 表达式 else 表达式为假返回的值
"""

# 返回两个数中的较大值
'''
# 实例 使用函数进行实现
def func(x, y):
    if x >= y:
        return x
    else:
        return y

print(func(10, 20))
print(func("abc", "bbb"))
'''


# 三元表达式
# 语法格式：
# 条件成立返回的值 if 条件 else 条件不成立返回的值

x = 10
y = 20
# 返回两个数中较大的值
res = x if x >= y else y
print(res)

res = 1111 if True else 2222
print(res)


# 实例 比较两个变量 返回大的值
def func(x, y):
    # if x >= y:
    #     return x
    # else:
    #     return y
    return x if x >= y else y

print(func(10, 20))
print(func("zhao", "pan"))
print(func(1000, 33))