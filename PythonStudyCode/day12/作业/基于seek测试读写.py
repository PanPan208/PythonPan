# @time: 2021/12/9 11:45 上午
# Author: pan
# @File: 基于seek测试读写.py
# @Software: PyCharm

"""
基于seek控制指针移动，测试r+、w+、a+模式下的读写内容
"""

# r+
# with open("../res/a.txt", mode="r+b") as f:
#     # read()之后 指针会移动后最后面
#     res = f.read()
#     print(res.decode("utf-8"))
#     # 如果再想读取内容 需要移动指针
#     f.seek(0)
#     print("再次读取", f.read())
#     f.seek(0)
#     f.write("测试".encode("utf-8"))
#     f.seek(0)
#     print(f.read(6).decode("utf-8"))

# w+
# with open("../res/b.txt", mode="w+b") as f:
#     # 如果有文件 会先清空文件 然后写入 哈哈哈
#     f.write("哈哈哈".encode("utf-8"))
#     # tell = 9
#     # 一个汉字占3个字节  三个汉字就是9个字节
#     print(f.tell())
#     # 写入文件之后 指针在文件末尾
#     # 读取内容为空
#     res = f.read()
#     print(res)
#     # 从文件末尾向前面 移动3个字节 也就是一个汉字
#     f.seek(-3, 2)
#     # 哈
#     print(f.read().decode("utf-8"))


# a+
with open("../res/c.txt", mode="a+b") as f:
    f.write(b"aaa\n")
    f.write(b"bbb\n")
    print(f.read())  # b''
    f.seek(0)
    # 可以读取全部内容
    print(f.read().decode("utf-8"))
    # a模式 不管指针在什么地方 在写入内容的时候都是在末尾进行 添加内容
    f.seek(0)
    f.write("哈哈".encode("utf-8"))
    # 再次从开始位置进行读取内容
    f.seek(0)
    print(f.read().decode("utf-8"))
