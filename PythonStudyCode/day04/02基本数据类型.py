"""
数字类型： 整形Int 浮点型Float
"""
# age = 20
# print(type(age))
# <class 'int'>

# salary = 1000.2
# print(type(salary))
# <class 'float'>

# print(10 + 3.132)
# print(10 - 10.123)
# print(10 * 23.1)
# print(100/23.3)
# 20.122999999999998
# 整数可以和小数进行运算 运算结果为float类型


# 2、字符串类型
# 可以使用 ''  ""  ''''''  """""" 进行定义
# info = """
# Helo
# world
# """
# print(type(info))
# <class 'str'>
# str 类型
# x = "1fdf"
# print(type(x))
# <class 'str'>
# 由数字组成的字符串 是字符串类型

# 如果想要再字符串中打印引号 可以使用转译符号 \'
# print("my name is \'zhappan\'")
# print('my name is \"zhappan\"')

# 字符串之间的相加
# 不推荐使用 + 因为字符串之间的拼接使用+的效率很低
# print("my name is " + "panpan")
# print("="*30)
# print("HelloWorld")
# print("="*30)

# 3 列表
# 类表默认的索引是从0开始的
# 定义使用 [] 内用逗号多个任意的值，其中的一个值称之为一个元素
arr = [1, 2, 3, 4, 5, 6]
# print(type(arr))
# <class 'list'> 类型是list
# print(arr)
# print(arr[0])  # 0
# print(arr[2])  # 3
# print(arr[10])  # list index out of range
#  len(arr) 获取列表的长度
# print(arr[len(arr) - 1])
# print(arr[-1])  # 6
# print(arr[-2])  # 5
# -1 是从后向前的第一个元素


# 4、字典类型
dic = {
    "name": "panpan",
    "age": 20,
    "salary": 1000.2,
    "gender": True
}
# print(type(dic))
# <class 'dict'>  类型是dict
# print(dic["name"])
# print(dic["age"])
# print(dic["lisi"])
# 如果没有对应的key 那么会报错 KeyError

# if dic.__contains__("lisi") {
#     print(dic["lisi"])
# }


# 5 布尔值 True/False
# Python是大小写敏感的
# 用于记录事物的两种状态

is_ok = True
print(is_ok)
is_ok = False
print(is_ok)
print(type(is_ok))
# <class 'bool'>

# 通常用于做条件判断

