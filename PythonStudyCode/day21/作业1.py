# @time: 2022/1/10 2:58 PM
# Author: pan
# @File: 作业1.py
# @Software: PyCharm

# 1、思考：判断下述说法是否正确
#     题目1：
#     1、应该将程序所有功能都扔到一个模块中，然后通过导入模块的方式引用它们
# 错：
# 封装到一个模块中的功能 应该是一些常用的功能
# 或是一些多次使用的功能

#     2、应该只将程序各部分组件共享的那一部分功能扔到一个模块中，然后通过导入模块的方式引用它们
# 错
# 也可以将一些常用的功能放到模块中

#     题目2：
#     运行python文件与导入python文件的区别是什么？
# 运行python文件和导入python文件都会运行文件中的代码
# 运行python文件不会产生一个文件名的名称空间
# 多次导入同一个python文件只会引入第一次导入产生的名称空间
#     运行的python文件产生的名称空间何时回收，为什么？
# 文件关闭的时候
#     导入的python文件产生的名称空间何时回收，为什么？
