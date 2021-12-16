# @time: 2021/12/16 2:15 PM
# Author: pan
# @File: 02函数嵌套.py
# @Software: PyCharm

"""
函数嵌套：
1、函数内调用另一个函数
2、函数内定义另一个函数
"""

# # 实例1
# def max2(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
# def max4(a, b, c, d):
#     res1 = max2(a, b)
#     res2 = max2(res1, c)
#     res3 = max2(res2, d)
#     return res3
#
# print(max4(20, 100, 99, 1000))


# 实例2 在一个函数内定义其他函数

def circle(radius, action=0):
    from math import pi

    def perimiter(radius):
        return 2 * pi * radius

    def area(radius):
        return pi * (radius ** 2)

    if action == 0:
        return perimiter(radius)
    else:
        return area(radius)

print(circle(10, 0))
print(circle(10, 2))


