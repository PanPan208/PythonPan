# @time: 2022/1/13 2:38 PM
# Author: pan
# @File: 03random模块.py
# @Software: PyCharm
"""
随机数据模块
"""
import random

# random() 循环一个(0, 1) 之间的一个小数
print(random.random())

# [1, 3] 随机一个1到3的一个整数
print(random.randint(1, 3))

# [1, 3) 因为range是顾头不顾尾 所以3 不会被随机到
print(random.randrange(1, 3))

# 从一个列表中随机出来一个数据
print(random.choice([111, "aaaa", (222, 333)]))

# 从一个列表中随机出来n个元素 然后组成一个新的列表
print(random.sample([111, "a", "b", "c"], 3))


# 随机一个在(a, b) 之间的一个小数
print(random.uniform(1, 3.9))


# 将一个列表的数据进行打乱 并返回到该列表
items = [1, 3, 4, 7, 9, 10]
random.shuffle(items)
print(items)


# 应用
print("随机实例".center(100, "*"))
'''
需求从26个英文字母中和1到9中随机n个组成一个随机的验证码
'''


def random_code(size):
    """
    随机出一个固定尺寸大小的验证码
    :param size: 验证码的长度
    :return:
    """
    import random
    code_str = ''
    for i in range(size):
        # 1 大写字母的ASC码表是从65到90的数字
        # 随机出65到90的数字后 然后将该数字转换为对应的字符
        ch = chr(random.randint(65, 90))
        # 2 随机1到9中的一个数字
        # 并将该数字转换为字符串
        num_str = str(random.randint(1, 9))
        # 3 在字母和数字中随机一个 拼接到验证码字符串中
        code_str += random.choice([ch, num_str])
    return code_str


print(random_code(4))
print(random_code(6))

print("end".center(100, "="))










