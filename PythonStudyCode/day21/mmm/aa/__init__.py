# @time: 2022/1/11 3:30 PM
# Author: pan
# @File: __init__.py.py
# @Software: PyCharm

# 使用aa包内的模块以及包模块
# import f1
# f1.f1()

# # 调用当前包的子包模块
# from aaa import test
# test.ttt()
# from aaa.test import ttt
# ttt()


# 使用相对导入 不能跨出该包
# 包内模块之间的导入 推荐使用相对导入
# from ..bb.f3 import f3 as f
# from ..bb.f3 import x
# f()
# print(x)

# 绝对导入没有包的限制 所以绝对导入会比较通用一些