# @time: 2022/1/13 6:28 PM
# Author: pan
# @File: 01json模块.py
# @Software: PyCharm
"""
1、什么是序列化&反序列化？
内存中的数据 ----> 序列化    ------> 特定的格式(json或pickle格式)
内存中的数据 <---- 反序列化  <------ 特定的格式(json或pickle格式)

2、为什么要序列化？
序列化就是将内存中的数据转换一种特定格式，这种格式的数据对于存储或传输都比较友好
序列化后的数据可以有两种用途
I 用户数据存储（数据存档等）
II 用户多平台之间的数据传输（跨平台数据交互）

强调：
用途1使用的特定格式：可以是一种专门的格式 = pickle只有python可以识别
用途2使用的特定格式：需要是多种平台都可以识别出来的格式 = json格式的数据

3、如何进行序列化和反序列化
使用库json或pickle

"""

# json使用
import json

# 实例1

# 序列化
# json_res = json.dumps([1, 'aaa', 'bbb', True, False, 10.1])
# print(json_res, type(json_res))
# [1, "aaa", "bbb", true, false, 10.1] <class 'str'>
# 序列化后的数据是一个字符串
# int/float => int/float
# list => []
# dic => {}
# str => "" 序列化后是一个双引号括起来的字符串
# True/False => true/false  大写的真假序列化后变成小写的true/false


# 反序列化
# res = json.loads(json_res)
# print(res, type(res))
# [1, 'aaa', 'bbb', True, False, 10.1] <class 'list'>
# 反序列化后 转换为 python语言可以识别的格式


# 实例 将序列化后的数据保存到文件中
# 以及从文件中 取出数据进行反序列化
print('实例2'.center(100, "="))


# ======== 序列化数据到一个文件中 ==========
json_res = json.dumps([1, 'aaa', 'bbb', True, False, 10.1, "你好中国"])
print(json_res, type(json_res))
# 中文会转换为unicode码
# [1, "aaa", "bbb", true, false, 10.1, "\u4f60\u597d\u4e2d\u56fd"] <class 'str'>
with open(r'test.json', mode='wt', encoding='utf-8') as f:
    f.write(json_res)
    # 可以直接使用dump方法 简化该序列化
    # dump中会默认将序列化后的数据进行写入到文件中
    # json.dump([1, 'aaa', 'bbb', True, False, 10.1], f)


# ========== 反序列化文件中的数据 ==============
with open(r'test.json', mode='rt', encoding='utf-8') as f:
    res = json.loads(f.read())
    print(res, type(res))
    # 可以使用load简化反序列化的结构
    # load会默认先进行读取文件中的内容 然后进行反序列化
    # json.load(f)


# 其他实例
# TypeError: Object of type set is not JSON serializable
# json序列化 不支持集合类型的数据
# json.dumps({1, 2, 3, 10})

# 对于一个元组进行序列化 会被序列化成一个列表形式的字符串
# [1, 2, 3, 10] <class 'str'>
# res = json.dumps((1, 2, 3, 10))
# print(res, type(res))

# json序列化就是一个字符串
# python的字符串序列化后 会转换为双引号的数据  而不是单引号的数据
res = json.loads('[1, "aaa", "bbb", "你好中国🇨🇳"]')
print(res, type(res))

# 不支持这种json格式的数据
# json字符串中不能出现单引号
# res2 = json.loads("[1, 'aaa', True]")
# print(res, type(res2))

"""
需求：
一个项目中开发完毕后，想要修改json序列化的方法
但是项目中很多地方都使用了 dumps和loads 
一个一个的修改太麻烦 如何办呢？

可以使用猴子补丁进行修改！！！
只需要在项目的起始文件start中进行修改一下 也就是打补丁

import json
# import ujson

def monkey_patch_json():
    json.__name__ = "ujson"
    # json.dumps = ujson.dumps
    # json.loads = ujson.loads

# 在项目的启动文件中进行调用该函数
monkey_patch_json()

# 不能使用该种方式
# 如果使用改种方式 也不要在很多地方都进行设置
# 但是多次导入一个库 只会引用第一次导入的时候产生的名称空间
import ujson as json
"""

# pickle 模块
# 该模块和json类似
# pickle模块支持所有的python数据格式
# 不适合进行跨平台数据传输  因为 其他平台有可能没有python的数据类型
import pickle

# res = pickle.dumps([1, "aaa", "bbb", True, False, 10.111])
# pickle支持集合类型 json不支持集合类型
res = pickle.dumps({1, 10, 22, 100})
# 返回的是bytes类型
# b'\x80\x04\x95\x1e\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01\x8c\x03aaa\x94\x8c\x03bbb\x94\x88\x89G@$8\xd4\xfd\xf3\xb6Fe.' <class 'bytes'>
print(res, type(res))

r = pickle.loads(res)
print(r, type(r))







