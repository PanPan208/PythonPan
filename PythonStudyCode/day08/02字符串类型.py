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

# 只能取 不能对对应的位置设置值
# msg[0] = "haha"


# 2 切片取
# msg = "hello world"
# 取0-5之间的子字符串
# print(msg[0:5])
# 取的是0-5之间的数 间为2
# 0 2 4
# print(msg[0:5:2])
# 反向取
# print(msg[3:0:-1])
# 倒着取值， 3 2 1  取完之后反转
# 0 右侧 不可取
# 全部取出来
# print(msg[:])
# hello world
# 全部反向来
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
# # print(msg.strip())
# print(msg.lstrip())
# print(msg.rstrip())

# 可以指定去掉字符串两端的字符
# msg = "****hello world***"
# print(msg.strip("*"))
# print(msg.lstrip("*"))

# 应用：
# while True:
#     input_name = input("请输入您的姓名:").strip().lower()
#     input_pwd = input("请输入密码:").strip().lower()
#     if input_name == "pan" and input_pwd == "123":
#         print("登录成功")
#         break
# print("=======end")

# 6 切分字符串 split
# 把一个字符串根据某个分割符进行分割 得到一个列表
# 默认的分割符是空格
# msg = "my mame is pan"
# print(msg.split())
# print(msg.rsplit())

# 根据指定的字符串进行分割
# msg = "my*mame*is*pan"
# print(msg.split("*"))
# 指定分割次数
# print(msg.split("*", 2))
# 从右侧开始分割 分割两次
# print(msg.rsplit("*", 2))
# 将整体作为一个元素
# print(msg.splitlines())


# # 7 大小写转换
# msg = "AAAbbCCcccDDDddd"
# print(msg.upper())
# print(msg.lower())


# 8 是否以某个字符串开头 某个字符串结尾
# msg = "my name is pan"
# print(msg.startswith("my"))
# print(msg.startswith("pan"))
# print(msg.endswith("pan"))
# print(msg.endswith("pans"))

# # 9 将一个列表拼接成一个字符串
# # 如果拼接一个列表 列表中只能是字符串类型
# myList = ["my", "name", "is", "100"]
# # 一个一个拼接
# res1 = myList[0] + ":" + myList[1] + ":" + myList[2] + ":" + myList[3]
# print(res1)
# # 使用join进行拼接
# res = ":".join(myList)
# print(res)