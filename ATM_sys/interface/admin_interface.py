# @time: 2022/1/26 3:08 PM
# Author: pan
# @File: admin_interface.py
# @Software: PyCharm

from db import db_handle
from interface import user_interface


# 查询某一个用户的余额
def admin_check_user_balance():
    while True:
        to_user_name = input("请输入需要查找的用户名:(输入q退出)").strip()
        if to_user_name == 'q' or to_user_name == 'Q':
            break

        # 1 先判断用户是否存在
        user_dic = db_handle.select_user(to_user_name)
        if not user_dic:
            print("请输入正确的用户名!!!")
            continue
        # 2 获取该用户的余额
        balance = user_interface.check_balance_interface(to_user_name)
        print(f"用户:{to_user_name}的当前余额为:${balance}")


# 冻结用户
def freeze_to_user_interface(to_user_name):
    # 1、获取用户信息
    user_dic = db_handle.select_user(to_user_name)
    # 2、修改用户信息
    user_dic['locked'] = True
    # 3、保存用户信息
    db_handle.save_user(user_dic)


# 冻结某一个用户
def admin_freeze_to_user():
    while True:
        to_user_name = input("请输入要冻结的用户名: 输入q/Q退出").strip()
        if to_user_name == 'q' or to_user_name == 'Q':
            break

        # 1 先判断用户是否存在
        user_dic = db_handle.select_user(to_user_name)
        if not user_dic:
            print("请输入正确的用户名!!!")
            continue

        # 2 请求冻结某一个用户
        freeze_to_user_interface(to_user_name)
        print(f"用户:{to_user_name}已被冻结")
        break


# 添加账户/注册功能
def admin_register():
    pass


admin_func = {
    "0": admin_register,
    "1": admin_check_user_balance,
    "2": admin_freeze_to_user
}


def admin():
    while True:
        print("""
        =========== 欢迎进入管理员页面 ==========
            0: 添加账户
            1: 用户额度
            2: 冻结账户
        ================= end ================
            """)
        # 1、输入功能编号
        cmd = input("请输入管理编号:").strip()
        if not cmd.isdigit():
            print("请输入数字编号!!!")
            continue
        if cmd not in admin_func:
            print("请输入正确的编号!!!")
            continue
        # 调用函数
        admin_func[cmd]()
