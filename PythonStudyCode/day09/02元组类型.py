"""
元组类型
元组就是类似一个不可变的列表
元组是只能读 不能写
"""

# tuple 类型
# t = (1, 3.14, "abc")
# print(t, type(t))

# # 如果是只有一个元素进行括起来，那么返回的值默认是int类型
# # 如果想要得到一个单独元素的元组 那么需要在该单独元素后面添加一个逗号 ,
# # t = (10)
# t = (10,)
# print(t, type(t))

t = (1, 2, ["a", "b", "c"])
# (第一个元素的内存地址, 第二个元素的内存地址， 第三个元素的内存地址)
# 不能对元组中的元素进行修改
# t[0] = 11
# t[1] = 22
# t[2] = 33
# print(t)

# # 可以对元组中的可变列表内部的元素进行修改
# t[-1][0] = "aaa"
# t[2][1] = "bbb"
# print(t)

# # 1 其他可迭代的数据 可以转换为tuple
# print(tuple("my name is pan"))
# print(tuple([1, 2, 3, 4]))
# print(tuple({"k1": "v1", "k2": "v2", "k3": "v3"}))

# 2 内置方法
# 1 取值
t = ("aa", "bb", "cc", "aa", "aa", "aa")
print(t[0])
print(t[-1])

# 2 切片取 顾头不顾尾
print(t[0:2])
print(t[:])
print(t[::-1])

# 3 元组长度
print(len(t))

# 4 in
print("aa" in t)
print("ab" not in t)

# 5 循环元组
for item in t:
    print(item)

# 6 index  元组没有find方法
print(t.index("aa"))
# 未发现元素 会直接报错
# print(t.index("aaaa"))
# t.find("aa")

# 7 count
# 查询元组中 "aa" 元素的个数
print(t.count("aa"))
