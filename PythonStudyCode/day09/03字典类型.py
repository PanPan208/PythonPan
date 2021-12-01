"""
字典类型
使用{} 进行定义  key: value
value 可以是任何值
key 必须是可hash的 也就是不可变的数据
一般使用的是字符串str来作为key值
"""

# 1 创建字典
# d = {"k1": 111, "k2": 222, "k3": 333}
# # typeerror: unhashable type list
# # d = {"k1": 111, "k2": 222, "k3": 333, [1, 2]: 444}
# print(d, type(d))

# # 2 空字典
# d = {}
# print(d, type(d))

# # 3 dict() 使用dict进行创建字典
# d = dict(k1 = 111, k2 = 222, a = 333)
# print(d, type(d))

# # 4 数据类型转换
# info = [
#     ["name", "pan"],
#     ["age", 20],
#     ["gender", "male"]
# ]
# # d = {}

# 方法1 使用for-in进行循环info列表 转换为字典
# for k, v in info:
#     # print(k, v)
#     d[k] = v
# print(d)

# # 方法2 使用dict() 直接转换为字典
# d = dict(info)
# print(d)

# # 方法3  fromkeys
# keys = ["name", "age", "gender"]
# d = {}
# for k in keys:
#     d[k] = None
# print(d)
#
# res = {}.fromkeys(keys, None)
# print(res)

# # 内置方法
# # 1 按key进行存取值 可存可取
# d = {"k1": 111}
# print(d["k1"])
# # 对已经存在的值 是修改
# d["k1"] = "aaa"
# # 对不存在的key值 是添加
# d["k2"] = "bbb"
# print(d)
#
# # 2 字典的长度
# print(len(d))
#
# # 3 in和not in
# print("k1" in d)
# print("a" not in d)


# 4 删除值
# d = {"k1": 111, "k2": 222, "k3": 333}

# # 通用删除 没有返回值
# del d["k1"]
# print(d)

# # 使用pop 删除某一个字典中的值 并返回对应key的值 value
# res = d.pop("k3")
# print(res)
# print(d)

# # 使用popitem删除字典中的内容， 并返回(key, vlaue)
# res = d.popitem()
# print(res)
# print(d)

# 5 循环 keys和d是一样的 循环的都是key
# for k in d.keys():
#     print(k)

# for k in d:
#     print(k)

# for v in d.values():
#     print(v)

# for k, v in d.items():
#     print(k, v)


# # 6 clear 清空字典中的数据
# d = {"k1": 111, "k2": 222, "k3": 333}
# print(d)
# d.clear()
# print(d)

# # 7 update  更新字典中的内容
# d = {"k1": 111}
# # 会将新的字典中的数据 添加到d中
# d.update({"k2": 222, "k3": 333})
# print(d)


# # 8 get
# d = {"k1": 111, "k2": 222, "k3": 333}
# print(d["k1"])
# # 如果没有对应的key 取值的时候会报错
# # print(d["k10"])
#
# print(d.get("k1"))
# # 如果是使用d.get获取一个不存在的key对应的值的时候
# # 不会报错 而是返回None
# print(d.get('k10'))

# 9 setdefault()
# info = {"age": 20}
# if "name" in info:
#     # ... 等同于 pass
#     # pass
#     ...
# else:
#     info["name"] = "pan"
# print(info)

# # 使用setdefault设置值的时候
# # 如果有对应的key 不改变value值
# # 如果没有对应的key值 那么设置一个后面的默认值
# res = info.setdefault("name", "pan")
# print(info)  # {'name': 'pan'}
# print(res)  # pan
# info.setdefault("age", 100)
# print(info)
