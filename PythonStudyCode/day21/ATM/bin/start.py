# @time: 2022/1/10 6:04 PM
# Author: pan
# @File: start.py
# @Software: PyCharm

'''
import sys
print(sys.path)

# 绝对导入 = sys.path = 执行文件
sys.path.append(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day21/ATM')


from conf import setting
from core import src

print(setting)
print(src)
src.run()
'''


# 优化方案：

# 当前文件的绝对路径
# print(__file__)

import os
import sys

# 获取某文件所在的文件夹绝对路径
# print(os.path.dirname(__file__))

# 获取ATM文件夹所在的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 将ATM包的路径添加到环境变量中去
sys.path.append(BASE_DIR)

print(sys.path)

from core import src

if __name__ == '__main__':
    src.run()
