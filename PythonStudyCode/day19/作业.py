# @time: 2021/12/24 4:43 PM
# Author: pan
# @File: 作业.py
# @Software: PyCharm

# 1、文件内容如下,标题为:姓名,性别,年纪,薪资
# egon male 18 3000
# alex male 38 30000
# lili female 28 20000
# niuniu female 28 10000


# 要求:
# 1 从文件中取出每一条记录放入列表中,
# 列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式
# user_info = []
# 方案一  普通方法
'''
with open("user_info.txt", mode="rt", encoding="utf-8") as f:
    for line in f:
        temp_l = line.strip().split(" ")
        print(temp_l)
        temp_dic = {"name": temp_l[0], "sex": temp_l[1],
                    "age": int(temp_l[2]), "salary": float(temp_l[3])}
        user_info.append(temp_dic)
print(user_info)
'''

# 方案二  普通方案优化
'''
def get_user_info():
    with open("user_info.txt", mode="rt", encoding="utf-8") as f:
        for line in f:
            name, sex, age, salary = line.strip().split(" ")
            # print(name, sex, age, salary)
            user_info.append({
                "name": name, "sex": sex,
                "age": int(age), "salary": int(salary)
            })
    return user_info

get_user_info()
'''


# 方案三： 使用列表生成式以及map函数
# 一行代码实现
def get_user_info2():
    user_info = []
    with open("user_info.txt", mode="rt", encoding="utf-8") as f:
        user = map(lambda l: {"name": l[0], "sex": l[1], "age": int(l[2]), "salary": int(l[3])}, [line.strip().split(' ') for line in f])
        user_info = list(user)
    return user_info

user_info = get_user_info2()
print(f"====> {user_info}")

# 2 根据1得到的列表,取出所有人的薪资之和
# 普通方法
# sum_salary = 0
# for dic in user_info:
#     print(dic)
#     salary = dic.get("salary")
#     print(salary)
#     sum_salary += salary
# print(sum_salary)

sum_salary = sum(dic.get("salary") for dic in user_info)
print(sum_salary)


# 3 根据1得到的列表,取出所有的男人的名字
male_name = [dic.get("name") for dic in user_info if dic.get("sex") == "male"]
print(male_name)

# # 过滤出性别是男的字典
# male_name2 = filter(lambda dic: dic.get("sex") == "male", user_info)
# print(list(male_name2))

# 4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
# 普通方法
'''
new_user_info = []
for dic in user_info:
    dic["name"] = str(dic.get("name")).capitalize()
    new_user_info.append(dic)
print(new_user_info)
'''

# 方法二
# 使用map进行映射 映射的时候姓名的首字母大写 其他的不变
new_user_info = map(lambda sub_dic: {
    "name": str(sub_dic.get("name")).capitalize(),
    "sex": sub_dic.get("sex"),
    "age": sub_dic.get("age"),
    "salary": sub_dic.get("salary")
}, [dic for dic in user_info])
print(f"=====> {list(new_user_info)}")


# 5 根据1得到的列表,过滤掉名字以a开头的人的信息
# 方法1 列表行列式
new_user_info1 = [dic for dic in user_info if not dic.get("name").startswith("a")]
print(new_user_info1)

# 方法二 filter过滤
# new_user_info2 = filter(lambda sub_dic: str(sub_dic.get("name")).startswith("a"),
#                         [dic for dic in user_info])
# print(list(new_user_info2))


# 6 使用递归打印斐波那契数列
# (前两个数的和得到第三个数，如：[0 1 1 2 3 5 8 13 21 34...])
# 递归得到第n个斐波那契数的数值
"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(8))

new_list = [fibonacci(i) for i in range(20)]
print(new_list)
"""

# 打印小于某一个数的 所有斐波那契额数列
'''
f1 = 0
f2 = 1
def fibonacci2(n):
    global f1, f2
    while f1 < n:
        print(f1, end=" ")
        # 将f2赋值给f1
        # 将f1和f2的和赋值给f2
        f1, f2 = f2, f1 + f2

fibonacci2(1000)
'''


# 7 一个嵌套很多层的列表，
# 如 l= [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]
# 用递归取出所有的值
"""
l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]
# print(l)
def print_num(list1):
    for line in list1:
        if type(line) is list:
            print_num(line)
        else:
            print(line)
print_num(l)
"""