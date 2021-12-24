# @time: 2021/12/22 4:46 PM
# Author: pan
# @File: 02有参装饰器.py
# @Software: PyCharm

"""
需求：
要求认证的时候 可以设置认证的方式
1、文件内账号密码
2、db数据库中的账号密码
3、ldap中的账号密码
"""

# 方式一： 山炮玩法
# 因为语法糖 @auth <==> func = auth(func) 语法糖默认是将函数地址传入auth
# 如果在auth中多添加一个参数 不能使用语法糖
# 而且在使用 index = auth(index, type) 的时候需要多传入一个参数
'''
def auth(func, auth_type):
    def wrapper(*args, **kwargs):
        if auth_type == "file":
            print(">>>>>> 使用的是方式 file")
            res = func(*args, **kwargs)
            return res
        elif auth_type == "db":
            print(">>>>> 使用的是方式 db")
        elif auth_type == "ldap":
            print(">>>>> 使用的是方式 ldap")
    return wrapper


def index(x, y):
    print(f"index: {x}, {y}使用文件中的账号密码")
def home(name):
    print(f"{name} 使用的是db数据库中的认证方式")
def transfer():
    print("使用的是ldap的认证方式")

index = auth(index, "file")
index(10, 20)

home = auth(home, "db")
home("pan")

transfer = auth(transfer, "ldap")
transfer()
'''


# 偷梁换柱之后：
# 1、index的参数是什么样， wrapper的参数就是什么样
# (*args, **kwargs)
# 2、index的返回值是什么样 wrapper的返回值就是什么样
# res = func(*args, **kwargs)
# return res
# 3、index函数的属性是什么样！ wrapper函数的属性就是什么样！
# from functions imports wraps
# @wraps


# 方法二：
# wrapper的参数不能变 为了和func参数进行对应
# deco 的参数也不能变 不然不能使用语法糖
# 由于语法糖的限制 deco 只能传入一个参数=函数地址
# 如果再想传入参数 可以在外层再添加一层闭包
def auth(auth_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            if auth_type == "file":
                print(">>>>>> 使用的是方式 file")
                res = func(*args, **kwargs)
                return res
            elif auth_type == "db":
                print(">>>>> 使用的是方式 db")
            elif auth_type == "ldap":
                print(">>>>> 使用的是方式 ldap")
            else:
                print("不支持的类型")
        return wrapper
    return deco


# @deco 等价于 index = deco(index)
# @deco = @auth("file")
@auth(auth_type="file")
def index(x, y):
    print(f"index: {x}, {y}使用文件中的账号密码")


@auth(auth_type="db")
def home(name):
    print(f"{name} 使用的是db数据库中的认证方式")


@auth(auth_type="ldap")
def transfer():
    print("使用的是ldap的认证方式")


index(1, 2)
home("pan")
transfer()