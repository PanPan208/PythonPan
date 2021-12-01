"""
深浅copy
"""

list1 = ["a", "b", [111, 222]]

# 将list1直接赋值给list2 这个不叫copy
# 这是两个变量都指向一个同一块栈内存地址
# 任意一个中的数据发生变化 另一个会跟着变化
# list2 = list1
# print(list1, list2)
# print(id(list1), id(list2))
# print(id(list1[0]), id(list1[1]), id(list1[2][0]), id(list1[2][1]))
# print(id(list2[0]), id(list2[1]), id(list2[2][0]), id(list2[2][1]))


# list1[0] = "aaa"
# list1[1] = "bbb"
# list1[2][0] = 1
# list1[2][1] = 2
# print(list1, list2)


# 浅copy
# copy之后 两个变量指向两个不同的内存地址
# 这两个不同的地址 指向的堆中的第一层地址都是一样的
# copy之后第一层的所有元素指向的地址都是一样的
# list2 = list1.copy()
# print(list1, list2)
# print(id(list1), id(list2))
# print(id(list1[0]), id(list1[1]), id(list1[2][0]), id(list1[2][1]))
# print(id(list2[0]), id(list2[1]), id(list2[2][0]), id(list2[2][1]))

# I： 修改列表1中的不可变数据
# 如果改变的是不可变的量 相当于将list中的不可变的量重新赋值
# list2中的不可变数据还是指向之前的地址， 所以list2中对应的不可变的量不会改变
# list2 = list1.copy()
# list1[0] = "pan"
# list1[1] = "bbb"
# print(list1, list2)

# II： 修改的是列表1中可变列表中的不可变数据
# 改变第二层中的数据  list1 list2都是指向这个子列表的地址
# 所以修改这个子列表中的数据
# 两个列表都会跟着变化
list2 = list1.copy()
list1[2][0] = "AAA"
list1[2][1] = "BBB"
print(list1)
print(list2)

# III： 直接将列表1中的可变数据直接赋值
# 直接将list1中的子列表改为其他值
# 相当于list1重新指向了一个新的地址
# list2还是指向之前的子列表的地址  所以list2不会改变
list1[2] = "haha"
print(list1, list2)

# 综上：两个列表并没有完全独立开来
# 当修改的是子列表中的数据的时候 两个列表都会跟着变化
# 如果是直接将子列表重新赋值 相当于指向了一个新的内存地址
# 另一个列表还是指向之前的地址 所以不会变化


# 2 深copy
import copy

# 使用copy库中deepcopy进行深copy
list2 = copy.deepcopy(list1)

# 深copy之后 两个列表指向了两个不同的地址
# 对于列表中的不可变数据 指向的还是同一块内存地址
# 这是因为当修改不可变数据的时候 都是相当于重新指向新的一块内存地址
# 所以不用重新指向一块新的内存地址 这样可以省内存

# 对于列表中的可变数据 新列表指向了一个不同的地址
# 这个可变数据中的子数据是不可变数据 又指向了同一个相同的内存
# 同理上面的是为了 省内存
# print(list1, list2)
# print(id(list1), id(list2))
# print(id(list1[0]), id(list1[1]), id(list1[2]))
# print(id(list2[0]), id(list2[1]), id(list2[2]))

# 修改不可变类型的数据 只会修改对应的列表
# list1[0] = "pan"
# list1[1] = "xxx"
# print(list1, list2)

# 修改列表中的可变类型
# 因为两个列表指向不同的可变类型  所以修改某一个可变类型， 另一个列表不会改变
# list1[2] = "new list"
# print(list1, list2)

# 修改可变类型中的不可变类型
# 修改不可变类型 都会指向一个新的内存地址 所以修改某一个列表中的不可变类型 另一个不会改变
# 所以深copy后 对于不可变的类型 都是指向相同的地址
# list1[2][0] = "new list"
# print(list1, list2)

# 综上所述： 深copy 修改一个列表中的可变和不可变数据另一个列表都不会变化
