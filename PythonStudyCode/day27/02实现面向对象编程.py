# @time: 2022/1/27 3:07 PM
# Author: pan
# @File: 02实现面向对象编程.py
# @Software: PyCharm
"""
定义类：
类是对象中的 相似数据和相似功能的结合体
程序 = 数据 + 功能
类 = 变量 + 函数

"""


# 1、类的定义使用class进行定义
# 2、类名使用的驼峰命名法 进行命名
# 3、类中可以存放数据和功能 也可以包含任何代码
# 4、类的代码在类定义的时候 就会立即执行 并产生类的命名空间
"""
class Student:
    # 数据定义
    stu_school = "old boy"

    # 功能定义
    def set_stu_info(stu_obj, x, y, z):
        stu_obj.stu_name = x
        stu_obj.stu_age = y
        stu_obj.stu_gender = z
        #
        # stu_obj["stu_name"] = x
        # stu_obj["stu_age"] = y
        # stu_obj["stu_gender"] = z

    def get_stu_info(stu_obj):
        print(f"学生名称:{stu_obj.stu_name}, "
              f"学生年龄:{stu_obj.stu_age}, "
              f"学生性别:{stu_obj.stu_gender}")

    # print("============>")
"""

# __dict__ 获取类中所有的所有数据
# 返回的是字典类型 既然是字典可以通过[""] 进行调用该字典中的数据
# print(Student.__dict__)
# print(Student.__dict__["stu_school"])
# print(Student.__dict__["set_stu_info"])
# print(Student.__dict__["get_stu_info"])


# 对于__dict__ 都可以转换为使用 点 进行调用
# print(Student.stu_school)
# print(Student.set_stu_info)
# print(Student.get_stu_info)


# Student.stu_name = "lisi"
# Student.stu_age = 10
# Student.stu_gender = "male"
# print(Student.__dict__)
# Student.set_stu_info(stu_obj1, "hah", 10, "male")
# Student.get_stu_info(stu_obj1)


# 使用类产生一个对象
#
# stu_obj1 = Student()
# print(stu_obj1)
# print(stu_obj1.__dict__)
# stu_obj1.name = "shang san"
# print(stu_obj1.name)
# stu_obj1.age = 20
# stu_obj1.gender = "male"
# print(stu_obj1.__dict__)

# stu_obj1.set_stu_info("lisi", 20, "female")
# stu_obj1.get_stu_info()


# 优化Student
class Student:
    # 数据定义
    stu_school = "old boy"

    # 对对象进行初始化
    # 1 会在调用类时自动触发该方法 用来初始对象独有的数据
    # 2 __init__ 存放的是对象初始化属性的功能 但是也可以存放其他任何代码
    # 3、该方法的返回值只能是None
    def __init__(self, x, y, z):
        self.stu_name = x
        self.stu_age = y
        self.stu_gender = z

    # 功能定义
    def set_stu_info(stu_obj, x, y, z):
        stu_obj.stu_name = x
        stu_obj.stu_age = y
        stu_obj.stu_gender = z

    def get_stu_info(stu_obj):
        print(f"学生名称:{stu_obj.stu_name}, "
              f"学生年龄:{stu_obj.stu_age}, "
              f"学生性别:{stu_obj.stu_gender}")

    # print("============>")


# 调用类的过程称为实例化
# 1、先产生一个空对象
# 2、然后python会自动调用__init__方法
# 然后会将空对象以及括号中传入的参数一并传入__init__方法
# 3、返回初始完成的对象
stu_obj = Student("pan", 20, "male")
print(stu_obj.__dict__)
print(stu_obj.stu_name)
stu_obj.get_stu_info()

stu_obj.set_stu_info("弟弟", 10, "male")
print(stu_obj.stu_name)
stu_obj.get_stu_info()




