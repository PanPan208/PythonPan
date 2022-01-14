# @time: 2022/1/11 4:52 PM
# Author: pan
# @File: start.py
# @Software: PyCharm

import os
import sys

# 将reader路径 添加到环境变量
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
print(sys.path)

from core import src


if __name__ == '__main__':
    src.run()


