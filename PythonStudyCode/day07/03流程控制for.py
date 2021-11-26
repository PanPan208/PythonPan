"""
for循环语句
for循环是python提供的另一个循环语句
for循环可以做的事 while循环都可以实现
之所以使用for循环是因为在 取值循环的时候 for循环比while循环更加的方便

for循环语法：
for i in 可迭代的对象：
    print
    print

可迭代的对象可以是字符串/list/dic/元组/集合
"""

# ambiguous
# 遍历列表
# 使用for-in循环列表
# list1 = [1, 2, 3, 4, 5]
# for i in list1:
#     print(i)

# 使用while循环太麻烦了
# list1 = [1, 2, 3, 4, 5]
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1

# 使用for-in循环字符串
# for i in "ambiguous":
#     print(i)

# 使用while循环字符串 太麻烦
# name = "pan pan"
# index = 0
# while index < len(name):
#     print(name[index])
#     index += 1

# 使用for循环 遍历字典
# stu = {"name": "pan", "age": 20}
# for key in stu:
#     print(key, stu[key])
#
# for key in stu.keys():
#     print(key)
#
# for value in stu.values():
#     print(value)

# 遍历元组
# for i in (1, 2, 3):
#     print(i)

# for 循环控制循环次数 range
# range(10) 意思是循环10次， 从0-9
# 左边闭合右侧开
# 从0开始
# for i in range(10):
#     print(i)

# 指定开始index
# for i in range(1, 10):
#     print(i)

# 指定开始1-结束10以及步间距2
# for i in range(1, 10, 2):
#     print(i)

# 退出for循环的方式只有一种 break
# for i in range(1, 10):
#     if i == 7:
#         break
#     print("i = ", i)

# continue跳出本次循环 和 while循环一样
# for i in range(1, 10):
#     if i == 8:
#         continue
#     print("i = ", i)

# for-else语句 与 while循环一致
# for i in range(1, 10):
#     print(i)
#     if i == 100:
#         break
# else:
#     # 如果是由于break退出了for循环 else语句不会执行
#     print("循环结束")

# 例子
# for i in range(3):
#     input_name = input("请输入您的姓名:")
#     input_pwd = input("请输入您的密码:")
#     if input_name == "pan" and input_pwd == "123":
#         print("登录成功")
#         break
# else:
#     print("输入错误次数太多!")

# print("hello %s" % "pan")
# print("hello", "world", "pan")
# print("hello\n")
# print("pan")
# 如果end后面跟的是"" 那么不会换行
# print("hello", end="")
# print("pan")
# end="*" 不进行换行 使用*进行分割上下行内容
# print("hello", end="*")
# print("pan")
