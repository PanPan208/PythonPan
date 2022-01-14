# @time: 2022/1/13 5:45 PM
# Author: pan
# @File: 13copy_file.py
# @Software: PyCharm
"""
文件copy脚本

执行脚本 会进行文件的copy  传入需要copy的文件路径 以及copy的位置
python 13copy_file.py res_file dis_file
"""

import sys
import shutil


def run():
    # 执行脚本的时候需要传入两个参数
    # 如果不是传入两个参数 直接return
    if len(sys.argv) != 3:
        return

    res_file = sys.argv[1]
    dis_file = sys.argv[2]
    print(res_file)
    print(dis_file)

    # 方式一： 进行copy
    # with open(r'%s' % res_file, mode='rb') as r_f, \
    #         open(r'%s' % dis_file, mode='wb') as w_f:
    #     for line in r_f:
    #         w_f.write(line)

    # 方式二 进行copy
    # 也可以使用shutil进行文件copy
    shutil.copyfile(res_file, dis_file)


run()

