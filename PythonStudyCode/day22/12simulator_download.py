# @time: 2022/1/13 5:23 PM
# Author: pan
# @File: 12simulator_download.py
# @Software: PyCharm
"""
模拟一个下载进度条

"""

# print('[%-80s]' % '#')
# print('[%-80s]' % '######')

import time

'''
res = ''
for i in range(50):
    res += '#'
    time.sleep(0.05)
    # \r 每次从头开始打印
    print('\r[%-50s]' % res, end='')
'''

# 模拟一个文件下载进度
total_size = 1000000
rece_size = 0


def print_precent(precent):
    """
    打印下载进度条
    :param precent:
    :return:
    """
    if precent >= 1:
        precent = 1
    res = int(precent * 50) * '#'
    print('\r[%-50s] %d%%' % (res, int(precent*100)), end='')


while rece_size < total_size:
    # 模拟下载小号的时间
    time.sleep(0.01)
    # 模拟已经下载的size
    rece_size += 1024
    # 下载的内容占总内容的多少百分比 [0, 1]
    precent = rece_size / total_size
    print_precent(precent)



