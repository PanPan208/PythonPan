"""
@Author: pan
@Study: file
"""

# windows平台打开一个文件的路径
# open("C:\a\b\.txt")  # error
# 解决方法一： 在前面添加一个r （推荐使用）
# open(r"C:/a/b.txt")
# 解决方法二: 直接将反斜杠改为斜杠
# open("C:/a/b.txt")


# 1 打开文件
# I: 文件路径可以使用绝对路径(Linux/Mac下的格式)
# "/Users/xxx/Desktop/PythonPan/PythonStudyCode/day11/res/a.text"
# II: 也可以使用相对路径 相对于当前文件 "res/a.text"
# 路径前面添加一个r 是raw string 源字符串 不会对\进行转译
# 如果是windows平台最好在字符串前面加上 r
f = open(r'res/a.text', mode='rt')
print(f, type(f))
# <_io.TextIOWrapper name='res/a.text'
# mode='rt' encoding='UTF-8'>
# <class '_io.TextIOWrapper'>


# f只是一个变量 可以指向其他内容
# f = 10
# print(f, type(f))

# 2 读取文件内容
# 读取文件中的内容
# 读取的结果为字符串类型
# 因为model为t模式 所以结果会自动转换为文本
res = f.read()
# print(res)  # 文件中的内容
print(type(res))  # str类型
# <class 'str'>


# 关闭文件
# open的时候 发生了两件事
# 1、f变量指到了 打开文件的内存地址
# 2、在操作系统中打开了文件
# f.close是关闭2中 操作系统中的文件
f.close()

# f变量还是存在的 但是不能再继续操作文件了 因为文件已经关闭了
# print(f)
# res = f.read()  # error
# print(res)


# 使用with 上下文管理器
# 读取一个文件 with结束之后会自动进行close
# 不用我们再亲自调用f.close() 函数了
# with open(r"a.txt", mode="rt") as f1:
#     res1 = f1.readline()
#     print(res1)


# 使用with语句 读取多个文件
# 使用逗号进行分割
with open(r"res/a.txt", mode="rt") as f1, \
        open(r"res/b.txt", mode="rt") as f2:
    res1 = f1.read()
    res2 = f2.read()
    # print(res1)
    # print(res2)
    # close 会自动调用
    # f1.close()
    # f2.close()


# 使用with 在with语句结束的时候 文件是默认自动关闭的
# 可以省略 f.close()
# r = f1.read()
# print(r)
