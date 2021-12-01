"""
列表类型
"""

# my_list = [1, 2, 3, 4, 5]
# print(my_list, type(my_list))
# 等价于
# my_list = list([1, 2, 3])

# list() 可以将一个可迭代的数据类型转换为列表
# 比如 str dic tuple

# # 如果是字符串会将字符串中的每一个字符转换为list中的一个元素
# list1 = list("my name is pan")
# print(list1)
# # ['m', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'p', 'a', 'n']

# # 如果是将一个字典转换为list那么获取的是字典中的key
# list1 = list({"k1": "pan", "k2": "value2", "k3": "value3"})
# print(list1, type(list1))

# 内置方法
# 1 取值/修改值
# list1 = [1, 2, "aaa", 3.14]
# 正向取
# print(list1[0])
# print(list1[2])
# list index out of range
# 下标越界 会直接报index errror
# print(list1[5])
# 也可以负向取值  -1 代表的是最后一位
# print(list1[-1])
# print(list1[-2])

# 也可以对存在的值进行修改
# list1[0] = "11111"
# list1[1] = "2222222"
# print(list1)

# IndexError: list assignment index out of range
# 如果是不存在的index 进行修改值会直接报错 index error
# list1[4] = "haha"
# print(list1)

# 2 切片取值  顾头不顾尾
# 和字符串类似
# list1 = [1, 2, "aaa", 3.14, "a", "b", [10, 11, 12, "pan"]]
# res = list1[0:2]
# print(res)

# # 设置步长
# res = list1[0:20:2]
# print(res)

# # 全部取 相当于是浅copy
# res = list1[:]
# print(list1, id(list1))
# print(res, id(res))
# print(id(res[-1]), id(list1[-1]))

# res[0] = "111111"
# print(res)
# print(list1)
#
# res[-1][0] = "aaaaaaaa"
# print(res)
# print(list1)

# # 全部取出来 并且反转过来
# res = list1[::-1]
# print(list1)
# print(res)
#
# list1[0] = "aaaaa"
# print(list1)
# print(res)

# 3 获取长度
# print(len([1, 2, 3, 4, 5]))

# # 4 in 和 not in
# print("aa" in ["11", "aa", 1, 2, 3])
# print(1 not in [1, 2, 3])


# 5 列表中追加内容
# list1 = [1, 2, 3, 4, "a"]

# # 在列表末尾添加数据
# list1.append("aaa")
# list1.append("bbb")
# print(list1)

# # 如果是添加一个列表 是将整个列表当成一个元素添加到列表中
# new_list = ["a", "b", "b"]
# list1.append(new_list)
# print(list1)

# 方法1 循环遍历新列表 （不推荐使用）
# new_list = ["a", "b", "c"]
# for item in new_list:
#     list1.append(item)
# print(list1)

# 方法2 使用extend
# 如果是将新列表中的所有元素都依次添加到列表中使用extend
# new_list = ["a", "b", "c"]
# list1.extend(new_list)
# print(list1)

# # 在某个位置插入值
# # 第一个参数是指定的位置
# # 第二个参数是需要插入的值
# list1.insert(0, "aaa")
# list1.insert(1, [1, 2])
# list1.insert(-1, True)
# print(list1)


# 6 删除值
# list1 = [1, 2, 3, 4, "a"]

# # 方法1 使用del 知识单纯的删除 没有返回值
# del list1[-1]
# print(list1)
# SyntaxError: invalid syntax
# del删除值 没有返回值
# res = del list1[0]
# 如果是删除列表 那么就不能使用列表了
# del list1
# print(list1)

# # 方法2 pop  删除指定位置的值 并返回移除的值
# res = list1.pop(0)
# print(list1)
# print(res)
# # 默认移除的是最后一个元素
# list1.pop()
# list1.pop()
# print(list1)
# # 如果移除的index超出了index 会直接报错
# # list1.pop(10)
# # print(list1)

# # 方法3 remove  直接移除对应的值 但是返回的是None
# res = list1.remove("a")
# print(res)
# print(list1)
# list1.remove(1)
# list1.remove(4)
# # 移除一个不存在的数据 会直接报错
# # remove(x) x not in list
# # list1.remove(10)
# print(list1)

# # 7 循环列表
# list1 = [1, 2, 3, 4, "ab", "b", "c"]
# for item in list1:
#     print(item)
#     # 在循环列表的时候 不要对列表进行操作
#     # list1.pop()

# # 8 count
# # 获取列表中某个元素出现的次数
# list1 = ["aa", 1, 2, "aa", "aa", "abc", "aa"]
# print(list1.count("aa"))

# # 9 index
# list1 = ["aa", 1, 2, "aa", "aa", "abc", "aa"]
# print(list1.index("aa"))
# print(list1.index("aa", 2, 10))
# # pan is not in list
# # 如果查找一个元素的index 这个元素不在列表中 会报错
# # print(list1.index("pan"))

# # 10 clear 清空列表中所有的内容 清空之后为 []
# list1 = ["aa", 1, 2, "aa", "aa", "abc", "aa"]
# list1.clear()
# print(list1)

# # 11 reverse() 将列表中的元素反转
# list1 = ["aa", 1, 2, "aa", "b", "c"]
# list1.reverse()
# print(list1)

# # 12 sort() 排序
# # 列表中的元素只有是同类型的才能进行排序
# # sort() 返回的值是None
# list1 = [10, -22, 23, 200, 9]
# # 默认是升序排序
# list1.sort()
# print(list1)
# # reverse = True 是将升序改为降序
# list1.sort(reverse=True)
# print(list1)

# TypeError: '<' not supported between instances of 'str' and 'int'
# 不同类型不能进行比较
# list1 = [10, 2, 33, "a"]
# list1.sort()
# print(list1)

# list2 = ["pan", "my", "name", "is"]
# list2.sort()
# print(list2)

# 字符串比较是根据字符串中字符的ASCII码进行比较
# 如果是第一位的字符相等那么就比较第二位的字符 依次进行比较

# 两个列表进行 比较
# 对应位置的元素必须是相同类型的元素
# 先比较第一个位置元素， 如果第一个位置的元素相等，那么就比较第二个 依次进行比较


# 了解：
# 1 队列是先进先出 FIFO
# list1 = []
# list1.append("a")
# list1.append("b")
# list1.append("c")
# print(list1)

# print(list1.pop(0))
# print(list1.pop(0))
# print(list1.pop(0))

# # 2 堆栈 后进先出 LIFO
# list1 = []
# list1.append("a")
# list1.append("b")
# list1.append("c")
# print(list1)
#
# print(list1.pop())
# print(list1.pop())
# print(list1.pop())
