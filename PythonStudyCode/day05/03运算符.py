"""
算术运算符
比较运算符
赋值运算符
"""
# 1 算术运算符
# print(10 + 23.1)  # 33.1
# print(10 - 23)  # -13
# print(10 * 23)  # 230
# print(10 / 3)  # 3.33333333
# print(10 // 3)  # 3
# # // 取整数部分  不是四舍五入
# print(10 % 3)  # 1
# # % 取余 也叫 取模
# print(10 ** 3)
# # ** 获取 10的三次方


# 2 比较运算符  > >= < <= == !=
# print(10 > 20)
# print(10 >= 9.9)
# print(10 == 20)
# name = "pan"
# print(name == "zhaopan")


# 3 逻辑运算符
# 单个= 是直接赋值运算符
# age = 10
# age = age + 1
# print(age)

# 增量赋值运算
# age = 10
# age += 1
# print(age)
#
# age /= 2
# print(age)
# age **= 2  # 等价于 age = age ** 2
# print(age)


# 链式赋值运算
# x = 10
# y = x
# z = x
# print(x, y, z)
# print(id(x), id(y), id(z))

# x = 10
# z = y = x
# print(x, y, z)
# print(id(x), id(y), id(z))


# 交叉赋值  两个数进行替换
# m = 10
# n = 20
# # 使用一个中间变量进行 两个值的替换
# print(m, n)
# temp = m
# m = n
# n = temp
# print(m, n)


# 使用简单方式 替换 m n
# m = 10
# n = 20
# print(m, n)
# # m, n = n, m
# (m, n) = (n, m)
# print(m, n)


# 解压赋值
# 1个1个的取
# salary = [1, 2, 3, 4]
# mon0 = salary[0]
# mon1 = salary[1]
# mon2 = salary[2]
# mon3 = salary[3]
# print(mon0, mon1, mon2, mon3)

# salary = [1, 2, 3, 4]
# # 直接使用多个变量对应一个列表
# # 变量多一个 少一个 都不行
# mon0, mon1, mon2, mon3 = salary
# # s0, s1, s2, s3, s4 = salary  # error
# # s0, s1 = salary  # error
# print(mon0, mon1, mon2, mon3)


# 使用 *_ 通配符 获取列表的前几个值， 或后几个值  不能获取中间的几个值
# _ 代表一个变量 匹配剩余所有的数据
# 匹配前三个数据
# mon0, mon1, mon2, *_ = salary = [111, 222, 333, 444, 555, 666, 777]
# print(mon0, mon1, mon2, _)

# 匹配的是后三个数据
# *_, mon0, mon1, mon2 = salary = [111, 222, 333, 444, 555, 666, 777]
# print(mon0, mon1, mon2)

# 匹配前面1个值， 和后面的两个值
# mon0, *_, mon1, mon2 = salary = [111, 222, 333, 444, 555, 666, 777]
# print(mon0, mon1, mon2)

# 这样会将除了第一个会最后一个 其他的都匹配到mon0
# _, *mon0, _ = salary = [111, 222, 333, 444, 555, 666, 777]
# print(mon0)

# 如果是使用链式取字典中的内容
# 默认是取的字典中的key值
# x, y, z = dict = {"name": "pan", "age": 10, "salary": 1000}
# print(x, y, z)



# 作业：
# name = input("请输入您的姓名:")
# age = input("请输入您的年龄:")
# job = input("请输入您的工作:")
# hobby = input("请输入您的爱好:")
# print("-"*12 + " info of {} ".format(name) + "-"*12)
# print("Name  : {}".format(name))
# print("Age   : {}".format(age))
# print("job   : {}".format(job))
# print("Hobby : {}".format(hobby))
# print("-"*18 + " end " + "-"*18)

# account = input("请输入账号:")
# password = input("请输入密码:")
# print(account == "123")
# print(password == "123")

# age_of_egon = 20
# age = input("请输入您所猜的年龄:")
# age = int(age)
# print(age_of_egon == age)

# 10000条数据 每页显示30条
# total_num = 10000
# page_num = 30
# # 333 一共有333个页面显示的数据是30个
# print(total_num // page_num)
# # 10 最后一个页面显示的数据是10个
# print(total_num % 30)

# age_of_egon = 18
# age_of_egon += 3
# print(age_of_egon)

# z = y = x = 10
# print(x, y, z)
# print(id(x), id(y), id(z))

# dsb = "egon"
# superman = "alex"
# superman, dsb = dsb, superman
# print(dsb, superman)


# names = ['alex_sb', 'wusir_sb', 'oldboy_sb', 'egon_nb', 'lxx_nb', 'tank_nb']
# sb1, sb2, sb3, *_ = names
# print(sb1, sb2, sb3)

