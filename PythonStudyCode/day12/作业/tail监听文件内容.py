# @time: 2021/12/9 2:21 下午
# Author: pan
# @File: tail监听文件内容.py
# @Software: PyCharm

"""
tail -f access.log 程序实现
tail 可以监听 log文件的内容的变化
"""

import time

# # 1 打开log文件
# with open("../res/access.log", "rt") as f:
#     # 2 循环读取文件line
#     while True:
#         res = f.readline()
#         # 如果读取的内容不为空 说明不是最后一行 有内容
#         if res:
#             print(">>>>>", res, end="")
#         else:
#             # 没有内容 sleep 0.3s之后再进行循环
#             time.sleep(0.3)


# 监听文件内容 实现tail功能
with open("../res/access.log", "rt") as f:
    f.seek(0, 2)  # 移动到最后的位置
    print(f.tell())
    while True:
        res = f.readline()
        # 如果读取的内容不为空 说明不是最后一行 有内容
        if res:
            print(">>>>>", res, end="")
        else:
            time.sleep(0.3)
