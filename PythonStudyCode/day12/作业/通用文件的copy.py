# @time: 2021/12/9 11:03 上午
# Author: pan
# @File: 通用文件的copy.py
# @Software: PyCharm

"""
1、通用文件copy工具实现
可以是文本文件/视频/图片/音频等任意文件 所以应该是b模式
需要输入原始文件的地址
copy文件的路径已经名称
"""


def copy_func():
    res_path = input("请输入源文件路径地址:").strip()
    dis_path = input("请指定copy的文件路径地址:").strip()
    # copy 实现
    with open(r"{}".format(res_path), mode="rb") as f1, \
            open(r"{}".format(dis_path), mode="wb") as f2:
        for line in f1:
            f2.write(line)


copy_func()
