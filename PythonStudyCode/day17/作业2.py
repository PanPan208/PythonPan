# @time: 2021/12/22 4:25 PM
# Author: pan
# @File: 作业2.py
# @Software: PyCharm


# 思考题（选做），叠加多个装饰器，加载顺序与运行顺序，
# 可以将上述实现的装饰器叠加起来自己验证一下
# @deco1 # index=deco1(deco2.wrapper的内存地址)
# @deco2 # deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
# @deco3 # deco3.wrapper的内存地址=deco3(index)
# def index():
#     pass


def authen1(func):
    def wrapper(*args, **kwargs):
        print("新授权方法1")
        res = func(*args, **kwargs)
        return res
    return wrapper

def authen2(func):
    def wrapper(*args, **kwargs):
        print("新授权方法2")
        res = func(*args, **kwargs)
        return res
    return wrapper

def authen3(func):
    def wrapper(*args, **kwargs):
        print("新授权方法3")
        res = func(*args, **kwargs)
        return res
    return wrapper


# 加载顺序是从下到上
# 执行顺序是从上到下 依次进行运行
@authen3
@authen1
@authen2
def test():
    print("test")
    pass

test()
