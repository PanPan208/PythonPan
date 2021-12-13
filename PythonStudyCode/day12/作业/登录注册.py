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
    用户注册功能 输入用户名判断已经存在重新输入  密码需要两次输入一致
    注册成功将用户名/密码写入到文件中
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
            with open("../res/user.txt", mode="at") as f:
                f.write(f"\n{inp_name}:{inp_pwd}")
                user_info[inp_name] = inp_pwd
            break


# login()
# register()

# 进行登录注册需要的命令编号
msg_info = {0: "退出", 1: "登录", 2: "注册"}

while True:
    msg = """
    0 退出
    1 登录
    2 注册
    """
    print(msg)
    cmd = input('请输入命令编号>>: ').strip()
    if not cmd.isdigit():
        print('必须输入命令编号的数字，傻叉')
        continue

    if int(cmd) not in msg_info:
        print("请输入有效编号!")
        continue

    if int(cmd) == 0:
        print("退出成功")
        break

    if int(cmd) == 1:
        # 登录功能代码（附加：可以把之前的循环嵌套，三次输错退出引入过来）
        login()

    if int(cmd) == 2:
        # 注册功能代码
        register()
