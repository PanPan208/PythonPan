# @time: 2021/12/8 6:33 下午
# Author: pan
# @File: 05文件操作a模式.py
# @Software: PyCharm

"""
a 模式  追加模式
如果没有文件 会自动创建一个文件 并写入内容
如果已经存在文件 会直接在文件的最末尾追加数据
"""

# 实例1
# a 追加模式
# 如果没有文件 会进行创建一个文件
# 如果有文件 追加内容 不会清空之前的内容 而是在最后面进行追加内容
# with open(r"res/d.txt", mode="at") as f:
#     f.write("我查勒")


# 实例2
# a+ 可写可读模式
# 如果是a+ 模式 读取内容 默认指针是在最后面
# with open('res/d.txt', mode='a+t') as f:
#     # 默认读取不到内容 因为指针在最后面
#     f.seek(0)
#     res = f.read()
#     print(res)
#     # a 模式追加内容 即使将指针移动到最开始的地方
#     # 在追加写入的时候 还是在最后面
#     f.seek(0)
#     f.write("哈哈")


# 实例3
# b 模式下必须写入的是二进制数据
with open("res/e.txt", mode="ab") as f:
    f.write("你好呀我查勒".encode("utf-8"))
    f.seek(0)
    f.write(b'hello123')
