# @time: 2022/1/14 3:37 PM
# Author: pan
# @File: 03hashlib模块.py
# @Software: PyCharm
"""
1 什么是hash
hash就是一类算法 该算法通过传入一个值， 然后返回一串hash字符串的值

hash值的特点：
I 只要每次传入的值不变 hash出来的hash值就不变
II hash值不能反解成对应的内容
III 不管传入的值有多大， 只要使用的hash算法不变 hash出来的hash值的长度是一定的


2、hash的用途
I 用户密码的密文传输和验证
II 用于验证文件的完整性

3、hash的使用
import  hashlib
"""

import hashlib

# 1 可以选择不同的hash算法
# md5是其中的一种
# 相当于是产生了一个hash工程 然后可以往该工厂中运送原材料(也就是进行hash的数据)
# 工厂生产完数据之后 返回一个产品也就是一个hash值
m = hashlib.md5()
# 2 update 进行hash的数据必须先进行编码
# 可以多次添加hash的值
m.update('hello'.encode('utf-8'))
m.update("world".encode("utf-8"))
# 3 最后将hash结果返回
res = m.hexdigest()
print(res)

# udpate添加数据可以分开进行添加数据 产生的hash值是一样的
# 这样可以加盐提供了方便
m1 = hashlib.md5("he".encode('utf-8'))
# m1.update("he".encode("utf-8"))
m1.update("llo".encode("utf-8"))
m1.update("wor".encode("utf-8"))
m1.update("ld".encode("utf-8"))
res1 = m1.hexdigest()
print(res1)

# 加盐
m2 = hashlib.sha256()
m2.update("天王盖地虎".encode("utf-8"))
m2.update("hello".encode("utf-8"))
m2.update("宝塔镇河妖".encode("utf-8"))
m2.update("world".encode("utf-8"))
res2 = m2.hexdigest()
print(res2, type(res2))


# 如何破解密码呢？
# 模拟撞库
# 将一些列可能的密码进行相同的hash  如果hash出来的值是一样的 那么就是对应的密码
# 需要猜密码的可能形式 以及是否加盐了
# 加盐为撞库添加了成本

# 制作密码字段
passwords = [
    "helloworld",
    "hello",
    "world",
    "worldhello",
    "hello123",
    "helloworld123456",
    "hellohello"
]
# 已经获取的密码密文格式
right_pwd = "fc5e038d38a57032085441e7fe7010b0"

# 使用for循环 遍历出和密文一致的明文密码
for p in passwords:
    res = hashlib.md5(p.encode("utf-8")).hexdigest()
    if res == right_pwd:
        print(f"模拟撞库, 正确密码为: {p}")
        break
else:
    print("没有正确的密码")







