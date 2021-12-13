# @time: 2021/12/13 4:39 下午
# Author: pan
# @File: 02函数参数的使用2.py
# @Software: PyCharm

"""
函数参数的混合使用
* 必须在 ** 参数的前面
* 后面定义都是 关键字参数 包括单独的关键字参数以及**kwargs
形参的位置：
位置参数 - 默认参数 - *args - 关键字参数 - **kwargs
"""

# SyntaxError: invalid syntax
# 语法错误 *args必须放在**前面
# def func1(**kwargs, *args):
#     pass

# 混合使用
# 混合使用的时候 *必须在**参数的前面
def func2(x, y=20, *args, **kwargs):
    print(x, y, args, kwargs)

# 调用的时候 位置参数也必须放到关键字参数的前面
# func2(1, 2, 3, y1=20, z=30)
# func2(y=200, x=100, z=666, k=777)
# 只有一个x是必须传递的参数
# func2(100)
# func2(x = 1000)


"""
关键字参数
在定义函数的时候 定义在*之后的参数都是关键字参数
* 可以是一个单独的 *
* 也可以是我们常见的 *args
"""
# 关键字参数 了解
# 在定义函数时， 定义在* 之后的参数都是关键字参数
# b = 100 不是默认参数  而是给关键字参数一个初始值
def func3(x, y, *, a, b=100):
    print(x, y)
    print(a, b)

# error 因为a、b都是关键字啊参数 实参必须是key=value形式
# func3(10, 20, 100, 200)
# func3(10, 20, 10, b=20)

# a, b为关键字参数 调用的时候 必须指定关键字 key = value形式
# func3(10, 20, a=100, b=200)
# func3(10, 20, b=200, a=2000)
# func3(10, 20, a=10000)

# name因为定义在 *args之后 也是关键字参数
# def func5(x, y, *args, name):
#     print(x, y, args)
#     print(name)
# func5(1, 2, 3, 4, 5)


# 综合使用：
# 顺序： 位置参数 > 默认参数 > *args > 关键字参数 > **kwargs
# 也就是 *前面的都是位置参数  *后面的都是 关键字参数
# 关键字参数必须定义在**kwargs 可变关键字参数前面
def func5(x, y=100, *args, name="哈哈", **kwargs):
    print(">>>>:", x, y, args, name, kwargs)


# 因为name是关键字参数
# 如果没有给name关键字设置 默认的值，那么调用的时候 必须指定一个name的关键字实参
# 如果name设置默认值，不传递name 默认为哈哈
func5(1, 2, 3, 4, 5, **{"key1": 11, "k2": 22, "k3": 33})
# 如果关键字参数只传递一个值 必须是单独的关键字参数值 name =
func5(1, y=2, name="didi")
func5(1, 2, name="pan")
# 传入name， 以及一个key=value的值
# k1="111" 会默认赋值给kwargs
func5(100, name="apple", k1="111", k2="222")
# 在**中传递name实参值
func5(1, 2, 3, 4, 5, **{"key1": 11, "k2": 22, "k3": 33, "name": "name的实参值"})
# x参数必须传入 y不传入默认是100 没有多余的实参那么*args为()
# 没有指定name 那么name为哈哈
# 后面的 **{"k1": 1} 会先打散为 k1=1 然后再调用函数
func5(1, **{"k1": 1})
# 位置参数必须在关键字参数前面
func5(y=1, x=100)
# SyntaxError: positional argument follows keyword argument
# func5(100, y=100, 200)
# TypeError: func5() got multiple values for argument 'y'
# func5(100, y=1000, *[10, 29], name="1")
func5(100, y=1000, name="1")
