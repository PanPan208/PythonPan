# @time: 2021/12/10 4:00 下午
# Author: pan
# @File: ATM.py
# @Software: PyCharm

# 选做题：编写ATM程序实现下述功能，数据来源于文件db.txt
# 1、充值功能：用户输入充值钱数，db.txt中该账号钱数完成修改
# 2、转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱
# 3、提现功能：用户输入提现金额，db.txt中该账号钱数减少
# 4、查询余额功能：输入账号查询余额
db_data = {}


def update_db_data():
    """更新数据"""
    with open("db.txt", mode="rt") as f:
        for line in f:
            res = line.strip()
            name, money = res.split(":")
            # print(name, money)
            db_data[name] = int(money)
        print("当前账户的信息:", db_data)


def update_local_db_data():
    """更新文件中的数据"""
    with open("db.txt", mode="wt") as f:
        for key, value in db_data.items():
            f.write("{}:{}\n".format(key, value))


def is_avalide_user(name):
    """判断用户是否存在"""
    if db_data.get(name):
        return True
    else:
        return False


def re_charge():
    """充值功能"""
    while True:
        inp_name = input("请输入充值账户:").strip()
        if not is_avalide_user(inp_name):
            print("充值用户不存在,请重新输入充值用户!")
            continue
        inp_money = input("请输入充值金额:").strip()
        if not inp_money.isdigit():
            print("请输入数字金额:")
            continue
        # 可以进行充值
        db_data[inp_name] += int(inp_money)
        print(db_data)
        update_local_db_data()
        update_db_data()
        break


def tranfer_money():
    """转账功能：用户A向用户B转账1000元，db.txt中完成用户A账号减钱，用户B账号加钱"""
    while True:
        inp_name_a = input("请输入用户A:").strip()
        if not is_avalide_user(inp_name_a):
            print("用户A不存在!")
            continue
        inp_name_b = input("请输入用户B:").strip()
        if not is_avalide_user(inp_name_a):
            print("用户B不存在!")
            continue
        if inp_name_a == inp_name_b:
            print("不能给自己转账!")
            continue

        inp_money = input("请输入转账金额:").strip()
        if not inp_money.isdigit():
            print("请输入数字金额:")
            continue

        if db_data[inp_name_a] < int(inp_money):
            print("转账金额不能大于A账户的余额!")
            continue

        # 可以进行转账
        db_data[inp_name_a] -= int(inp_money)
        db_data[inp_name_b] += int(inp_money)
        print(db_data)
        update_local_db_data()
        update_db_data()
        break


def hand_out_money():
    """提现功能：用户输入提现金额，db.txt中该账号钱数减少"""
    while True:
        inp_name = input("请输入用户名:").strip()
        if not is_avalide_user(inp_name):
            print("该用户不存在!")
            continue

        inp_money = input("请输入提现金额:").strip()
        if not inp_money.isdigit():
            print("请输入提现数字金额:")
            continue

        if db_data[inp_name] < int(inp_money):
            print("提现金额过大!")
            continue

        # 可以提现
        db_data[inp_name] -= int(inp_money)
        print(db_data)
        update_local_db_data()
        update_db_data()
        break


def check_user_money():
    """查询余额功能：输入账号查询余额"""
    while True:
        inp_name = input("请输入用户名:").strip()
        if not is_avalide_user(inp_name):
            print("该用户不存在!")
            continue

        # 可以查询
        user_money = db_data[inp_name]
        print("用户当前账户余额为:", user_money)
        break

update_db_data()
# re_charge()

# tranfer_money()

# hand_out_money()

check_user_money()

# 选做题中的选做题：登录功能
# 用户登录成功后，内存中记录下该状态，上述功能以当前登录状态为准，必须先登录才能操作
