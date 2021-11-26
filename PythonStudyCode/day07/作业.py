# 打印1-10 除了7
# count = 1
# while count <= 10:
#     if count == 7:
#         count += 1
#         continue
#     print(count)
#     count += 1

# for-in
# for i in range(1, 11):
#     if i == 7:
#         continue
#     print(i)

# 计算1-100的和
# sum = 0
# count = 1
# while count <= 100:
#     sum += count
#     count += 1
# print(sum)

# for-in
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)

# 打印1-100之间的所有奇数
# count = 1
# while count <= 100:
#     if count % 2 != 0:
#         print(count)
#     count += 1

# for-in
# for i in range(1, 101):
#     if i % 2 != 0:
#         print(i)

# 打印1-100之间的所有偶数
# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1
# else:
#     print("打印完成")

# 打印1-100中所有的质数
# 质数只能被1和自身整除的数
# count = 1
# while count <= 100:
#     i = 2
#     is_prime = False
#     while i < count and count > 2 and i < count // 2:
#         if count % i == 0:
#             is_prime = True
#             break
#         i += 1
#     if not is_prime:
#         print(count)
#     count += 1

# 逢7过
# 如果数字中包含7或能被7整除的话 不打印
# count = 1
# while count <= 100:
#     if count % 7 == 0 or count % 10 == 7 or count // 10 == 7:
#         print("包含{}".format(count))
#     count += 1

# for-in
# for i in range(1, 101):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         print(i)


# 计算1-100 减去偶数 加上奇数后的结果
# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 0:
#         sum -= count
#         print("sum-{}".format(count))
#     else:
#         sum += count
#         print("sum+{}".format(count))
#     count += 1
# print(sum)

# for-in
# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum -= i
#         print("sum - ", i)
#     else:
#         sum += i
#         print("sum + ", i)

# 三次机会输入用户名和密码
# count = 0
# while True:
#     input_name = input("请输入您的姓名:")
#     input_pwd = input("请输入您的密码:")
#     if input_name == "pan" and input_pwd == "123":
#         print("登录成功!")
#         break
#     else:
#         print("请重新输入:")
#         count += 1
#
#     if count == 3:
#         print("三次机会已经没有了")
#         break

# for-in
for i in range(3):
    input_name = input("请输入您的姓名:")
    input_pwd = input("请输入您的密码:")
    if input_name == "pan" and input_pwd == "123":
        print("登录成功")
        break
else:
    print("三次机会已经使用完毕")

# 猜年龄
# age = 60
# count = 0
# while True:
#     input_age = input("请输入年龄:")
#     if int(input_age) > age:
#         print("输入的年龄大了")
#     elif int(input_age) < age:
#         print("输入的年龄小了")
#     else:
#         print("恭喜您 猜对了")
#         break
#     count += 1
#
#     if count == 3:
#         while True:
#             answer = input("是否还想继续玩:")
#             if answer == "y" or answer == "Y":
#                 print("请继续猜吧")
#                 count = 0
#                 break
#             elif answer == "n" or answer == "N":
#                 print("次数已经用完，下次再来")
#                 break
#             else:
#                 print("请重新回答是否还要继续玩?")
#
#         if count == 3:
#             break
#
# print("===== end =====")
