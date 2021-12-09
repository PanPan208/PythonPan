# 1、有列表['alex',49,[1900,3,18]]，
# 分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
# 方法一 一个一个的取
# info = ['alex', 49, [1900, 3, 18]]
# name = info[0]
# age = info[1]
# year = info[2][0]
# mouth = info[2][1]
# day = info[2][2]
# print(name, age, year, mouth, day)

# 方法二 对应取
# name, age, birthday = ['alex', 49, [1900, 3, 18]]
# year, mouth, day = birthday
# print(name, age, birthday)
# print(year, mouth, day)

# 2、用列表的insert与pop方法模拟队列
# # 先进先出
# info = []
# info.insert(0, "a")
# info.insert(1, "b")
# info.insert(2, "c")
# print(info)
#
# print(info.pop(0))
# print(info.pop(0))
# print(info.pop(0))

# 3. 用列表的insert与pop方法模拟堆栈
# # 后进先出
# info = []
# info.insert(0, "a")
# info.insert(1, "b")
# info.insert(2, "c")
# print(info)
#
# print(info.pop())
# print(info.pop())
# print(info.pop())


# 5、有如下值集合 [11, 22, 33, 44, 55, 66, 77, 88, 99, 90, 100]
# 将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90, 100]
info = {"k1": [], "k2": []}
for num in nums:
    if num >= 66:
        info.get("k1").append(num)
    else:
        info.get("k2").append(num)
print(info)

# 6、统计s='hello alex alex say hello sb sb'中每个单词的个数
s = 'hello alex alex say hello sb sb'
my_list = s.split()
my_dic = {}

for item in my_list:
    if item not in my_dic:
        my_dic[item] = 1
    else:
        my_dic[item] += 1
print(my_dic)

# for item in s.split():
#     print("{} 单词出现的个数是:{}".format(item, s.count(item)))
