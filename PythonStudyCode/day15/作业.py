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
print(input)

# ===================题目二===================
def func():
    print(x)
x=111

func()


# ===================题目三===================
x=1
def func():
   print(x)


def foo():
    x=222
    func()

foo()

# ===================题目四===================
input=111
def f1():
    def f2():
        # input=333
        print(input)
    input=222

    f2()

f1()

# ===================题目五===================
x=111
def func():
    print(x) #
    x=222

func()


# ===================题目六===================
x=111

def foo():
    print(x,)

def bar():
    print(x)

foo()
bar()

# ===================题目七===================
x=1
def func2():
    func1()

x=2
def func1():
    print(x)

x=3

func2()

# ===================题目八===================
# 1、如下全局变量记录了当前登录用户，编写登录功能，一旦用户登录成功，则将全局变量赋值为当前登录的用户名
# login_user=None
# 2、针对之前编写的查询余额的功能，添加额外的逻辑：如果用户没有登录，则先执行登录功能






