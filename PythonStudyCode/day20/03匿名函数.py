# @time: 2021/12/27 3:53 PM
# Author: pan
# @File: 03匿名函数.py
# @Software: PyCharm

# 1、使用def定义有名函数
def func1(x, y):
    return x + y

print(func1)
# 调用有名函数
res = func1(10, 20)
print(res)

# 2、使用lambda定义无名函数
print(lambda x, y: x + y)

# 调用匿名函数的方式一：
res = (lambda x, y: x + y)(10, 20)
print(res)

# 调用匿名函数的方式二：
# 将匿名函数赋值给一个有名的变量 还不如直接定义一个有名函数
f = lambda x, y: x + y
print(f(10, 20))


# 匿名函数一般都是临时调用一次
# 匿名函数一般不单独使用 一般都是将匿名函数和其他函数一起进行使用

# 匿名函数的应用： ===================   实例 ========================

salaries = {
    'siry': 3000,
    'tom': 7000,
    'lili': 10000,
    'jack': 2000
}

# 需求1 找出薪水最高的那个人 lili

# 直接使用max进行遍历字典的时候 遍历的是字典的key
# 找到的是key最大的值 是tom
# res = max(salaries)
# print(res)


# 如果需要使用value进行查找最大的值 需要指定key也就是按照什么进行查找最大的值
def func(k):
    return salaries[k]
# 1、key可以跟一个函数的地址
res1 = max(salaries, key=func)
print(res1)

# 2、key也可以使用一个匿名函数
res2 = max(salaries, key=lambda k: salaries[k])
print(res2)

# 实例 根据薪水进行查找出 薪水最少的那个人
res3 = min(salaries, key=lambda k: salaries[k])

# 实例： 进行排序 sorted的使用
# 字典默认的是根据key的顺序进行排序的
res4 = sorted(salaries)
print(res4)

# 实例 根据薪水的大小进行排序
res5 = sorted(salaries, key=lambda k: salaries[k])
print(res5)

# 实例根据薪水降序排序  reverse默认为False
res6 = sorted(salaries, key=lambda k: salaries[k], reverse=True)
print(res6)
