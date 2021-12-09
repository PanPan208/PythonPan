# 一：今日作业：
# 1、编写文件copy工具

# 版本1
# with open(r"a.txt", mode="rt") as f1, \
#         open("aaaa.txt", mode="wt") as f2:
#     res = f1.read()
#     f2.write(res)

# 版本2
# res_file = input("请输入源文件路径:")
# dis_file = input("请输入目标文件路径:")
# with open(res_file.strip(), mode="rb") as f1, \
#     open(dis_file.strip(), mode="wb") as f2:
#     res = f1.read()
#     f2.write(res)

# 版本3
# res_file = input("请输入源文件路径:")
# dis_file = input("请输入目标文件路径:")
# with open(res_file.strip(), mode="rb") as f1, \
#     open(dis_file.strip(), mode="wb") as f2:
#     for line in f1:
#         f2.write(line)



# 2、编写登录程序，账号密码来自于文件
# name_input = input("请输入您的用户名:").strip()
# pwd_input = input("请输入您的密码:").strip()
# with open(r"user.txt", mode="rt") as f:
#     for line in f:
#         # 每一行 最后默认有一个换行符 需要strip一下
#         name, pwd = line.strip().split(":")
#         print(name, pwd)
#         if name_input == name and pwd_input == pwd:
#             print("登录成功")
#             break
#     # for - else 如果for循环结束之后 没有break 说明没有对应的用户名/密码
#     # 也就是账号或密码错误
#     else:
#         print("账号或密码错误")


# 3、编写注册程序，账号密码来存入文件
name_input = input("请输入您的用户名:").strip()
pwd_input = input("请输入您的密码:").strip()

# 因为是注册 不能将老的数据清除所以需要使用 a模式
with open(r"register.txt", mode="a+t", encoding="utf-8") as f:
    # 因为是a模式所以 光标打开之后默认是在最后面的
    # 为了查找数据 先将光标seek到开头
    f.seek(0, 0)
    # 如果用户名已经存在 提示账号已经存在
    for line in f:
        name, pwd = line.strip().split(":")
        print(name, pwd)
        if name_input == name:
            print("用户名已经存在")
            break
    else:
        # 用户名不存在 然后将光标移动到最后面
        # 然后再添加数据
        f.seek(0, 2)
        f.write(f"{name_input}:{pwd_input}\n")

