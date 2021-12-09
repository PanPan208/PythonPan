# @time: 2021/12/9 4:10 下午
# Author: pan
# @File: 登录注册.py
# @Software: PyCharm

"""
# 1：编写用户登录接口
# 2：编写程序实现用户注册后（注册到文件中），可以登录（登录信息来自于文件）
"""

# 用户存放用户信息
user_info = {}

# 将文件中的内容 读取到内存的字典中
with open("../res/user.txt", mode="rt") as f:
    for line in f:
        name, pwd = line.strip().split(":")
        user_info[name] = pwd
    print("用户信息:", user_info)


def valid_user(name):
    """
    判断输入的用户名是否在字典中
    :param name: 用户名
    :return: 返回是否在
    """
    if user_info.get(name):
        return True
    else:
        return False


def login():
    """
    登录功能
    :return:
    """
    flag = True
    while flag:
        inp_name = input("请输入用户名:").strip()
        if not valid_user(inp_name):
            print("输入的用户名不存在，请重新输入>>>")
            continue

        while True:
            inp_pwd = input("请输入密码:").strip()
            if not inp_pwd.isdigit():
                print("请输入数字密码>>>")
            else:
                # 判断密码是否正确
                user_pwd = user_info[inp_name]
                if user_pwd == inp_pwd:
                    print("恭喜您！登录成功")
                    flag = False
                    break
                else:
                    print("密码错误, 请重新输入>>>")


def register():
    """
    用户注册功能
    :return:
    """
    while True:
        inp_name = input("请输入用户名:").strip()
        if valid_user(inp_name):
            print("用户名已经存在, 请重新输入用户名>>>")
            continue

        inp_pwd = input("请输入密码:").strip()
        confirm_pwd = input("请再次输入密码:").strip()
        if inp_pwd == confirm_pwd:
            print("注册成功")
            # 将用户名/密码写入到user文件中
            with open("../res/user.txt", mode="at") as f:
                f.write(f"\n{inp_name}:{inp_pwd}")
            break



# login()
register()