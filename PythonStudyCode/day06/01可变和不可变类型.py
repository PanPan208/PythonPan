"""
Python中的可变类型/不可变类型
可变类型： 值变化id不变
不可变：值变化id变化
"""

# x = 10
# print(x, id(x))
# x = 20
# print(x, id(x))
# 值变化 id也变化  int类型是不可变类型

# x = True
# print(x, id(x), type(x))
# x = 12
# print(x, id(x), type(x))

# Python中的int float str bool 类型都是不可变类型
# Python中的 list dic tuple都是可变类型

# 列表中的数据变化 但是列表的id不变  所以列表是一个可变的类型
# list = [1, 2, 310, "pan"]
# print(list, id(list))
# list.append("zhao")
# print(list, id(list))



# 字典也是一个可变的类型
# 字典中的key只能是 不可变的类型 也就是可hash
# 字典中的value可以是任何类型
# 字典中添加新数据 但是字典的id不变， 所以字典是可变类型
dic = {"pan": 10, 10: 20, True: "hah", 10.10: "10.10"}
print(dic, id(dic))
dic["a"] = "aaaaa"
print(dic, id(dic))
# dic[[1, 2]] = [1, 2]  # error


# 可hash
# print(hash(112))
# print(hash(10.23))
# print(hash("12jj"))
# print(hash(True))

# 不可hash
# print(hash([1, 2]))
# print(hash({"12": "12"}))





