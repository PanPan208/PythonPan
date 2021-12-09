# @time: 2021/12/8 6:32 下午
# Author: pan
# @File: 04文件操作w模式.py
# @Software: PyCharm

"""
w模式： 只写模式
w+ 可写可读模式  一般不结合使用
1、在没有文件的时候 会自动创建一个文件 并写入内容
2、在已经有文件的时候 会先清空所有的内容 然后再写入内容
"""

# 实例1
# w模式 写入模式
# 如果没有文件 会自动创建一个文件
# 如果有文件 有内容 会将内容进行清空 然后再写入内容
# with open(r"res/c.txt", mode="wt", encoding="utf-8") as f:
#     f.write("aa\n222b\n3333ccc")
#     # not readable 因为是wt 模式所以是 不能进行读取文件内容的
#     # res = f.read()
#     # print(res)


# 实例2
# # w+ 模式  可写可读模式
# with open(r"res/c.txt", mode="w+t") as f:
#     f.write("哈哈哈")
#     # 为什么不能读出来内容？
#     # 因为写入内容之后 指针的位置会在最后位置
#     # 这时候再读入内容 是从光标位置 开始读取 这时就读不出内容的
#     # res = f.read()
#     # print(res)
#     # 将光标移动到开始的位置 这时候就可以读出内容了
#     f.seek(0, 0)
#     res = f.read()
#     print(res)


# 实例3
# w 写入二进制数据
# b 模式只能写入的是 二进制数据
# b 模式 不能指定编码格式
# encoding="utf-8"
# ValueError: binary mode doesn't take an encoding argument
# with open(r"res/c.txt", mode="wb") as f:
#     # 如果指定的是b 模式 必须写入的是二进制数据
#     # f.write("你好")  # error 不能是非二进制数据
#     # >>>>>> 1 第一种: 二进制 直接在前面添加一个b
#     # 后面内容只能是  字母和数字的组合内容形式
#     # f.write(b'aaad123')
#     # f.write(b'aaad123哈哈')  # error 不能有中文
#     # >>>>>> 2 第二种: 使用bytes函数
#     # 第一个参数 需要写入的字符 第二个参数是编码方式
#     # f.write(bytes("你好", "utf-8"))
#     f.write(bytes("Hello World"), "utf-8")
#     # >>>>>> 3 第三种: 使用encode直接编码为二进制数据
#     f.write("你好niha你好呀".encode("utf-8"))


# 实例4
# with open("res/d.txt", mode="wt+", encoding="utf-8") as f:
#     # 判断是否是可写
#     if f.writable():
#         print(f.writable())  # True
#         print("可写")
#         f.write("hello")

# 实例5
# 将一个列表中的数据 直接写入到文本中
l = ["hello\n", "world\n", "bbb\n", "dddd"]
with open("res/e.txt", mode="wt") as f:
    # f.writelines(l)
    for item in l:
        f.write(item)


# flush
# 不是每次调用 write的时候 就会将内存数据 写入到硬盘中
# 而是等到一定的数据之后 才会写入
# flush() 是强制进行写入

# 其他类型
# with open("res/a.txt", mode="rt") as f:
#     print(f.readable())
#     print(f.writable())
#     print(f.encoding)
#     print(f.name)
#     print(f.closed)
# print(f.closed)
