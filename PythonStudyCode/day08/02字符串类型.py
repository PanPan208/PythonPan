"""
字符串类型
字符串有很多内置方法
"""

# msg = "hello"
# msg = str("hello")
# print(msg, type(msg))

# str可以将任何类型 都转换为字符串
# res = str([1, 2])
# res = str(True)
# res = str(100)
# res = str({"name": "pan"})
# print(res, type(res))

# 内置方法
# 1 正向/方向取值
# msg = "hello world"
# 正数 正向取  从0开始
# print(msg[0])
# print(msg[4])
# 负数 反向取 从-1开始
# print(msg[-1])
# index out of range 下标越界
# print(msg[100])
# 下标最大为 len(msg) - 1
# print(msg[len(msg) - 1])

# 只能取 不能改
# 不能对对应的位置设置值
# 因为str类型是不可变的类型
# msg[0] = "haha"


# 2 切片取
# msg = "hello world"
# 取0-5之间的子字符串 (顾头不顾尾)
# print(msg[0:5])  # hello
# 取的是0-5之间的数  步长为2
# 0 2 4
# print(msg[0:5:2])  # hlo
# 反向取
# print(msg[3:0:-1])  # lle  可以取到3 取不到0
# 倒着取值， 3 2 1  取完之后反转

# 全部取出来
# print(msg[:])
# hello world
# 全部取出来 然后反向
# print(msg[::-1])
# dlrow olleh

# 3 字符串长度
# msg = "hello world"
# print(len(msg))

# 4 in 和 not in
# msg = "hello world"
# print("hell" in msg)
# print("h" not in msg)
# print(not "hee" in "hello workd")  # 不推荐使用


# 5 移除字符串两端的空格
# 默认是去掉空格
# msg = "    hello world  "
# print(msg.strip())
# print(msg.lstrip())
# print(msg.rstrip())

# 可以指定去掉字符串两端的字符
# msg = "****hello world***"
# print(msg.strip("*"))
# print(msg.lstrip("*"))
# print(msg.rstrip("*"))

# 应用：
# while True:
#     input_name = input("请输入您的姓名:").strip().lower()
#     input_pwd = input("请输入密码:").strip().lower()
#     if not input_pwd.isdigit():
#         print("密码为数字类型")
#         continue
#
#     if input_name == "pan" and input_pwd == "123":
#         print("登录成功")
#         break
# print("=======end")

# 6 拆分字符串为一个列表  split
# 把一个字符串根据某个分割符进行分割 得到一个列表
# 默认使用的分割符是空格
# msg = "my mame is pan"
# print(msg.split())
# print(msg.rsplit())

# 根据指定的字符串进行分割
# msg = "my*mame*is*pan"
# print(msg.split("*"))
# # ['my', 'mame', 'is', 'pan']
# # 从左侧指定分割次数
# print(msg.split("*", 2))
# # ["my", "name", "is*pan"]
# # 从右侧开始分割 分割两次
# print(msg.rsplit("*", 2))
# # ["my*name", "is", pan]
# # 将整体作为一个元素
# print(msg.splitlines())
# # ['my*mame*is*pan']


# # # 7 大小写转换
# msg = "AAAbbCCcccDDDddd"
# upper_msg = msg.upper()
# print(upper_msg)
# print(upper_msg.isupper())
# lower_msg = msg.lower()
# print(lower_msg)
# print(lower_msg.islower())


# # 8 是否以某个字符串开头 某个字符串结尾
# msg = "my name is pan"
# print(msg.startswith("my"))
# print(msg.startswith("pan"))
# print(msg.endswith("pan"))
# print(msg.endswith("pans"))

# # 9 将一个列表拼接成一个字符串 join
# # 如果拼接一个列表 列表中只能是字符串类型
# myList = ["my", "name", "is", "100"]
# # 一个一个拼接  太麻烦
# res1 = myList[0] + ":" + myList[1] + ":" + myList[2] + ":" + myList[3]
# print(res1)
# # 使用join进行拼接
# # "*" 是进行元素拼接的字符串
# res = ":".join(myList)
# print(res)

# error
# 如果要将一个列表拼接成一个字符串，那么这个列表中只能有str类型
# 不能有其他类型 也不能包含子列表
# res2 = [["123", "a"], True, "aaa"]
# print("*".join(res2))

# # 10 replace 替换字符中的子字符串
# msg = "you can you up, no can no bb"
# # 源字符串 新字符串 替换个数
# # 替换之后之前的字符串没有变化 而是将替换后的字符串直接返回
# new_msg = msg.replace("you", "YOU", 1)
# print(msg)
# print(new_msg)
# new_msg = msg.replace("no", "NO")
# print(msg)
# print(new_msg)

# 11 判断一个字符串是否是纯数字的字符串
# age = "123"
# print(age.isdigit())
# print(age.islower())
# print(age.isupper())
# print(age.isalnum())
# age = "123.132"
# print(age.isdigit())
# age = "pan"
# print(age.isdigit())
# name = "PAN"
# print(name.title())
# print(name.isupper())


# 例子 猜年龄
# age = 20
# while True:
#     inp_age = input("请输入您的年龄:")
#     # 判断是不是一个数字字符串
#     if inp_age.isdigit():
#         if int(inp_age) > age:
#             print("猜大了")
#         elif int(inp_age) < age:
#             print("猜小了")
#         else:
#             print("bingo")
#             break
#     else:
#         print("请输入整数")


# # # 12 find index 查询某个子字符串或者字符在大字符串中的起始索引
# msg = "hello pan hello world"
# print(msg.find("llo"))
# print(msg.rfind("llo"))
# print(msg.index("llo"))
# print(msg.rindex("llo"))
# # 如果使用find查找不到对应的子字符串 返回-1
# print(msg.find("zhao"))
# # 如果使用的是index查找不到对应的子字符串  抛出异常
# print(msg.index("zhao"))
# # 所以推荐使用的是find  而不是index


# # 13 count 查询子字符串在大字符串中出现的次数
# msg = "my name is pan pan pan zhao pan"
# print(msg.count("pan"))
# print(msg.count("a"))
# print(msg.count("zhao pan"))


# # 14 对齐方式 center ljust rjust zfill
# msg = "pan"
# print(msg.center(50, "*"))
# print(msg.ljust(50, "*"))
# print(msg.rjust(50, "*"))
# # 如果是填充 是右对齐 前面默认是使用0作为占位符
# print(msg.zfill(50))

# 15 设置 制表符的空格数
# msg = "hello\world"
# print(msg.expandtabs(10))

# # 16
# # capitalize 会将字符串的第一个字符改为大写 其他都改为小写
# print("hello world PAN".capitalize())
# # Hello world pan
# # swapcase 大小写转换， 会将字符串中的大写字符全部改为小写 小写字符全部改为大写
# print("Hello World Pan".swapcase())
# # hELLO wORLD pAN
# # title 会将字符串中的每个单词的首个字符改为大写
# # 如果是非字母会忽略 直接找到下一个
# print("hello world 1an 攀pan".title())
# # Hello World 1An 攀Pan

# # 17 is系列
# # 判断是否是title样式
# print("Hello World 1An".istitle())
# # 判读是否是大小写
# print("abc".islower())
# print("ABC".isupper())
# # 是不是全部是字符
# print("adffdasifdsadf".isalpha())
# # 是不是只有字母和数字组成的字符串
# print("f123fasdfdsi".isalnum())
# # 是否是由空格组成的字符
# print("  ".isspace())
# # 判断是否是合法变量名
# print("print".isidentifier())
# print("ege_of-pa".isidentifier())
# print("123age".isidentifier())

# 18 num系列
num1 = b'5'  # bytes
num2 = u'5'  # unicode python3中无需添加u就是unicode
num3 = '五'  # 中文数字
num4 = 'Ⅳ'  # 罗马数字

# # isdigit 只能识别num1 num2
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())
# print(num4.isdigit())

# # isnumeric 可以识别 num2 num3 num4
# # num1 不能调用isnumeric这个方法
# # print(num1.isnumeric())  # error
# print(num2.isnumeric())
# print(num3.isnumeric())
# print(num4.isnumeric())

# #  isdecimal 只能识别num2
# print(num2.isdecimal())
# print(num3.isdecimal())
# print(num4.isdecimal())
