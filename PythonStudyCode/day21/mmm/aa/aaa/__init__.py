# @time: 2022/1/11 3:37 PM
# Author: pan
# @File: __init__.py.py
# @Software: PyCharm


# import test
# test.ttt()

# from .test import ttt
# ttt()

# 使用绝对导入 包之外的模块
import sys
sys.path.append(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day21/mmm/aa')
print(sys.path)

import f1
import f2
f1.f1()
f2.f2()
