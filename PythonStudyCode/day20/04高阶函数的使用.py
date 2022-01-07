# @time: 2021/12/27 4:22 PM
# Author: pan
# @File: 04高阶函数的使用.py
# @Software: PyCharm


# ========================= map 映射
# 高阶函数map的使用 了解
# 映射一般是一一对应的
l = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'ddx']

# 1、使用生成式
# new_l = [name+'_dsb' for name in l]
# print(new_l)

# 2、使用map函数进行映射
new_l = map(lambda x: x + '_dsb', l)
# 使用map进行映射之后 返回的是 生成器
print(new_l)  # <map object at 0x10e71bb20>
print(list(new_l))
# new_l.__iter__()
# new_l.__next__()
# for name in new_l:
#     print(name)


# ================= 》 filter过滤
# 一般是过滤数据 从中找到需要的数据
# 需求：找到列表中以ddx进行结尾的数据
# 1、使用列表生成式
new_l = [name for name in l if not name.endswith("ddx")]
print(new_l)

# 2、使用filter过滤得到对应的数据
new_l = filter(lambda name: name.endswith("ddx"), l)
print(new_l)
for name in new_l:
    print(name)


# ======================= 》  reduce 叠加
# reduce在functools模块中
from functools import reduce
# def reduce(function, sequence, initial=_initial_missing):
# reduce迭代运算  每次迭代将返回的值和当前迭代的值进行运算  默认第一次的初始值是10
res = reduce(lambda x, y: x + y, [1, 2, 3])
print(res)


res2 = reduce(lambda x, y: x + y, ['a', 'b', 'c'], "+++")
print(res2)





