# @time: 2022/1/10 11:20 AM
# Author: pan
# @File: 作业3.py
# @Software: PyCharm


# 作业：
# 1、编写课上讲解的有参装饰器准备明天默写
"""
def auth(auth_type):
    def outter(func):
        def wrapper(*args, **kwargs):
            if auth_type == "1":
                print("验证方式一")
                print("其他装饰内容")
                res = func(*args, **kwargs)
                return res
            elif auth_type == "2":
                print("验证方式二")
            else:
                print("不支持的验证方式")
        return wrapper
    return outter


# @outter
@auth(auth_type="1")
def index(x, y):
    print("index")

index(1, 2)
"""

# 2：还记得我们用函数对象的概念，制作一个函数字典的操作吗，
# 来来来，我们有更高大上的做法，在文件开头声明一个空字典，
# 然后在每个函数前加上装饰器，完成自动添加到字典的操作
"""
code_dic = {}
# {'index': <function index at 0x107b8d940>, 'home': <function home at 0x107bef5e0>}

def cmd_append_dic(func):
    def wrapper(*args, **kwargs):
        if not code_dic.get(func.__name__):
            code_dic[func.__name__] = func
        res = func(*args, **kwargs)
        return res
    return wrapper

@cmd_append_dic
def index(x, y):
    print(f"index: x = {x}, y = {y}")

@cmd_append_dic
def home(name):
    print(name)

index(10, 20)
home("shangsan")
home("lisi")

print(code_dic)
code_dic["index"](1, 2)
"""


# 3、 编写日志装饰器，实现功能如：一旦函数f1执行，
# 则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
# 注意：时间格式的获取
# import time
# time.strftime('%Y-%m-%d %X')
# string from time
"""
def func_log(file_path):
    def deco(func):
        def wrapper(*args, **kwargs):
            # 在运行func函数之前添加记录日志
            import time
            with open(file_path, "at") as f:
                time_now = time.strftime('%Y-%m-%d %X')
                f.write(f'时间:{time_now}  函数:{func.__name__} run \n')
            res = func(*args, **kwargs)
            return res
        return wrapper
    return deco

@func_log(file_path="log.txt")
def f1(x):
    print(x)

@func_log(file_path="log.txt")
def f2(x, y):
    print("haha")

f1(10)
f1(1)
f2(1, 2)

"""