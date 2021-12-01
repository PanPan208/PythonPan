"""
流程控制之while语句
"""

# count = 1
# while count < 5:
#     print(count)
#     count += 1


# 死循环
# while True:
#     print("111")

# while True:
#     name = input("请输入您的姓名:")
#     print("my name is {}".format(name))

# 如果一个死循环是纯计算没有io操作的那么会导致致命的效率问题
# while True:
#     1 + 1

name = "pan"
pwd = "123"

# 退出循环的两种方法:
# 1 使用break
# while True:
#     input_name = input("请输入您的姓名:")
#     input_pwd = input("请输入您的密码:")
#
#     if input_name == "pan" and input_pwd == "123":
#         print("登录成功!")
#         break
#     else:
#         print("请重新输入:")
#
# print("======= end ====== ")

# 2 使用变量控制 flag
# flag = True
# while flag:
#     input_name = input("请输入您的姓名:")
#     input_pwd = input("请输入您的密码:")
#
#     if input_name == name and input_pwd == pwd:
#         print("登录成功!")
#         flag = False
#     else:
#         print("请重新输入:")
#
# print("======= end ====== ")

# 实例
# while True:
#     input_name = input("请输入您的姓名:")
#     input_pwd = input("请输入您的密码:")
#     if input_name == name and input_pwd == pwd:
#         print("登录成功!")
#         while True:
#             cmd = input("请输入命令>:")
#             if cmd == "q" or cmd == "Q":
#                 break  # 结束的是内层循环
#             print("cmd命令正在运行中...")
#             print("{}命令运行完成".format(cmd))
#
#         break  # 跳出外层循环
#     else:
#         print("请重新输入:")
#
# print("======= end ====== ")

# while-else语句
# 1 正常退出 不是因为break才退出while循环的
# 会执行while-else中的语句
# count = 1
# while count < 5:
#     print(count)
#     count += 1
# else:
#     # else 语句如果不是break语句退出的语句 都会执行else中的代码块
#     print("while else 正常退出的语句")
#
# print("=========  end ==========")

# 2 由break 而退出while-else循环的
# 会执行break语句
count = 0
while count < 3:
    input_name = input("请输入姓名:")
    if input_name == name:
        print("姓名输入正确")
        break
    else:
        print("请重新输入")
    count += 1
else:
    # 由于是因为break退出的while循环 所以else代码块永远不会执行
    # 不会执行的语句 PyCharm直接会提示错误
    print("break退出的while语句不会执行 else语句")

print("=========  end ==========")

# Python中没有do-while语句
