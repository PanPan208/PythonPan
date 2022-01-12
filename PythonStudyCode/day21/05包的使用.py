# @time: 2022/1/10 5:09 PM
# Author: pan
# @File: 05包的使用.py
# @Software: PyCharm

"""
什么是包：
包就是一个含有__init__.py文件的文件夹

为什么要使用包？
包的本质是模块的一种形式，包是用来被当成模块导入

导入一个包发生的三件事:
1、产生一个包名的名称空间
2、运行包下面的__init__.py文件 并将运行过程中产生的名字都丢到1中的名称空间中
(并不会运行包下面的其他文件)
3、在当前执行文件的名称空间中拿到一个名字mmm 该mmm名字指向1的名称空间
"""

# 导入包名 指名道姓的调用包内部还有的名称
# import mmm
# print(mmm.x)
# print(mmm.y)
# mmm.say()

# 包的导入依然适用form...import
# 单独的导入包内的某一个名称
# from mmm import x
# from mmm import y
# from mmm import say
# print(x)
# print(y)
# say()


# 环境变量是为执行文件准备的
# 所有被导入的模块或者后续的其他文件的引用的sys.path都是参照执行文件的sys.path
# import sys
# print(sys.path)
# ['/Users/izzld/Desktop/PythonPan/PythonStudyCode/day21',
# '/Users/izzld/Desktop/PythonPan/PythonStudyCode', ...
# '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']

# 如果想要使用包mmm下study文件的内容
# 可以在该文件下修改sys.path的环境变量
# 也可以在导入的包的__init__文件中加入包文件的环境变量
# 也可以直接导入 import mmm.study
import sys
sys.path.append(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day21/mmm')
# import mmm
import study
print(study.age)
print(study.name)
study.study()

'''
强调内容：

1、包的导入也可以使用import或者是使用from...import...
无论是使用哪种 凡是导入的时候点的左侧必须是包名
例如： import a.b.c.d.e.f
点前面都是包或子包名

2、在不同的包下面有相同的模块不会冲突
比如在包A和包B下 都有一个mm模块 
A.mm 和 B.mm 来自两个不同的名称空间

3、import导入文件的时候  产生的名称空间名字来源于文件
使用import导入包的时候 产生的名称空间名字同样来源于文件 - 该文件是包下的__init__文件
导入一个包的本质就是导入该文件
'''