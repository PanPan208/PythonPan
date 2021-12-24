# @time: 2021/12/24 9:29 AM
# Author: pan
# @File: 03叠加装饰器分析.py
# @Software: PyCharm


def deco1(func):
    def wrapper1(*args, **kwargs):
        print("装饰器1运行了")
        res = func(*args, **kwargs)
        return res
    return wrapper1


def deco2(func):
    def wrapper2(*args, **kwargs):
        print("装饰器2运行了")
        res = func(*args, **kwargs)
        return res
    return wrapper2


def deco3(x, y, z):
    def outter(func):
        def wrapper3(*args, **kwargs):
            print("装饰器3运行了")
            res = func(*args, **kwargs)
            return res
        return wrapper3
    return outter


@deco1  # index = deco(index)             ===> wrapper2的地址 = wrapper1的地址
@deco2  # index = deco2(index)            ===> outter.wrapper3的地址 = wrapper2的地址
@deco3(1, 2, 4)  # @outter = @deco(1, 2, 4) ===> index = outter(index)  ===> index的地址 = outter.wrapper3的地址
def index(x, y):
    print(f'index of x = {x}, y = {y}')


index(10, 20)


"""
总结：
加载顺序是从下往上
执行顺序是从上到下
"""