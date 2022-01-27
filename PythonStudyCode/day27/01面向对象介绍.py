# @time: 2022/1/27 2:37 PM
# Author: pan
# @File: 01面向对象介绍.py
# @Software: PyCharm
"""
面向过程：
核心是过程两字
过程的终极奥义就是将程序流程化
过程就是'流水线' 用来一步一步的解决问题
优点==== 将复杂的程序简单化
缺点==== 一个程序只能用来解决一个问题，即使能解决其他问题也要进行大改


面向对象：
核心是对象两次
对象的终极奥义就是将程序整合
对象就是'容器' 用来盛放数据和功能的
优点====== 解决了程序的扩展性
缺点====== 编程的复杂度远高于面向过程

类也是'容器'，该容器用来存放'同类'对象共有的数据和功能

程序 = 数据 + 功能

现实生活中：现有对象后有类
编程中：先有类 后有对象
"""


'''
# 面向过程
stu_school = "old boy"
stu_name = "张三"
stu_age = 20
stu_gender = "male"

def set_stu_info(x, y, z):
    global stu_name, stu_age, stu_gender
    stu_name = x
    stu_age = y
    stu_gender = z

def get_stu_info():
    print(f"学生名字:{stu_name}, 学成年龄:{stu_age}, 学成性别:{stu_gender}")

get_stu_info()
set_stu_info("lisi", 30, "female")
get_stu_info()

'''


def set_stu_info(stu_obj, x, y, z):
    stu_obj["stu_name"] = x
    stu_obj["stu_age"] = y
    stu_obj["stu_gender"] = z


def get_stu_info(stu_obj):
    print(f"学生名字:{stu_obj['stu_name']}, "
          f"学成年龄:{stu_obj['stu_age']}, "
          f"学成性别:{stu_obj['stu_gender']}")


# 一个盒子 存放数据和功能
# 功能还是没有和数据一起放到一起
stu_obj = {
    "stu_school": "old boy",
    "stu_name": "zhang san",
    "stu_age": 19,
    "stu_gender": "male",
    "set_stu_info": set_stu_info
}

stu_obj2 = {
    "stu_school": "old boy",
    "stu_name": "li si",
    "stu_age": 20,
    "stu_gender": "female",
    "set_stu_info": set_stu_info
}

print(stu_obj)
print(stu_obj2)







