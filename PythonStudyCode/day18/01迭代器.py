# @time: 2021/12/22 5:19 PM
# Author: pan
# @File: 01迭代器.py
# @Software: PyCharm

"""
1、什么是迭代器：
    指进行迭代取值的工具，
    迭代：是一个重复的过程，每次重复都是基于上一次重复的结果而继续重复
    单纯的重复并不是迭代
"""

# 不是迭代
# while True:
#     print('haha')

# 是迭代
# count = 0
# while count < 5:
#     print(f'count is {count}')
#     count += 1

"""
2、为什么要有迭代器？
    迭代器是指迭代取值的工具，
    涉及到将多个值 循环取出来的类型有：列表、元组、字典、集合、字符串、文件
    
    while取值
    只能取那些有索引的数据类型： 列表、字符串、元组  使用len(obj)获取长度
    
    为了解决while也可以取那些没有索引的数据类型，
    Python提供了一个不依靠索引进行取值方式，就是迭代器
"""

# l = [1, 2, 3, 4, 5]
# count = 0
# while count < len(l):
#     print(l[count])
#     count += 1

"""
3、如何使用迭代器
但凡内置中是有__iter__() 的对象 ===> 都是可迭代的对象
内置中有__next__()和__iter__()的对象 ===> 都是迭代器对象

列表、元组、字典、集合、字符串 都是可迭代对象
文件f 既是可迭代对象 也是迭代器对象

调用可迭代对象下的iter()方法 可以将其转换为迭代器对象
有了迭代器对象就可以使用next()函数 获取对象中的数据了

l = [1, 3, 5]
l_iterator = l.__iter__()

s = "hello world"
s.__iter__()

t = (1, 2)
t.__iter__()

se = {1, 2}
se.__iter__()

d = {"a": 1, "b": 2}
d.__iter__()

# f既是可迭代对象也是迭代器对象
with open("a.txt", mode="rt") as f:
    f.__iter__()
    f.__next__()
"""

# 实例1
# d = {"a": 111, "b": 222, "c": 333}
# 将一个可迭代的对象转换为一个迭代器对象
# d_iterator = d.__iter__()
# print(d_iterator)
# 返回的是一个 字典key迭代器
# 也就是一个 "会下蛋的老母鸡"  基本上不占用什么内存空间 需要的时候使用next进行取值即可
# <dict_keyiterator object at 0x103a9f360>

# 可以通过__next__() 函数获取迭代器每次迭代的值
# print(d_iterator.__next__())
# print(d_iterator.__next__())
# print(d_iterator.__next__())
# print(d_iterator.__next__())
# 如果迭代器中的内容都取出来了，再取 就取不出来了
# 而且会抛出一个异常 StopIteration


# 实例2
d = {"a": 111, "b": 222, "c": 333}
d_iterator = d.__iter__()
# 如果迭代器中的内容有很多 可以使用while循环进行取值
# 并且在while循环中可以使用try进行捕获StopIteration异常
while True:
    try:
        print(d_iterator.__next__())
    except StopIteration:
        break

print("第二次取值>>>>>>>>>")
# 在一个迭代器中的所有值都取出来之后 再进行取值 取不出来
# 好比：一个老母鸡将鸡蛋全部下完了，
# 如果再想要鸡蛋 需要再造一个老母鸡
d_iterator = d.__iter__()
while True:
    try:
        print(d_iterator.__next__())
    except StopIteration:
        break


# 实例3
# 只要是一个可迭代的对象都可以转换为一个迭代器对象
my_str = "Hello World!"
str_iterator = iter(my_str)
while True:
    try:
        print(f"迭代:{next(str_iterator)}")
    except StopIteration:
        break


"""
for循环的工作原理：
1、通过__iter__() 得到一个迭代器对象
2、迭代器对象通过 __next__() 获取到迭代器中的值 然后赋值给for 后面的变量
3、循环反复的执行第二步  直到抛出StopIteration异常， for循环会自动捕获异常然后结束循环
"""
# 实例3
li = [10, 20, 30, 100, 200, 1000]
for i in li:
    print(f"for i = {i}")

# 任何for循环的语句 都可以转换为使用while循环进行遍历
li_iterator = li.__iter__()
while True:
    try:
        print(f"while i = {li_iterator.__next__()}")
    except StopIteration:
        break


# 1、可迭代对象：
# 可迭代对象调用iter可以得到的是一个迭代器对象
# 可迭代对象没有next函数
# 2、迭代器对象：
# 迭代器对象调用iter得到的还是一个迭代器对象 还是其本身
# 迭代器调用next函数得到的是每次迭代的值
# <list_iterator object at 0x1048b1280>
# <list_iterator object at 0x1048b1280>
# True
print(li_iterator)
print(li_iterator.__iter__())
print(li_iterator is li_iterator.__iter__().__iter__())


# 调用len() 也就是调用 "".__len__()
# __iter__()  和调用iter()  是一样的效果的
# 其他 __xx__()  都有两种调用方式
temp_str = "Hello world"
print(len(temp_str))
print(temp_str.__len__())
print(iter(temp_str))
print(temp_str.__iter__())


# list() 的原理同for 循环一样
# list(T)
# 后面参数是一个 可迭代的对象
# 1、通过iter获取一个迭代器对象
# 2、通过迭代器对象的next获取每一次迭代的值 放入到list列表中
# 3、循环执行第二步 直到抛出异常StopIteration
list("Hello")


# 文件是迭代器对象
with open("a.txt", "rt") as f:
    # 1 可以直接使用for in进行读取文件内容
    # for line in f:
    #     print(line)

    # 2 可以使用迭代器进行迭代取值
    # f 打开的文件是一个迭代器对象
    # 有iter和next函数
    # f_iterator = f.__iter__()
    while True:
        try:
            # print(f_iterator.__next__())
            print(next(f))
        except StopIteration:
            break

"""
迭代器的优缺点
优点：
1、为序列数据和非序列数据 提供了一个统一的迭代取值的方式
2、惰性取值：迭代器对象表示的是一个数据流， 可以在只需要的时候调用next进行取值
像一个会下蛋的老母鸡，在内存中只有一个值，但是却可以存放无限大的数据流
如列表：列表的数据需要先存放在列表中
受内存的限制 列表中存放的数据是有限的

缺点：
1、只有一个一个的取完所有的值 才能知道迭代器长度
2、只能取下一个值， 不能回退取 之前的值， 也不能直接取到某个对应的值，
如果想要取到对应的值，只能依次循环next取到该值，
如果想要再次取迭代器中的值， 只能再造一个迭代器  迭代器更像是一个一次性的产品
"""
