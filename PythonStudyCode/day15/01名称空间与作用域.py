# @time: 2021/12/13 6:28 下午
# Author: pan
# @File: 01名称空间与作用域.py
# @Software: PyCharm

"""
namespace: 名称空间
存放名字的地方，是对栈区进行的划分， （值都是放在堆中）
1、内置名称空间：
存放的是python解释器内置的名字 比如: int print input is等等
存活周期：python解释器启动就会产生，解释器关闭则销毁

2、全局名称空间：
只要不是内置的名称空间以及在函数内部定义的名称，剩余其他的都是全局名称空间。
比如：全局定义的变量名、定义的函数名
存活周期：python文件执行则产生，文件关闭则销毁

3、局部名称空间：
存在于函数def内部定义的，都是局部名称空间。
比如：函数内部定义的变量名、函数的参数名
存活周期：函数调用时产生，函数调用完毕则销毁


》》》》》加载顺序：
内置名称空间》全局名称空间》局部名称空间
》》》》》销毁顺序：
局部名称空间》全局名称空间》内置名称空间

》》》》》名称查找优先顺序：
如果在局部：先在局部名称空间查找 然后全局名称空间查找 最后是内置名称空间
如果在全局：先在全局名称空间查找 然后再在内置名称空间查找
"""

# 实例1
# # input = "111"
# def func1():
#     # input = "222"
#     print(input)
# func1()

# 实例2
# input = "111"
# def func2():
#     input = "333"
# func2()
# print(input)
# func2()

# 实例3
# def func3():
#     print(x)
# # 在定义x之前 调用方法 找不到x
# # func3()
# x = 100
# # func3()

# 实例 名称空间的嵌套关系以函数定义阶段为准 与调用位置无关
# x=1
# def func():
#    print(x)
#
#
# def foo():
#     x=222
#     func()
#
# foo()  # 1


# 实例函数嵌套

# # D 如果在全局也没有定义input 那么就会在内置名称区去查找
# # C 如果在f2和f1中都没有定义input 那么就会在全局名称区去查找
# # input = "111"
# def f1():
#     def f2():
#         # A 如果是在函数f2中 定义input 那么打印就会先找这个input名称
#         # input = "333"
#         print(input)
#
#     # B 如果f2中没有定义input 那么就会在f1函数内部寻找input
#     # input = "222"
#     f2()
#     # 在赋值之前引用input会报错
#     # input = "2"
# f1()


# 实例
# x = 1
# def func4():
#     # local variable 'x' referenced before assignment
#     # 不能在引用名称之后 再设置名称
#     print(x)
#     x = 1000
# func4()

"""
作用范围：

内置名称和全局名称空间：
1、在全局存活
2、全局有效 被所有函数共享

局部名称空间：
1、临时存活
2、只在局部有效 函数内有效
"""

# 名称
# LEGB

# # builtin
# # global
# def f1():
#     # enclosing
#     def f2():
#         # enclosing
#         def f3():
#             # local
#             pass

