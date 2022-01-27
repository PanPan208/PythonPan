# @time: 2022/1/21 3:46 PM
# Author: pan
# @File: src.py
# @Software: PyCharm
"""
用户视图层代码
"""

from interface import user_interface
from interface import bank_interface
from interface import shop_interface
from interface import admin_interface
from lib import common
from db import db_handle

# 全局变量，记录用户是否已登录
login_user = None


# 1、注册功能
def register():
    while True:
        # 1 输入用户名和密码
        inp_username = input("请输入用户名:").strip()
        inp_password = input("请输入密码:").strip()
        re_inp_password = input("请再次输入密码:").strip()
        # 用户注册的初始金额 也可以进行输入设置
        # inp_balance = input("请输入初始金额").strip()
        # 2 视图层做的小的逻辑判断 判断两次输入的密码是否一致
        if inp_password == re_inp_password:
            # 两次输入的密码一致 然后请求注册接口
            flag, msg = user_interface.register_interface(inp_username, inp_password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("两次输入的密码不一致！请重新输入")


# 2、登录功能
def login():
    while True:
        # 1、输入登录用户名以及密码
        inp_username = input("请输入用户名:").strip()
        inp_password = input("请输入密码:").strip()
        # 2、调用登录接口
        flag, msg = user_interface.login_interface(inp_username, inp_password)
        print(msg)
        if flag:
            global login_user
            login_user = inp_username
            break


# 3、查看余额
@common.login_auth
def check_balance():
    # 1、调用查询余额的接口
    balance = user_interface.check_balance_interface(login_user)
    print(f'用户{login_user}: 账户余额为:{balance}')


# 4、提现功能
@common.login_auth
def withdraw():
    while True:
        # 1、提示用于输入提现金额
        inp_money = input("请输入提现金额:").strip()

        # 2、判断输入的金额是否是数字
        if not inp_money.isdigit():
            print("请输入数字！！！")
            continue

        # 3 调用提现接口
        flag, msg = bank_interface.withdraw_interface(login_user, inp_money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 5、还款功能/充值功能 往银行卡里充钱
@common.login_auth
def repay():
    while True:
        # 1、提示用于输入充值金额
        inp_money = input("请输入充值金额:").strip()

        # 2、判断输入的金额是否是数字
        if not inp_money.isdigit():
            print("请输入数字！！！")
            continue

        # 3 调用充值接口
        flag, msg = bank_interface.repay_interface(login_user, inp_money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 6、转账功能
@common.login_auth
def transfer():
    while True:
        # 1、输入转账的用户以及转账金额
        to_user = input("请输入转账对象：").strip()
        to_money = input("请输入转账金额：").strip()
        # 2、判断输入的金额是否是数字
        if not to_money.isdigit():
            print("请输入数字金额!!!")
            continue
        # 3、请求转账接口 进行转账
        flag, msg = bank_interface.transfer_interface(
            login_user, to_user, to_money
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 7、查看流水 flow
@common.login_auth
def check_flow():
    flow_list = user_interface.check_flow_interface(login_user)
    # enumerate会将列表中的数据转换为 (index, value)的格式
    for value in enumerate(flow_list):
        print(f'用户流水信息为 >>>> {value}')


# 8、购物功能
@common.login_auth
def shopping():
    # 初始化商品购物车数据
    shop_car = {}  # {'商品名称': [单价, 数量]}
    shop_car = user_interface.check_shop_list_interface(login_user)

    while True:
        # 1、查询商品列表
        shop_dic = dict(shop_interface.get_shopping_list_interface())
        # print(shop_dic, type(shop_dic))

        # 商品信息为空
        if not shop_dic:
            print("商品信息为空，请联系管理员！！！")
            break

        # 2、显示商品列表
        print("============= 欢迎来到有趣商城 ===============")
        for key, value in shop_dic.items():
            print(f'>>>商品编号:{key}, 商品名称:{value[0]}, 商品价格:{value[1]}')
        print("================== end ====================")

        # 3、输入购买编号
        shop_no = input("请输入商品编号:").strip()
        # 4.1 输入的不是数字编号
        if not shop_no.isdigit():
            print("请输入数字编号!!!")
            continue

        # 4.2 判断商品编号是否存在
        if shop_no not in shop_dic:
            print("请输入正确的商品编号!!!")
            continue

        # 5、商品编号存在 获取商品单价和数量 {'商品名称': [单价, 数量]}
        shop_name = shop_dic[shop_no][0]
        shop_price = shop_dic[shop_no][1]
        if shop_car.get(shop_name):
            # 已经存在对应商品  数量+=1
            count = shop_car[shop_name][1]
            count += 1
            shop_car[shop_name] = [shop_price, count]
        else:
            # 商品不存在 数量 = 1
            shop_car[shop_name] = [shop_price, 1]

        # 6、直接加入购物车
        # 请求加入购物车的接口
        shop_interface.save_shop_car_interface(login_user, shop_car)

        # 输出当前已经添加的购物车信息
        print(f"当前购物车商品有: {shop_car}")

        # 7 询问是否去购买
        cmd = input("是否进行购买: (y 进行购买 n退出购买)").strip()
        if cmd == "y" or cmd == "Y":
            # 请求购买接口 购买单个商品/清空购物车
            print("直接购买")
            flag, msg = shop_interface.pay_shop_car_interface(login_user)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        if cmd == "n":
            print("已经退出商城")
            break


# 9、查看购物车
@common.login_auth
def check_shop_car():
    shop_car_dic = user_interface.check_shop_list_interface(login_user)
    for key, value in shop_car_dic.items():
        print(f">>>商品名称:{key}, 商品价格:{value[0]}, 商品个数:{value[1]}")

# 10、管理员功能
@common.login_auth
def admin():
    admin_interface.admin()


# 创建函数功能字典
func_dic = {
    '0': exit,
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin,
}


# 函数启动入口
def run():
    """
    视图层 类似web前端/移动端功能
    :return:
    """
    while True:
        print("""
        ============ ATM + 购物车 ==========
                0、退出系统
                1、注册功能
                2、登录功能
                3、查看余额
                4、提现功能
                5、还款功能
                6、转账功能
                7、查看流水
                8、购物功能
                9、查看购物车
                10、管理员功能
        ============ ATM + 购物车 ==========
        """)
        # 1、输入用户指令
        inp_cmd = input("请输入指令代码:").strip()
        # 2、判断指令使否在函数字典中
        if inp_cmd not in func_dic:
            print("请输入正确的指令!!!")
            continue
        # 3、有对应的指令 直接调用对应的方法
        func_dic.get(inp_cmd)()


