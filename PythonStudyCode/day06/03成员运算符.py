"""
成员运算符： in  is
"""

# 1 in
# 判断一个字符串是否是在一个字符串中
print("pan" in "my name is zhao pan")
print("123" in "my age is 120")

# 判断一个元素是否在一个列表中
# not in 是判断是否是不在整个列表中
# 推荐使用: 元素 not in list
# 而不是: not 元素 in list
print(10 in [10, "112", 23, "11"])
print(20 not in [10, 20, 30])  # 推荐使用
# print(not 100 in [100, 200, 300])  # 不推荐使用

# 判断一个元素是否在一个字典中
# 字典判断的时候是判断的是元素是否在字典的key中
print(100 in {"name": "pan", 100: "100"})


# 2 is
# 判断的是两个变量的id是否一致
x = 10
y = x
print(id(x), id(y))
print(x is y)
y = 11
print(id(x), id(y))
print(x is y)
