# 1、有列表['alex',49,[1900,3,18]]，
# 分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
# info = ['alex', 49, [1900, 3, 18]]
# name = info[0]
# age = info[1]
# year = info[2][0]
# mouth = info[2][1]
# day = info[2][2]
# print(name, age, year, mouth, day)

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


# 4、简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，
# 则将商品名，价格，购买个数以三元组形式加入购物列表，
# 如果输入为空或其他非法输入则要求用户重新输入　
"""
msg_dic = {
    'apple': 10,
    'tesla': 100000,
    'mac': 3000,
    'lenovo': 30000,
    'chicken': 10,
}
product_list = []

while True:
    product_name = input("请输入购买的商品:").strip()
    product_count = input("请输入购买数量:").strip()
    if product_count.isdigit():
        if msg_dic.get(product_name):
            t = (product_name, msg_dic[product_name], int(product_count))
            product_list.append(t)
            print(product_list)
        else:
            print(">>>>>>请输入合法商品")
    else:
        print(">>>>>>请输入合法的数量")
"""


# 5、有如下值集合 [11, 22, 33, 44, 55, 66, 77, 88, 99, 90, 100]
# 将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90, 100]
info = {"k1": [], "k2": []}
for num in nums:
    if num >= 66:
        list1 = info.get("k1")
        list1.append(num)
        info["k1"] = list1
    else:
        list2 = info.get("k2")
        list2.append(num)
        info["k2"] = list2
print(info)

# 6、统计s='hello alex alex say hello sb sb'中每个单词的个数
s = 'hello alex alex say hello sb sb'
for item in s.split():
    print("{} 单词出现的个数是:{}".format(item, s.count(item)))
