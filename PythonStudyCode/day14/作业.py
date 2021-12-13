# @time: 2021/12/10 2:55 下午
# Author: pan
# @File: 作业.py
# @Software: PyCharm

# 1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
def change_file1(name, res_content, dis_content):
    with open(r"{}".format(name), mode="rt") as f1:
        res = f1.read()
        data = res.replace(res_content, dis_content)
    with open(r"{}".format(name), mode="wt") as f2:
        f2.write(data)


# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def get_type_cout(name):
    type_dic = {"num": 0, "str": 0, "space": 0, "other": 0}
    for item_str in name:
        if item_str.isdigit():
            type_dic["num"] += 1
        elif item_str.isalpha():
            type_dic["str"] += 1
        elif item_str.isspace():
            type_dic["space"] += 1
        else:
            type_dic["other"] += 1
    print(type_dic)


# get_type_cout("hello123ff1 fd^&*")

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def func1(k):
    if len(k) > 5:
        return True
    else:
        return False

# print(func1("hello world"))
# print(func1("hell"))
# print(func1([1, 2, 3, 4, 10, 20]))
# print(func1((1, 2, 3, 10, 30)))

# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者。
def func2(k: list):
    if len(k) > 2:
        return k[:2]

# print(func2("hello"))
# print(func2([10, 20, 30, 100]))

# 5、写函数，检查获取传入列表或元组对象的 '所有奇数位索引' 对应的元素，
# 并将其作为新列表返回给调用者。
def func3(k: list):
    return k[1::2]

# print(func3([10, 20, 3, 5, 10]))
# print(func3("Helloworld"))
# print(func3("1"))


# 6、写函数，检查字典的每一个value的长度,
# 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表
def func4(k: dict):
    for key, value in k.items():
        if len(value) > 2:
            k[key] = value[:2]
    return k


dic1 = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
dic2 = func4(dic1)
print(dic2)
