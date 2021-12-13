# @time: 2021/12/10 9:53 上午
# Author: pan
# @File: 01文件修改.py
# @Software: PyCharm

"""
文件中的内容不能直接进行修改，如果write的话都是覆盖
文件修改的两种方式
1、打开文件到内存中进行修改 然后对该文件进行修改
2、使用一个copy文件进行临时过渡修改
"""

# with open("res/d.txt", mode="r+t") as f:
#     res = f.read()
#     print(res)
#     f.seek(0)
#     f.write("你好")
#     f.seek(0)
#     print(f.read())

# 第一种方式： 文本编辑器的思路
# 将文件内容一次性全部读入到内存 然后在内存中修改之后 再重新写入到文件中
# 优点：修改过程中同一份数据只有一份
# 缺点：因为是将文件内容读入到内存 所以会占用内存
# with open("res/d.txt", mode="rt") as f1:
#     res = f1.read()
#     re_data = res.replace("你好", "已经修改后的数据")
#     print(re_data)
# with open("res/d.txt", mode="wt") as f2:
#     f2.write(re_data)


# 第二种方式：
# 需要使用到os库
# 对文件中的内容修改之后存储到新建的文件中 for line in f
# 修改之后将源文件删除 将新文件改为之前的源文件名称
# 优点：不会太占用内容 因为是使用for line in f
# 缺点：文件修改过程中 同一份数据存储了两份 多占用了硬盘空间
import os
with open("res/d.txt", mode="rt") as f1, \
        open("res/.d.txt.swap", mode="wt") as f2:
    for line in f1:
        f2.write(line.replace("你好", "哈哈哈哈哈哈哈啊哈"))
# 文件修改之后 移除源文件
# 对修改后的文件进行修改名称
os.remove("res/d.txt")
os.rename("res/.d.txt.swap", "res/d.txt")

