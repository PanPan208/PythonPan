"""
指定光标位置:
seek: 指针移动的单位都是以bytes/字节为单位的
seek(offset, n)
第一个参数 offset: 偏移字节个数 （一个汉子占三个字节）
第二个参数 n: 是光标起始位置 （默认是开头位置）
0 开头位置
1 当前位置
2 文件末尾 offset从后面开始移动光标 应该是-

# 只有t模式 可以使用 0模式
# b模式 都可以使用
"""

# 实例1
# t 模式可以使用 0模式 seek
# with open("res/a.txt", "rt") as f:
#     f.seek(6, 0)
#     res = f.read(5)
#     print(res)
#     print(f.read(2))


# 实例2
# t模式不能使用 1/2 seek模式
# with open("res/a.txt", mode="rt") as f:
#     r = f.readline()
#     print(r, end="")
#     print(f.tell())  # 告诉指针当前位置
#     f.seek(-6, 2)
#     res = f.read(2)
#     print(res)


# 实例3
with open("res/a.txt", mode="rb") as f:
    res1 = f.readline()
    print(res1.decode("utf-8"))
    f.seek(6, 1)
    res2 = f.read(6)
    print(res2)
    # 因为 仙器 汉字 占用了 6个字节
    # 所有如果是read(n) 不能读取是真个汉字 那么就不能进行decode
    print(res2.decode(encoding="utf-8"))














