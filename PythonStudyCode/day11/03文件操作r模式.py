# @time: 2021/12/8 6:31 下午
# Author: pan
# @File: 03文件操作r模式.py
# @Software: PyCharm

"""
r 模式
1、默认如果文件不存在会报错
2、每次打开文件 默认指针都会跳到开始的位置 可以使用seek 调整指针的位置
"""

# 实例1
# with open('res/a.txt', mode='rt') as f:
#     print("第一次读取".center(20, "*"))
#     res = f.read()
#     print(res)
# # 再次读取还是从开头 进行读取
# with open('res/a.txt', mode='rt+') as f:
#     print("第二次读取".center(20, "*"))
#     res = f.read()
#     print(res)
#     f.write("哈哈")


# 实例2
# 一次性 读取
# 不推荐使用 如果是文件内容很大 那么会很卡 比较占用内存
# with open("res/a.txt", mode="rt") as f:
#     print("是否可读:", f.readable())
#     if f.readable():
#         res = f.read()
#         print(res)

# 实例3
# for line in f:
# 一行一行的读取 for line in f 推荐使用
# with open("res/a.txt", mode="rt") as f:
#     for line in f:
#         print(line, end="")


# 实例4
# # readline
# with open("res/a.txt", "rt") as f:
#     # 按行读取 后面可以指定 读取的字符个数
#     # 如果指定的字符个数 大于改行的长度 那么也是只读取改行内容
#     # 不指定字符个数 默认读取该行全部内容
#     # res = f.readline(200)
#     # print(res, end="")
#     # 使用while循环 一行一行的读取 文件中的全部内容
#     while True:
#         res = f.readline()
#         print(res, end="")
#         # 如果res长度为0 说明已经是最后一样了
#         # 推荐使用
#         if len(res) == 0:
#             break
#         # 也可以使用 not res
#         # if not res:
#         #     break


# 实例5
# readlines 会将文件中的内容 每一行的内容作为一个元素 存储到一个列表中
# 不推荐使用 因为如果是文件很大 会很占用内存
# ['美人不是凡胎生\n', '应是仙器灵长成\n', '哈哈哈哈']
# with open("res/a.txt", "rt") as f:
#     res = f.readlines()
#     print(res)

# 实例6
# read(n)
# 指定每次 读取的内容字符个数
with open("res/a.txt", "rt") as f:
    while True:
        res = f.read(3)
        print("=====>", res)
        if not res:
            break

