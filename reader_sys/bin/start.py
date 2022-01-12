# @time: 2022/1/12 10:07 AM
# Author: pan
# @File: start.py
# @Software: PyCharm
"""
项目启动文件
"""

import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)

from core import src

if __name__ == '__main__':
    src.run()

