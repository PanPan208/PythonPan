"""
什么是条件？
可以判断真假的是条件
1、显示的条件 True False
判断之后会得到一个bool值的条件
2、隐式的条件
所有的值都可以当作条件进行使用
其中 0 False "" None () {} 代表的是False 其他代表的都是真
"""

# 如果想要在字符串中显示 {}  可以使用 {{{name}}}
# 不能是{{name}}
# print("my name is {{{name}}}".format(name="pan"))
# 使用\转译符号 转译{ } 没有效果 会报错
# print("my name is \{ {name} \}".format(name="pan"))
# 其他符号可以转译
# print("my name is \'pan\'")
# name = "pan"
# print(f"my name is {{{name}}}")

# 条件语句
# 显示条件
# print(10 > 2)
# print(True)
# is_beautiful = True
# print(is_beautiful)

# 隐式条件
# if 100:
#     print("100 is True")
#
# if {}:
#     print("空字符串是真")
# else:
#     print("===")


# if条件判断
'''
if 条件:
    print
    print
elif 条件2:
    print
    print
elif 条件3:
    print
    print
else:
    print
'''

# if elif else 语句
# score = int(input("请输入您的分数:"))
# if score == 100:
#     print("💯 太棒了")
# elif score >= 90:
#     print(" >= 90 优秀")
# elif score >= 60:
#     print("良好")
# else:
#     print("继续努力")


# if语句
# if 10 > 0:
#     print("单个if语句")


# if else 语句
# res = 10 > 0
# if res:
#     print("10 > 0")
# else:
#     print("error")

# if条件判断和逻辑运算符一起使用
