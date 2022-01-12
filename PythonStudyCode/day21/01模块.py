# @time: 2021/12/27 5:26 PM
# Author: pan
# @File: 01模块.py
# @Software: PyCharm

"""
模块： 模块就是一系列功能的集合体 可以分为三大类
1、内置模块
2、第三方模块
3、自定义模块
     ps： 一个python文件本身就是一个模块 文件名foo.py  模块就是foo

ps： 模块的四种形式：
1、使用Python编写的 .py文件
2、已被编译为共享库或DLL的C或C++扩展
3、把一系列的模块组织到一起的文件夹
文件夹下有一个 __init__.py的文件 该文件称之为包文件
4、使用C语言编写并链接到Python解释器的内置模块


为什么要使用模块呢？
1、拿来主义  内置模块和第三方模块可以直接拿来使用  这种拿来主义极大的提升了开发的效率
2、自定义模块
    可以将代码中的各部分功能提取出来放到一个模块中供大家使用
    好处是减少了代码冗余，程序组织结构更加的清晰

"""

# 模块的使用
import foo

# 一、首次导入模块 发生了三件事情
# 1、执行foo.py 文件中的代码
# 2、会产生一个foo的名称空间, 并将foo.py运行过程中产生的名字都丢到该名称中间中
# 3、在当前文件会产生一个名字foo，该名字会指向步骤2中产生的名称空间的地址

# 之后导入相同的模块 不会重复执行foo.py文件中的代码 而是会直接引用foo的名称空间
# 防止重复引入
# import foo
# import foo

# 引用模块中的变量、方法
# 直接使用 模块.名称
print(foo.x)
print(foo.get())
x = 9999
# 强调1：使用模块.名称 指名道姓的调用模块中的变量 不会和当前文件中的变量产生冲突
# 强调2：无论是调用还是修改都是对模块中的值 进行操作， 与当前文件无关
foo.change_x()
print(foo.x)
print(f"当前文件的x = {x}")


# 二、可以使用逗号进行一次导入多个模块
# 不推荐使用
# import time, sys, foo
# # 建议使用以下方式进行导入多个模块
# import time
# import sys
# import foo

# 三、导入多个不同模块的规范
# 先 内置模块
# 再 中间是第三方模块
# 然后 最后是自定义模块
# import time
# import sys
#
# import requests 第三方模块1
# import requests2 第三方模块2
#
# import foo 自定义模块1
# import bar 自定义模块2


# 4、可以对导入的模块取一个别名
# 如果一个模块的名字很长 或者是有名称冲突的时候 可以取一个别名
# import foo as f
# f.x
# f.get()
# f.change_x()


# 5、模块是第一类对象
# 6、自定义模块的名称一般使用纯小写以及下划线组合的方式进行命名
# 7、也可以在函数内部进行导入模块
def func():
    import foo
    print(foo.x)

# 8、一个python的文件的几种用途！
# 一：被当成程序执行
# 二：被当成模块导入
# 两者的区别是什么？
