# @time: 2022/1/27 5:05 PM
# Author: pan
# @File: 03属性查找.py
# @Software: PyCharm

class Student:
    stu_school = "old boy"
    init_count = 0

    # 定义函数 第一个参数都是self
    # 使用类名调用 需要传入第一个对象参数
    # 使用对象进行调用方法 第一个参数会默认为该对象
    def __init__(self, name, age, gender):
        Student.init_count += 1
        self.name = name
        self.age = age
        self.gender = gender

    def set_stu_info(self, x, y, z):
        self.name = x
        self.age = y
        self.gender = z

    def get_stu_info(self):
        print(f"姓名:{self.name}, 年龄:{self.age}, 性别:{self.gender}")


stu1 = Student("张三", 20, "male")
# print(stu1.init_count)
stu2 = Student("里斯", 21, "female")
# print(stu2.init_count)
stu3 = Student("王武", 22, "male")
# print(stu3.init_count)
# print(Student.init_count)

# # 类中的属性共享给所以的对象用的 类似静态变量 是共有的
# print(id(Student.stu_school))
# print(id(stu1.stu_school))
# print(id(stu2.stu_school))
# print(id(stu3.stu_school))
#
# # 使用Student进行修改 所有的对象都会修改
# Student.stu_school = "1111"
# print(Student.stu_school)
# print(stu1.stu_school)
# # 只修改对应的对象的属性值 只会修改该对象的属性值
# stu1.stu_school = "22222"
# print(stu1.stu_school)
# print(stu2.stu_school)
# print(stu3.stu_school)
# print(Student.stu_school)

# 类调用自己的函数 必须按照函数的用法来
# Student.get_stu_info(stu1)
# Student.set_stu_info(stu1, "didi", 100, "male")
# Student.get_stu_info(stu1)
# Student.get_stu_info(stu2)

# 使用对象进行调用 会将对象自身作为第一个参数进行传入
stu1.get_stu_info()
stu1.set_stu_info("王武", 100, "male")
stu1.get_stu_info()


# 列表类似类的使用
l1 = [111, 222, 333]
print(l1)
l1.append("ddd")
print(l1)
list.append(l1, "ahaha")
print(l1)
