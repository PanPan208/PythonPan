# @time: 2021/12/23 4:13 PM
# Author: pan
# @File: 作业.py
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

# 4、基于迭代器的方式，用while循环迭代取值字符串、列表、元组、字典、集合、文件对象
"""
my_str = "Hello"
str_iterator = my_str.__iter__()
while True:
    try:
        print(str_iterator.__next__())
    except StopIteration:
        break


def iter_obj(obj):
    obj_iterator = iter(obj)
    while True:
        try:
            print(next(obj_iterator))
        except StopIteration:
            break


# iter_obj("nihao")
# iter_obj([1, 2, 3, 4, 100])

"""


# 5、自定义迭代器实现range功能
"""
def my_range(start, end, step):
    while start < end:
        yield start
        start += step

  
for i in my_range(1, 20, 2):
    print(i)
"""


# ====================本周选做作业如下====================
# 编写小说阅读程序实现下属功能
# # 一：程序运行开始时显示
#     0 账号注册
#     1 充值功能
#     2 阅读小说


# 二： 针对文件db.txt，内容格式为："用户名:密码:金额",完成下述功能
# 2.1、账号注册
# 2.2、充值功能

# 三：文件story_class.txt存放类别与小说文件路径，如下,读出来后可用eval反解出字典
# {"0":{"0":["倚天屠狗记.txt",3],"1":["沙雕英雄转.txt",10]},"1":{"0":["令人羞耻的爱.txt",6],"1":["二狗的妻子与大草原的故事.txt",5]},}

# 3.1、用户登录成功后显示如下内容，根据用户选择，显示对应品类的小说编号、小说名字、以及小说的价格
"""
0 玄幻武侠
1 都市爱情
2 高效养猪36技
"""

# 3.2、用户输入具体的小说编号，提示是否付费，
# 用户输入y确定后，扣费并显示小说内容，如果余额不足则提示余额不足

# 四：为功能2.2、3.1、3.2编写认证功能装饰器，要求必须登录后才能执行操作

# 五：为功能2.2、3.2编写记录日志的装饰器，日志格式为："时间 用户名 操作(充值or消费) 金额"

# 附加：
# 可以拓展作者模块，作者可以上传自己的作品



