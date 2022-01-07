# @time: 2021/12/23 5:32 PM
# Author: pan
# @File: 01yield表达式.py
# @Software: PyCharm

# x = yield None

"""
x = yield xxx

当调用生成器的send函数的时候 会给yield发送值
调用send函数和调用next函数类似
调用send函数 会给yield传值 然后yield再降值传给x
调用next函数 传的是None
"""


'''
实例1 

def dog(name):
    print(f"{name} 准备吃东西了...")
    while True:
        x = yield
        print(f'dog  {name} 吃了 食物:{x}')


# 获取的是一个生成器
dog_g = dog("小黑")
print(dog_g)

# 不能发送一个非空的数据到一个刚刚开始的生成器
# TypeError: can't send non-None value to a just-started generator
# dog_g.send("包子")

# 1、第一步 必须先发送一个None 或 先调用一下next
dog_g.send(None)
# next(dog_g)
# 2、调用send相当于调用了next
# 并将传入的值传给yield 然后yield再降值传给x
# send 调用之后会给yield传值
# next 调用之后不会给yield传值  next(dog_g)
dog_g.send("包子")
dog_g.send("一根骨头")
dog_g.close()
# 生成器关闭之后再send值 会报StopIteration错误
# dog_g.send("馒头")
# 调用next也是一样 会报StopIteration错误
# next(dog_g)
'''


# 实例2
def dog(name):
    # 定义一个存放食物的列表
    food_list = []
    print(f"{name} 准备开始吃饭了...")
    while True:
        x = yield food_list
        print(f"dog {name} 吃了: {x}")
        food_list.append(x)


dog_g = dog("小黄")
res = dog_g.send(None)
print(res)

# send的值会传给yield然后传给x
# 返回值food_list会会返回给res1
res1 = dog_g.send("包子")
print(res1)

res2 = dog_g.send("馒头")
print(res2)

# 传入的是一个None
print(dog_g.__next__())


"""
使用场景：
如果需要传入值的话 需要使用send
如果只是迭代取值 只需要使用next即可
"""
