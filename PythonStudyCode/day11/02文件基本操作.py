"""
t和b模式不能单独使用 必须和r/w/a模式结合使用

t 模式 文本模式 针对于文本模式 会比较方便
    - 读取都是以str 也就是unicode为单位的
    - 针对的主要是文本文件
    - 需要指定编码格式 utf-8

b 模式 bytes模式 可以针对任何文件 通用
    二进制模式 也就是bytes模式
    可以操作任何文件
    不能指定encoding
    如果是读取文本文件 需要将bytes进行解码

"""

# r 只读模式  只能read 不能write (r模式必须文件存在)
# w 只写模式  打开一个文件会将内容全部清空 之后再写入内容
# a 只追加模式  只会在文件的末尾进行追加内容
# + 模式 不能单独使用 需要和r w a 一起使用
# r+  w+ a+ 可读可写模式
# 一般 + 模式 不经常使用, 一般都是单独使用某个模式
# x 模式 类似w模式 只写模式  如果文件已经存在会报错


# 实例：
# 如果没有指定编码方式 默认是使用系统自己的编码方式
# linux系统默认的是 utf-8
# windows系统默认使用的是 gbk

# with 语法： 文件对象/文件句柄
# 1、with open 打开一个文件 赋值给一个变量 as f
# 2、with语句完成之后 会自动关闭文件 相当于执行了f.close()
# 3、with后面可以打开多个文件 使用逗号分割开
# with open('res/a.txt', "rt") as f1, \
#         open('res/b.txt', mode="rb") as f2:
#     res1 = f1.read()
#     print(res1)
#     res2 = f2.read()
#     print(res2)

# t模式 读取文本内容
# 只有在t模式下 才可以指定encoding 如果不指定会使用默认的
# 在b模式下  不能指定encoding模式
# with open(r"res/a.txt", mode="rt", encoding="utf-8") as f:
#     # t模式会将f.read() 读出的结果自动解码为unicode
#     # 在内存中unicode会和字符进行自动转换
#     res = f.read()
#     print(res)

# b 错误示范
# b 模式不能使用 encoding
# 因为b模式是在硬盘中 内容是什么样子 读出来就是什么样子 不需要进行解码
# 所以不需要进行encoding
# with open(r"a.txt", mode="rb", encoding="utf-8") as f:
#     res = f.read()
#     print(res)


# # b 模式 读取文本内容
# with open(r"a.txt", mode="rb") as f:
#     # 读出的是 b'' 二进制形式的数据
#     # res = f.read()
#     # print(res)
#     # 如果是文本内容 我们可以自己进行decode
#     # 将bytes格式的数据转换为unicode格式
#     # 如果内容不是文本 进行解码会出现错误
#     res = f.read().decode("utf-8")
#     print(res)

# b 模式读取一张图片
# with open('res/mac1.jpeg', mode='rb') as f:
#     # 使用for-in 可以对文件进行一行一行的读取
#     for line in f:
#         print(line)
#         # 对非文本文件的二进制数据进行解码 会报错
#         # print(line.decode('utf-8'))
