# @time: 2021/12/13 6:29 下午
# Author: pan
# @File: 作业.py
# @Software: PyCharm

# 作业要求：下述所有代码画图以及分析代码执行流程
# 1、以定义阶段为准，先画出名称空间的嵌套关系图
# 2、然后找到调用函数的位置，写出函数调用时代码的执行过程，涉及到名字的查找时，参照1中画好
#    的嵌套图，标明查找顺序，一层一层直到找到位置


# ===================题目一===================
input=333
def func():
    input=444
func()
print(input)  # 333

# ===================题目二===================
def func():
    print(x)
x=111

func()  # 111


# ===================题目三===================
x=1
def func():
   print(x)

def foo():
    x=222
    func()

x = 10
foo()  # 10



# ===================题目四===================
# 3 如果在f1/f2局部没有input名称 直接使用全局的input名称
input=111
def f1():
    def f2():
        # 1 如果f2内部有input名称 直接使用这个local的
        # input=333
        print(input)
    # 2 如果在f1内部有input名称 f2内部没有input名称
    # 直接使用这个enclosing的
    input=222

    f2()

f1()  # 222



# ===================题目五===================
# x=111
# def func():
#     # 报错 引用之后声明x
#     # UnboundLocalError: local variable 'x' referenced before assignment
#     # 未绑定局部变量 在定义名称之前引用了局部变量x
#     # global x
#     print(x)
#     x=222
# func()


# ===================题目六===================
# 全局名称 在全局有效
x = 111
def foo():
    print(x, id(x))

def bar():
    print(x, id(x))

foo()
bar()


# ===================题目七===================
x = 1
def func2():
    func1()

x = 2
def func1():
    print(x)

x = 3

func2()  # 3

"""
# 内置名称空间：...

# 全局名称空间：
x = 3 
func1的内存地址
func2的内存地址

# 局部名称空间：
func1内部：无名称
func2内部：无名称
"""

# ===================题目八===================
# 1、如下全局变量记录了当前登录用户，编写登录功能，
# 一旦用户登录成功，则将全局变量赋值为当前登录的用户名
# login_user=None
# def login():
#     name = input("请输入用户名:").strip
#     if name == "123":
#         global login_user
#         login_user = name
# login()


# 2、针对之前编写的查询余额的功能，添加额外的逻辑：
# 如果用户没有登录，则先执行登录功能






