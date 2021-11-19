"""
用户交互
控制输入的是 input
控制输出的是 print
"""

# input 是Python3.x 之后出现的
# 会将所有的输入内容 全部识别为字符串类型
# 然后赋值给input
# name = input("请输入您的姓名:")
# print(name, type(name))
# age = input("请输入您的年龄:")
# print(age, type(age))


# raw_input 会根据输入的类型 自动识别为用入输入的内容是什么类型
# python3.x 已经舍弃不用
# 对使用者不友好
# name = raw_input("请输入您的年龄")
# name
# age = raw_input("请输入您的年龄:")
# age

# 如果输入的不是数字会转换失败
# age = int(input("请输入您的年龄:"))
# print(age, type(age))


# 字符串的格式化

# 1 使用%进行字符串格式化
# 从Python出现一直就存在
# 匹配多个值
# print("my name is %s, my age is %s" % ("panpan", "20"))
# print("my name is %s, my age is %d" % ("panpan", 20))
# # 匹配单个字符串
# print("my name is %s" % "pan")
# # 匹配字典数组
# print("my name is %(name)s, my age is%(age)s" % {"name": "pan", "age": 10})

# %s 可以匹配任何类型
# print("my name is %s" % "pan")
# print("my name is %s" % 10)
# print("my name is %s" % [10, 20])
# print("my name is %s" % {"name": "pan", "age": 10})
# print("my name is %s" % True)

# %d 只能匹配数字类型
# print("my name is %d" % "pan") # error
# print("my age is %d" % 10)


# 2 使用str的format方法 (推荐使用)
# 直接使用{} 作为一个占位符号
# print("my name is {}, my age is {}".format("panpan", 20))
# {0} 为取format中的第一个元素
# {1} 为取format中的第二个元素
# print("my name is {0}{0}{0}, my age is {0}{1}".format("pan", 10))

# 可以安装key = value的格式进行传值
# {name} 找到format中对应的name 对应的值 放入到 {name} 的位置即可
# print("my name is {name}, my age is {age} {age}".format(name = "pan", age = 100))

#  如果找不到对应的name 会报 keyError错误
# print("my name is {name}".format(age = 10))
# {} 默认是根据index找出format中对应的值， 不能是key = value格式
# print("my name is {}".format(age = 10))

# 进一步 了解
# 对齐填充格式化
# {1:*<10}    {[匹配的字符]:[对齐方式][宽度]}
# *< 左对齐   是将匹配到的字符进行对齐处理   左侧是的姓名是拼接的
# # 姓名      赵*********
# print("姓名{1:*<10}".format("pan", "赵"))
# # *> 右对齐
# # 姓名*********赵
# print("姓名{1:*>10}".format("pan", "赵"))
# # *^ 居中对齐
# # 姓名****赵*****
# print("姓名{1:*^10}".format("pan", "赵"))


# 精度
# .3f 是后面保留三位小数点
# 针对的是整数以及浮点数 如果是其他类型会报错
# print("整数: {0: .2f}".format(23))  # 如果给的是一个整数会保留两位小数
# print("PI is {0: .3f}".format(3.1415926))
# print("薪水是:{salary: .3f}".format(salary = 1000.13923234))


# 进制转换
# 转换为二进制 b
# print("{0:b}".format(123))
# 转换为8进制 o
# print("{0:o}".format(12323))
# 转换为16进制 x
# print("{0:x}".format(15))

# 778,812,399,913,123
# 千分位 每隔三位使用逗号进行分割  只能是用 , 使用其他的会报错
# print("{0:,}".format(778812399913123))
# print("{0:.}".format(778812399913123)) # error


# 3 f  Python3.5之后才推出的一种格式化
# 字符串前面使用一个字母f
# 使用{} 中间直接放入需要放的变量即可
x = input("请输入x:")
y = input("请输入y:")
res = f"my name is {x}, my age is {y}"
print(res)



