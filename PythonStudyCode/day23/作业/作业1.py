# @time: 2022/1/14 4:43 PM
# Author: pan
# @File: 作业1.py
# @Software: PyCharm

# 1、把登录与注册的密码都换成密文形式
import hashlib
import json


def register():
    inp_name = input("请输入用户名:").strip()
    inp_pwd = input("请输入密码:").strip()
    hash_pwd = hashlib.md5(inp_pwd.encode("utf-8")).hexdigest()
    print(inp_name, hash_pwd)
    # 将用户名密码写入到数据库中
    # 可以使用之前的文本格式 name:pwd:money 的格式进行存储
    # 也可以使用json进行存储
    user_dic = {"user_name": inp_name, "user_pwd": hash_pwd}
    with open(r'user.txt', mode="wt", encoding="utf-8") as f:
        json.dump(user_dic, f)
        # f.write(f'{inp_name}:{hash_pwd}\n')

register()


def login():
    inp_name = input("请输入用户名:").strip()
    inp_pwd = input("请输入密码:").strip()
    hash_pwd = hashlib.md5(inp_pwd.encode("utf-8")).hexdigest()
    with open(r'user.txt', mode='rt', encoding="utf-8") as f:
        res = json.load(f)
        if inp_name == res.get("user_name") and hash_pwd == res.get("user_pwd"):
            print("登录成功")
        else:
            print("用户名或密码错误！！！")
        # for line in f:
            # name, pwd = line.strip().split(":")
            # if name == inp_name:
            #     print("用户名正确!!!!")
            #     if hash_pwd == pwd:
            #         print("密码也正确!!!!")
            #     else:
            #         print("密码错误")

login()


# 2、文件完整性校验（考虑大文件）
'''
1、全部文件内容进行hash之后 检验hash是否一致
2、只检验文件的前1000个字符 hash之后是否一致
3、取文件的开始位置的200个字符  五分之一处的200个字符 五分之二处的200个字符  
五分之三处的200个字符  五分之四处的200个字符 
然后进行hash 判断hash值是否一致 如果一致 代表文件是完整的
'''

