# @time: 2021/12/27 5:25 PM
# Author: pan
# @File: 作业.py
# @Software: PyCharm

# 作业：
# 1、文件内容如下,标题为:姓名,性别,年纪,薪资
#     egon male 18 3000
#     alex male 38 30000
#     wupeiqi female 28 20000
#     yuanhao female 28 10000
#
# 要求:
# 从文件中取出每一条记录放入列表中,
# 列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式
user_info = []
"""
with open("user_info.txt", mode="rt", encoding="utf-8") as f:
    for line in f:
        res = line.strip().split(" ")
        print(res)
        user_dic = {"name": res[0], "sex": res[1],
                    "age": int(res[2]), "salary": int(res[3])}
        user_info.append(user_dic)
print(user_info)
"""


# 获取文件中的用户数据
def get_user_info():
    global user_info
    with open("user_info.txt", mode="rt", encoding="utf-8") as f:
        # 使用for循环优化
        # for line in f:
        #     name, sex, age, salary = line.strip().split(" ")
        #     user_info.append({
        #         "name": name, "sex": sex,
        #         "age": int(age), "salary": int(salary)
        #     })
        # 方法二 使用列表生成式  列表生成式套列表生成式
        user_info = [{"name": sub_dic.strip().split(" ")[0],
                      "sex": sub_dic.strip().split(" ")[1],
                      "age": sub_dic.strip().split(" ")[2],
                      "salary": sub_dic.strip().split(" ")[3]} for sub_dic in [line for line in f]]
get_user_info()
print(user_info)


# [{'name': 'egon', 'sex': 'male', 'age': 18, 'salary': 3000},
# {'name': 'alex', 'sex': 'male', 'age': 38, 'salary': 30000},
# {'name': 'wupeiqi', 'sex': 'female', 'age': 28, 'salary': 20000},
# {'name': 'yuanhao', 'sex': 'female', 'age': 28, 'salary': 10000}]


# 2 根据1得到的列表,取出薪资最高的人的信息
# 取出最大的值 根据后面的key进行取max
res = max(user_info, key=lambda sub_dic: sub_dic.get("salary"))
print(f"max salary: {res}")


# 3 根据1得到的列表, 取出最年轻的人的信息
res2 = min(user_info, key=lambda sub_dic: sub_dic.get("age"))
print(res2)


# 4、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
"""
# 使用列表生成式1
names = ['egon', 'alex_sb', 'wupeiqi', 'yuanhao']
# new_names = [name.upper() for name in names]
# print(new_names)

# 使用map映射2
new_names = map(lambda name: name.upper(), names)
print(new_names)
for name in new_names:
    print(name)
"""

# 5、将names=['egon','alex_sb','wupeiqi','yuanhao'] 中以sb结尾的名字过滤掉，
# 然后保存剩下的名字长度
"""
names = ['egon', 'alex_sb', 'wupeiqi', 'yuanhao']
new_names = [len(name) for name in names if not name.endswith("sb")]
print(new_names)

new_names = filter(lambda name: not name.endswith("sb"), names)
print(new_names)
for name in new_names:
    print(name)
"""

# 6、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
'''
# with open("user_info.txt", mode="rt") as f:
    # for line in f:
    #     print(line)

    res = max(f, key=lambda line: len(line))
    print(res)
    print(len(res))
'''


# 7、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？
# （需要使用sum函数）
'''
# with open("user_info.txt", mode="rt") as f:
    # 方法一
    # a_sum = 0
    # for line in f:
    #     a_sum += len(line)
    # print(a_sum)
    # 方法二
    a_sum = sum(len(line) for line in f)
    print(a_sum)
    # 因为当前读取之后 指针在最后面 所有后面再读取的都是0
    a_sum = sum(len(line) for line in f)
    print(a_sum)
    a_sum = sum(len(line) for line in f)
    print(a_sum)
    a_sum = sum(len(line) for line in f)
    print(a_sum)
'''


# 8、思考题
# with open('user_info.txt') as f:
#     g = (len(line) for line in f)
#     print(g)
#
# print(g)
# print(sum(g))  # 为何报错？
# ValueError: I/O operation on closed file.
# 因为文件中的g是返回的是一个生成器和文件有关
# with之后文件被关闭了
# 再操作该生成器就相当于在操作一个已经关闭的文件 所以会报错


# 9、文件shopping.txt内容如下
# mac,20000,3
# lenovo,3000,10
# tesla,1000000,10
# chicken,200,1
# 1、求总共花了多少钱？
from functools import reduce
def get_total_money():
    total_money = 0
    with open("shopping.txt", mode="rt", encoding="utf-8") as f:
        # 方法一： 使用for循环
        # for line in f:
        #     name, price, count = line.strip().split(",")
        #     total_money += int(price) * int(count)

        # 方法二： 使用reduce进行递归计算
        total_money = reduce(lambda x, y: x + y,
                             [int(line.strip().split(',')[1]) * int(line.strip().split(',')[2]) for line in f], 0)
    return total_money

res = get_total_money()
print(res)

# 2、打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
shop_list = []
def get_shop_list():
    with open("shopping.txt", mode="rt", encoding="utf-8") as f:
        for line in f:
            name, price, count = line.strip().split(',')
            shop_list.append({
                "name": name,
                "price": int(price),
                "count": int(count)
            })

get_shop_list()
print(shop_list)

# 3、求单价大于10000的商品信息, 格式同上
res3 = [dic for dic in shop_list if int(dic.get("price")) > 10000]
print(f"大于10000的商品: {res3}")

# 使用过滤函数
res4 = filter(lambda sub_dic: int(sub_dic.get("price")) > 10000, [dic for dic in shop_list])
print(list(res4))
