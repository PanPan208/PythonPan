"""
集合类型
集合使用set进行定义 使用{} 括起来
1、集合内元素必须为不可变类型
2、集合内元素无序
3、集合内元素没有重复

集合可以做交集并集差集等
可以使用集合用来去重 但是有局限性
"""

# ----------------------------------  1
# 定义集合1
# s = {1, 23, 1, 1, 2, 3}
# print(s, type(s))

# 如果一个中括号中没有内容 那么默认是字典
# s = {}
# print(s, type(s))  # dict
# 定义一个空集合 使用set()
# s = set()

# 可迭代类型都可以转换为集合类型  会自动去重
# s = set([1, 2, 3, 3, 2, 1, 1])
# s = set({"k1": "v1", "k1": "v1", "k2": "v2"})
# s = set((1, 2, 3, 3, 4, 3, 5))
# s = set("Hello world")
# print(s, type(s))

# ----------------------------------  2
friend1 = {"tony", "pan", "mark", "jeck", "pan", "pan"}
friend2 = {"tony", "pan", "mary", "mali"}

# 使用代码取交集
# l = []
# for x in friend1:
#     if x in friend2:
#         l.append(x)

# 取交集 &
# print(friend1 & friend2)
# print(friend1.intersection(friend2))

# # update是做完交集之后会将结果返回给friend1
# print(friend1.intersection_update(friend2))
# print(friend1)
# print(friend2)

# 取并集 ｜
# print(friend1 | friend2)
# print(friend1.union(friend2))

# 差集 -  只在谁中使用谁去减去另一个集合
# 一 只在friend1中
# print(friend1 - friend2)
# print(friend1.difference(friend2))

# 会将做完差集的结果返回friend1
# print(friend1.difference_update(friend2))
# print(friend1)
# print(friend2)

# 二 只在friend2中
# print(friend2 - friend1)
# print(friend2.difference(friend1))

# 对称差集 ^   就是去掉两个集合中重复的部分
# (friend1 - friend2) | (friend2 - friend1)
# print(friend1 ^ friend2)
# print(friend1.symmetric_difference(friend2))

# # 将做完对称差集的结果返回给friend1
# print(friend1.symmetric_difference_update(friend2))
# print(friend1)
# print(friend2)


# ----------------------------------  3
# # 父子集关系
# s1 = {1, 3, 4}
# s2 = {1, 3, 4}
# # 如果一个集合包含另一个集合 那么就是 >  superset
# print(s1 > s2)
# # 当s1大于或等于s2的时候 才说s1是s2的父集
# print(s1.issuperset(s2))  # 等价于 >=
#
# print(s2 < s1)
# print(s2.issubset(s1))
#
# # s1和s2 互为父子集
# print(s1 == s2)


# ----------------------------------  4

# 去重 有局限性
# 1 只能去不可变的类型
# 2 不能保证去重之后的列表顺序
# l = [
#     {'name':'lili','age':18,'sex':'male'},
#     {'name':'jack','age':73,'sex':'male'},
#     {'name':'tom','age':20,'sex':'female'},
#     {'name':'lili','age':18,'sex':'male'},
#     {'name':'lili','age':18,'sex':'male'},
# ]
# new_l = []
# # 使用循环遍历 进行去重
# for item in l:
#     if item not in new_l:
#         new_l.append(item)


# ----------------------------------  5
# #  获取集合的长度
# print(len({1, 2, 3, 3, 3, 4}))  # 4
# # in
# print("a" in {"a", "b", "c"})  # true
# # 循环
# for item in {"a", "b", "b", "b", "c"}:
#     print(item, end=" ")  # a c b


# ----------------------------------  6
# # 6 discard remove 删除集合中的元素
# s = {1, 2, 3, 3, 4, 5}
# s.discard(1)
# print(s)
# s.discard(2)
#
# # discard 如果是删除一个不存在的一个元素 do nothing
# # 不会报错 推荐使用
# # s.discard(10)
# # remove 如果是删除一个不存在的元素  运行直接报错
# # s.remove(10)
# # print(s)


# 7 update - 更新集合中的数据 ------------------
# s = {1, 2, 3, 3, 4, 5}
# # update 更新集合中的内容
# # 传入的是一个可迭代对象    可以是字符串、列表、字典、元组
# # 如果集合中原本就有对应的元素 do nothing
# # 如果集合中原本中没有对应的元素 那么就添加到这个集合中  无则添加
# s.update({1, 2, 10})
# print(s)
# s.update("hello")  # hello会将字符串中的每一个字符添加到集合中
# print(s)
# s.update([1, 100])
# print(s)
# s.update({"k1": "v1", "k2": "v2"})
# print(s)


# # 8 pop 随机移除一个集合中的数  默认移除第一个？
# s = {1, 2, 3, 3, 4, 5}
# # Remove and return an arbitrary set element.
# # 删除并返回一个任意的元素
# s.pop()
# print(s)
# s.pop()
# print(s)
# res = s.pop()  # 移除之后并返回移除的值
# print(s)
# print(res)
# s.clear()
# print(s)
# # 'pop from an empty set'
# # 如果是从一个空集合中删除元素 那么会报错
# s.pop()
# print(s)


# # 9 add 添加元素
# s = {1, 2, 3, 3, 4, 5}
# s.add(10)
# s.add(100)
# # 只能add不可变的数据
# # s.add({1, 2, 200, 300})
# s.add((200, 300))  # 可以添加
# print(s)
# # 清空集合中的所有元素
# s.clear()
# print(s)


# # 10 isdisjoint 判断两个集合是不是没有交集  互斥
# # 没有公共部分 返回True
# s = {1, 2, 3, 3, 4, 5}
# print(s.isdisjoint({10, 12, 11}))
# # true
# print(s.isdisjoint({10, 12, 1}))
# # false
