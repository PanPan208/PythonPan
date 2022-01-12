# @time: 2022/1/11 5:13 PM
# Author: pan
# @File: login.py
# @Software: PyCharm

from conf import setting

user_info = []

def get_user_info():
    if len(user_info) != 0:
        return

    with open(f'{setting.BASE_DIR}/db/db.txt', mode="rt", encoding="utf-8") as f:
        for line in f:
            name, pwd, money = line.strip().split(":")
            user_info.append({
                "name": name,
                "pwd": pwd,
                "money": int(money)
            })


def is_register(name, user_info: list):
    for dic in user_info:
        if name == dic.get("name"):
            return True
    else:
        return False


def register():
    """
    用户注册功能 如果已经存在用户 不能再进行注册
    :return:
    """
    get_user_info()
    print(user_info)
    while True:
        inp_name = input("请输入用户名:").strip()
        if is_register(inp_name, user_info):
            print("已经注册过了！ 亲")
            continue

        inp_pwd = input("请输入密码:").strip()
        if not inp_pwd.isdigit():
            print("密码请使用数字型! 亲")
            continue

        user_info.append({
            "name": inp_name,
            "pwd": inp_pwd,
            "money": 0
        })
        with open(f'{setting.BASE_DIR}/db/db.txt', mode="at", encoding="utf-8") as f:
            f.write(f'\n{inp_name}:{inp_pwd}:0')
            break


