# @time: 2022/1/13 4:08 PM
# Author: pan
# @File: 11run.py
# @Software: PyCharm
import sys
import os

# 执行sys文件 并传入两个参数
# os.system('python3 05sys模块.py "aaaa", "bbbb"')

"""
脚本执行
检索一个文件夹下的所有文件名以及对应文件的大小
包含子文件夹 以及子文件夹下的文件

其他文件运行 或 在终端下运行
os.system('python3 11run.py "/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22"')

"""

print("=========")
# print(sys.argv)
# 1 获取传入的文件夹
file_path = sys.argv[1]
print(file_path)
print("================")


# 2 获取该文件夹下的所有文件列表
# file_list = os.listdir(file_path)
# print(os.listdir(file_path))


# 3 循环遍历文件夹下的所有文件
def get_file_list_size(file_path):
    # 获取文件路径下的所有文件列表
    # listdir需要传入的是一个文件夹的路径
    file_list = os.listdir(file_path)

    for name in file_list:
        # 文件的路径
        name_path = os.path.join(file_path, name)
        # 判断该路径是否是文件
        if os.path.isdir(name_path):
            # 如果是一个文件夹 再次进行循环
            get_file_list_size(name_path)
        else:
            # 如果是一个文件直接打印文件名以及问价大小
            print(f'文件名:{name_path}, 文件大小:{os.path.getsize(name_path)}b')


get_file_list_size(file_path)




