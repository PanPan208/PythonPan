# @time: 2021/12/16 2:56 PM
# Author: pan
# @File: 作业.py
# @Software: PyCharm

# 1、函数对象优化多分支if的代码练熟
# 2、编写计数器功能，要求调用一次在原有的基础上加一
#     温馨提示：
#         I:需要用到的知识点：闭包函数+nonlocal
#         II:核心功能如下：
#             def counter():
#                 x+=1
#                 return x
#
#
#     要求最终效果类似
#         print(couter()) # 1
#         print(couter()) # 2
#         print(couter()) # 3
#         print(couter()) # 4
#         print(couter()) # 5

def func1():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter

counter = func1()

print(counter())
print(counter())
print(counter())
print(counter())
print(counter())



# ====================周末作业====================
# 编写ATM程序实现下述功能，数据来源于文件db.txt
# 0、注册功能：用户输入账号名、密码、金额，按照固定的格式存入文件db.txt
# 1、登录功能：用户名不存在，要求必须先注册，用户名存在&输错三次锁定，登录成功后记录下登录状态（提示：可以使用全局变量来记录）

# 下述操作，要求登录后才能操作
# 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 2、转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱
# 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
# 4、查询余额功能：输入账号查询余额





