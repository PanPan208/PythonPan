# @time: 2021/12/20 2:34 PM
# Author: pan
# @File: 作业.py
# @Software: PyCharm

import time

# 一：编写函数，（函数执行的时间用time.sleep(n)模拟）
'''
def index(x, y):
    time.sleep(3)
    print("this is index method: %s %s" % (x, y))
index(10, 20)
'''

# 二：编写装饰器，为函数加上统计时间的功能
'''
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return res
    return wrapper

@timer
def index(x, y):
    time.sleep(3)
    print(f"index method x = {x}, y = {y}")

# index = timer(index)
# index(10, 20)
'''


# 三：编写装饰器，为函数加上认证的功能
"""
login_name = None


def login():
    while True:
        inp_name = input("请输入用户名:").strip()
        inp_pwd = input("请输入密码:").strip()
        if inp_name == "pan" and inp_pwd == "123":
            print("登录成功")
            global login_name
            login_name = inp_name
            break
        else:
            print("登录失败")


def login_auth(func):
    def wrapper(*args, **kwargs):
        if not login_name:
            login()
        res = func(*args, **kwargs)
        return res
    return wrapper


@login_auth
def index(x, y):
    time.sleep(2)
    print("index x = {}, y = {}".format(x, y))


index(10, 20)
"""


# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，
# 可以用eval('{"name":"egon","password":"123"}')转成字典格式


# 五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，
# 在超时时间内无需重复登录，超过了超时时间，则必须重新登录


is_login = False
user_info = {}
end_timer = 0

# 获取文件中的用户信息
with open("user_db.txt", mode="rt") as f:
    res = f.read()
    # 使用eval将字符串格式转换为数据本身对应的数据类型
    user_info = eval(f"{{{res}}}")
    print(user_info, type(user_info))


# 登录
def login():
    while True:
        inp_name = input("请输入用户名:").strip()
        inp_pwd = input("请输入密码:").strip()
        # 如果输入的用户名密码和本地文件中存储的用户名密码一致 登录成功
        if inp_name == user_info.get("name") and inp_pwd == user_info.get("password"):
            print("登录成功")
            # 登录成功将登录状态改为True
            global is_login
            is_login = True
            break
        else:
            print("登录失败")


# 登录授权装饰器 授权一次一直有效
def login_auth(func):
    def wrapper(*args, **kwargs):
        if not is_login:
            login()
        res = func(*args, **kwargs)
        return res
    return wrapper


# 为index函数添加登录授权装饰器
# @login_auth
# def index(x, y):
#     time.sleep(2)
#     print("index x = {}, y = {}".format(x, y))
#
# index(10, 20)


# 一定时间内有效装饰器  在有效时间内 登录有效
def timer_auth(func):
    def wrapper(*args, **kwargs):
        global end_timer
        print(f"到期时间:{end_timer}, 当前时间是:{time.time()}")
        if end_timer > time.time():
            print("已经授权过！")
        else:
            login()
            end_timer = time.time() + 10  # 设置超时时间10s后到期
            print(f">>>到期时间设置为:{end_timer}")
        res = func(*args, **kwargs)
        return res
    return wrapper



# @login_auth
@timer_auth
def index(x, y):
    print("index 运行中...")
    time.sleep(6)
    print("index x = {}, y = {}".format(x, y))

index(10, 20)
index(20, 30)
index(30, 40)
index(50, 60)
