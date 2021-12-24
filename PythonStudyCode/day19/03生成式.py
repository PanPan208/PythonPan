# @time: 2021/12/23 5:36 PM
# Author: pan
# @File: 03生成式.py
# @Software: PyCharm


# 1、列表生成式
l = ['alex_dsb', 'lxx_dsb', 'wxx_dsb', "xxq_dsb", 'egon']

# 1、使用for循环生成新的列表
# new_l = []
# for name in l:
#     if name.endswith("sb"):
#         new_l.append(name)
# print(new_l)


# 2、使用列表生成式进行生成新的列表
# new_l = [name for name in l]
# 后面可以跟条件语句
# new_l = [name for name in l if name.endswith("sb")]
# 可以直接对变量操作 将小写全部改为大写
# new_l = [name.upper() for name in l]
# 将所有的名字 去掉后面的 _dsb
# new_l = [name.strip("_dsb") for name in l]
new_l = [name.replace("_dsb", "") for name in l]
print(new_l)
print(list(l))


# 2、字典生成式
# keys = ['name', 'age', 'gender']
# new_dic = {key: "default" for key in keys}
# print(new_dic)

# 将下面的列表转换为字典
# 同理 后面可以跟if语句
# items = [('name', 'egon'), ('age', 18), ('gender', 'male')]
# new_dic = {k: v for k, v in items if k != "gender"}
# print(new_dic)


# 3、集合生成式
# keys = ['name', 'age', 'gender', "age"]
# new_set = {key for key in keys}
# print(new_set, type(new_set))
# print(set(keys))


# 4、生成器生成式
g = (i for i in range(10) if i > 3)
# print(g)
# print(type(g))
# g.__iter__()
# g.__next__()
# g是一个生成器 g是一个会下蛋的老母鸡
# for item in g:
#     print(item)
