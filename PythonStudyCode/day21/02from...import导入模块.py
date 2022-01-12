# @time: 2022/1/10 3:08 PM
# Author: pan
# @File: 02from...import导入模块.py
# @Software: PyCharm

"""
1、直接使用import导入模块
该种方式导入的模块使用的时候必须加上前缀
优点：不会和当前文件中的名称混淆
缺点：使用的时候必须加上前缀

2、使用form...import进行导入模块
该中方式导入也发生了三件事：
1、产生一个模块的名称空间
2、运行模块中的代码 将运行中产生的名字都加入到模块的名称空间中去
3、当前模块会拿到一个名称，该名称和模块名称空间的名称的内存地址一致
优点：使用代码的时候不用再带前缀了
缺点：容易和当前名称空间混淆
"""

# import foo
# print(foo.get())
# foo.change_x()
# print(foo.x)

"""
from foo import x  # x和模块foo中1000的内存地址一致
# from foo import get
# from foo import change_x

print(x)
print(f'02这个文件中x的地址{id(x)}')
# print(get())
# change_x()
print(x)

x = 999  # x的地址改为值999的地址
print(x)
print(f'新的x的id地址{id(x)}')

# 再次导入foo中的x
from foo import x  # x重新指向foo中x新值的地址
print(x)
print(f"foo中修改之后x的地址：{id(x)}")
"""


# 2、可以在一行导入多个名称  但是不推荐使用
# from foo import x, get, change_x

# 3、可以使用 * 将所有的名称进行导入
# from foo import  *
# from socket import  *
# 使用 * 导入的名称 是根据 模块中的 __all__ 变量进行决定的 默认是所有的名称
from foo import *
print(x)
# __all__ 中没有get 所以这里不能调用 get() 了
# print(get())

# 4、给导入的名称取一个别名
from foo import get as g
print(g())  # 等价于 get()
