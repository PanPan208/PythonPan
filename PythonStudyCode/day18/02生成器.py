# @time: 2021/12/22 5:20 PM
# Author: pan
# @File: 02生成器.py
# @Software: PyCharm

"""
自定义一个迭代器：
需要使用到yield关键字
器：工具 创建一个迭代器就是创建一个工具，可以当成工具的有函数、类等
在函数内一旦调用了yield关键字 那么调用函数并不会执行函数 而是会返回一个生成器对象
函数本身还是一个函数 只有调用函数的时候才会产生一个生成器
生成器对象即自定义的迭代器
"""


def func():
    print("第一次迭代")
    yield 1
    print("第二次迭代")
    yield 2
    print("第三次迭代")
    yield 3
    print("第四次迭代")


g = func()
print(func)
# func本身还是function
# <function func at 0x103c1e430>
print(g)
# generator 生成器对象
# <generator object func at 0x10a65bcf0>
print(type(g))
# type类型是 generator
# <class 'generator'>

# 生成器就是迭代器对象 有iter和next函数
# g.__iter__()
# g.__next__()

# 当执行next的时候 会执行函数体中的代码 直到遇到yield停下来
# 并将yield后的值 返回
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())  # 如果没有迭代数据了 会抛出一个异常StopIterator

while True:
    try:
        print(g.__next__())
        # print(next(g))
    except StopIteration:
        break


# 实例：
# 自定义创建一个可以存放无限大数据的迭代器
def my_range(start, end, step):
    while start < end:
        yield start
        start += step


g = my_range(1, 10, 2)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(next(g))
# print(next(g))
# print(next(g))

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break


# for i in my_range(1, 20, 1):
#     print(i)

"""
总结：
有了yield 我们就可以创建一个生成器了
也就是创建自定义迭代器的方式
yield和return的不同之处是， return是直接结束函数并将值返回
而yield可以挂起函数、用于多次的返回值
直到运行生成器的next函数的时候 才会返回值
"""