# @time: 2022/1/14 4:43 PM
# Author: pan
# @File: 作业1.py
# @Software: PyCharm

# 1、把登录与注册的密码都换成密文形式
import hashlib
import json
import os

user_dic = {}


def get_user(name):
    """
    根据用户名获取数据库中的用户信息
    :param name: 用户名
    :return: 用户信息
    """
    with open(r'user.txt', mode="rt", encoding="utf-8") as f:
        # 获取文件中的用户json信息
        res = json.load(f)
        global user_dic
        user_dic = res
        print(res, type(res))
        if res.get("user_name") == name:
            return res
        else:
            return None

# print(get_user("pan"))


def md5_pwd(pwd):
    """
    对密码进行加密
    :param pwd:
    :return:
    """
    # 对密码进行加密 无盐状态
    # hash_pwd = hashlib.md5(inp_pwd.encode("utf-8")).hexdigest()
    # 加密 加盐
    m = hashlib.md5()
    m.update(pwd.encode("utf-8"))
    m.update("天王盖地虎,上山抓老鼠".encode("utf-8"))
    hash_pwd = m.hexdigest()
    return hash_pwd


def register():
    """
    用户注册功能
    :return:
    """
    while True:
        inp_name = input("请输入用户名:").strip()
        # 判断用户有没有存在  如果存在 提示重新输入
        user_dict = get_user(inp_name)
        if user_dict:
            print("该用户已经存在, 请重新输入")
            continue

        inp_pwd = input("请输入密码:").strip()
        re_inp_pwd = input("请输入确认密码:").strip()
        if inp_pwd != re_inp_pwd:
            print("两次输入的密码不一致,请重新输入")
            continue

        # 对密码进行加密
        hash_pwd = md5_pwd(inp_pwd)
        print(inp_name, hash_pwd)
        # 将用户名密码写入到数据库中
        # 可以使用之前的文本格式 name:pwd:money 的格式进行存储
        # 也可以使用json进行存储
        user_dic = {"user_name": inp_name,
                    "user_pwd": hash_pwd,
                    "user_balance": 1000}
        with open(r'user.txt', mode="wt", encoding="utf-8") as f:
            json.dump(user_dic, f)
            break

# register()


def login():
    """
    登录功能
    :return:
    """
    while True:
        inp_name = input("请输入用户名:").strip()
        user_dict = get_user(inp_name)
        if not user_dict:
            print("输入的用户名不存在, 请重新输入！！！")
            continue

        inp_pwd = input("请输入密码:").strip()
        hash_pwd = md5_pwd(inp_pwd)
        if user_dict.get("user_pwd") == hash_pwd:
            print("登录成功")
            break
        else:
            print("密码错误！！！")


# login()


# 2、文件完整性校验（考虑大文件）
'''
1、全部文件内容进行hash之后 检验hash是否一致
2、只检验文件的前1000个字符 hash之后是否一致
3、取文件的开始位置的200个字符  五分之一处的200个字符 五分之二处的200个字符  
五分之三处的200个字符  五分之四处的200个字符 
然后进行hash 判断hash值是否一致 如果一致 代表文件是完整的
'''
def check_file(file_path):
    """
    大文件校验完整性
    :param file_path:
    :return:
    """
    file_size = os.path.getsize(file_path)
    offset0 = 0
    offset1 = file_size // 5
    offset2 = file_size // 5 * 2
    offset3 = file_size // 5 * 3
    offset4 = file_size // 5 * 4
    print(file_size, offset1, offset2, offset3, offset4)
    file_size_list = [offset0, offset1, offset2, offset3, offset4]
    with open(r"aaa.txt", mode="rt", encoding="utf-8") as f:
        res = ''
        for offset in file_size_list:
            f.seek(offset)
            res += f.read(10)
            print(res)
        file_hash_pwd = md5_pwd(res)
        return file_hash_pwd


res = check_file(r"/Users/izzld/Desktop/PythonPan/PythonStudyCode/day23/作业/aaa.txt")
print(res)
# 拿到文件的hash值 预设的hash值 是否一致， 如果一致说明文件是完整的
# bc75f8565c04e9a6435665a52f5b21c0


