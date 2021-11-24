"""
not  非
and 且
or 或
三个逻辑运算符的使用
"""

# not 把后面跟的条件的结果取反
# print(not True)
# print(not 10)
# print(not 10 > 2)
#
# print(not False)
# print(not 0)
# print(not "")
# print(not None)
# print(not ())
# print(not {})

# and 且运算符 只有运算符的结果都为True才为True
# print(10 > 2 and True and False)
# print(False and "100")
# 偷懒原则 如果前面有一个为False那么后面的就不会再继续进行运算 整个结果都为False
# 以下实例到""  才出现结果为False的条件 那么后面的条件就不会再继续的运算
# print(100 and True and "" and 10 and 100 > 2)


# or 或运算符 只要有一个结果为真那么结果就为真
print(3 > 0 or 0)
# or也支持偷懒原则 前面只要有一个结果为True那么后面的条件就不会再继续判断
# 整个结果都为True
print(True or "" or 0 or False)


# 优先级： not > and > or
# 如果多个条件再一起进行混合运算 那么可以使用括号进行括起来进行判断
# 先将not的运算 括起来， 然后将and的运算括起来  然后就会只剩余or的运算了
# res = 3 > 4 and not 4 > 3 or 1 == 3 and 'x' == 'x' or 3 > 3

#            False                      False               False
res = (3 > 4 and (not 4 > 3)) or (1 == 3 and 'x' == 'x') or 3 > 3
print(res)
