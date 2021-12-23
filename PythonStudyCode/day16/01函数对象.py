# @time: 2021/12/16 10:22 AM
# Author: pan
# @File: 01函数对象.py
# @Software: PyCharm

"""
可以将函数当成一个变量去使用
直接使用函数名  >>>   也就是函数所在的内存地址
使用函数在后面添加一个小括号  >>>  是调用函数内存地址
"""
# # 例子1
# def func1():
#     pass
#
# f = func1
# # <function func1 at 0x10bd1e430>
# # func1赋值给一个变量f  那么func1和f指向的是同一个内存地址
# print(func1, f)
# # 地址以及id值 都相同
# print(id(func1), id(f))
# # 调用func1 都是返回None
# print(func1(), f())


# # 例子2
# # 函数(函数地址)可以作为一个变量作为函数的参数
# # 也可以直接作为一个函数的返回值
# def get_sum(a, b):
#     return a + b
# sum = get_sum
# print(sum(10, 20))
#
# def func2(f):
#     print(f)
#     return f
#
# func2(sum)
# print(get_sum)
# temp = func2(sum)
# print(temp)


# # 例子3：
# # 函数对象可以作为列表中的元素
# def func3():
#     print("haha")
# l = ["111", 222, func3]
# print(l)
# # 调用列表中的函数对象
# l[2]()
#
# d = {"k1": 1, "fff": func3}
# print(d)
# # 调用字典中的函数对象
# d.get("fff")()



# >>>>>>>>>>>>>>>>>>  函数对象使用的实例  <<<<<<<<<<<<<<<<<<<

def login():
    print("登录成功")

def register():
    print("注册成功")

def transfer_money():
    print("转账功能")

def check_banlance():
    print("查询余额")

def withdraw():
    print("提现功能")

# 使用字典优化if语句：
func_dic = {
    "0": ["退出", None],
    "1": ["登录", login],
    "2": ["注册", register],
    "3": ["转账", transfer_money],
    "4": ["查询余额", check_banlance],
    "5": ["提现功能", withdraw]
}

while True:
    # print("""
    # 0 退出
    # 1 登录
    # 2 注册
    # 3 转账
    # """)
    for k in func_dic:
        print(" {} {}".format(k, func_dic[k][0]))

    # 1、输出操作
    cmd = input("请输入您想要进行操作：").strip()

    # 2、检测是否是数字
    if not cmd.isdigit():
        print("error >>> 请输入数字!")
        continue
    # 3、输入的是不是退出
    if cmd == "0":
        break

    # 4、将if-else语句简化
    if cmd in func_dic:
        # 找到字典中的函数对象直接调用
        func_dic[cmd][1]()
    else:
        print("输入的操作有误...")

    # if-else语句 当操作变的多的时候 代码会很长
    # if cmd == "1":
    #     login()
    # elif cmd == "2":
    #     register()
    # elif cmd == "3":
    #     transfer_money()
    # else:
    #     print("未知功能")
