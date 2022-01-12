# @time: 2022/1/10 4:11 PM
# Author: pan
# @File: 03模块的搜索路径优先级.py
# @Software: PyCharm

"""
无论是使用import 还是 使用from...import 在导入模块的时候都涉及到查找问题
查找优先级：
1、内存中：（内置模块 Python自带的模块）
2、硬盘： 即按照sys.path中存放的文件的顺序依次查找要导入的模块
"""

import sys
print("=====")
# sys.path 值为一个列表 列表中存放的是一系列的文件夹路径
# 其中第一个文件夹的路径为当前文件所在的文件夹路径
print(sys.path)

# 因为模块foo在当前文件夹内 所以可以直接导入 可以找到
# import foo
# foo.get()
#
# print("time is runing...")
# import time
# time.sleep(5)
#
# 因为foo已经被导入过一次 再次导入会使用命名空间中已经存在的foo
# import foo
# foo.get()


'''
import foo
# modules是系统中已经存在的模块 (包括内置模块以及导入的模块)
# 是一个字典 key是模块的名称
print("foo" in sys.modules)
print(sys.modules)
'''

# 因为bar所在的文件不在系统的path中 所以不能导入模块bar
# import bar

# 将bar模块所在的文件夹或包路径添加到系统的path中
# 这样就可以在当前文件中导入对应的bar模块了
# 使用绝对路径 这样写写死了 可以使用os模块进行优化
sys.path.append(f'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day21/mm')
print(sys.path)

# 可以使用了
# import bar
# bar.say()
# from bar import say
# say()

