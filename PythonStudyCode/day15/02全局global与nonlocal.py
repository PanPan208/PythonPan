# @time: 2021/12/13 6:29 下午
# Author: pan
# @File: 02全局global与nonlocal.py
# @Software: PyCharm

"""
如何要在函数内部修改全局的变量？
1、全局变量为不可变数据
使用global
2、全局变量为可变数据
什么也不需要使用 可以直接进行append等操作(非重新赋值)
"""


# 实例1
# 名称空间的引用只与定义阶段有关
# x = 111
# def func1():
#     x = 222
#     print(x)
# func1()  # 222
# # 函数内修改x 并不能对全局的x产生影响
# # 因为在func1中定义的x是重新定义了 一个局部的变量x
# print(x)  # 111


# # 实例2
# # 如果在局部想要修改全局名字对应的值(不可变类型) 需要使用global
# x = 111
# def func1():
#     # 声明这个x是全局的变量名称 不需要再造一个变量了
#     global x
#     # 这时候修改的x 就是对全局的x进行修改 而不是重新创建了一个局部名称x
#     x = 222
#     print(x)
# func1()
# # 因为在函数内部使用了global x 那么x会被修改
# print(x)  # 222


# # 实例3 可变数据
# x = [111, ]
# def func3():
#     # 直接找到x 对x进行append
#     x.append("222")
#     # 如果是直接使用=进行赋值新值 那么就不是对全局变量x进行 修改了
#     # 而是重新创建了全新的局部变量x
#     # 如果是将x重新赋值给一个不可变数据 也不会对全局的x产生影响
#     # x = 100
#     # x = ["a", ]
#     print(x, id(x))
# func3()
# # 如果是一个可变数据 在函数内部对可变数据进行修改 那么全局的x也会跟着变化
# print(x, id(x))


"""
修改函数 外层函数内部的名称
使用nonlocal
"""

# 实例4 nonlocal
# nonlocal 修改函数外层函数内名称空间的数据
x = 0
l = ["aaa", ]
def f1():
    x = 11
    # l = ["bbb", ]
    def f2():
        # 1、默认f2函数中 不会修改外层的名称
        # x = 22
        # 2、使用nonlocal 修改函数外层函数内部的对应名称的值 不可变数据
        nonlocal x
        x = 22
        # 3、如果使用的是global 修改的是全局的对应的名称的值 不可变数据
        # global x
        # x = 333
        # 针对可变数据 不需要使用global
        l.append("CCC")
    f2()
    print(x)
    print(l)
f1()
print(x)

