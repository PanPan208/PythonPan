# @time: 2022/1/21 3:46 PM
# Author: pan
# @File: src.py
# @Software: PyCharm
"""
核心代码文件
=
用户视图层代码
"""

from interface import user_interface
from interface import bank_interface
from lib import common

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
        # 2 小的逻辑判断
        if inp_password == re_inp_password:
            # 两次输入的密码一致 然后请求注册接口
            flag, msg = user_interface.interface_register(inp_username, inp_password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("两次输入的密码不一致！请重新输入")
            continue


# 2、登录功能
def login():
    while True:
        # 1、输入登录用户名以及密码
        inp_username = input("请输入用户名:").strip()
        inp_password = input("请输入密码:").strip()
        # 2、调用登录接口
        flag, msg = user_interface.interface_login(inp_username, inp_password)
        print(msg)
        if flag:
            global login_user
            login_user = inp_username
            break

# 3、查看余额
# @common.login_auth
def check_balance():
    pass
    # # 1.直接调用查看余额接口，获取用户余额
    # balance = user_interface.check_bal_interface(
    #     login_user
    # )
    # print(f'用户{login_user} 账户余额为: {balance}')


# 4、提现功能
# @common.login_auth
def withdraw():
    pass
    # while True:
    #     # 1) 让用户输入提现金额
    #     input_money = input('请输入提现金额: ').strip()
    #
    #     # 2) 判断用户输入的金额是否是数字
    #     if not input_money.isdigit():
    #         print('请重新输入')
    #         continue
    #
    #     # 3) 用户提现金额，将提现的金额交付给接口层来处理
    #     flag, msg = bank_interface.withdraw_interface(
    #         login_user, input_money
    #     )
    #
    #     if flag:
    #         print(msg)
    #         break
    #     else:
    #         print(msg)


# 5、还款功能
# @common.login_auth
def repay():
    pass


# 6、转账功能
# @common.login_auth
def transfer():
    pass


# 7、查看流水
# @common.login_auth
def check_flow():
    pass


# 8、购物功能
# @common.login_auth
def shopping():
    pass


# 9、查看购物车
# @common.login_auth
def check_shop_car():
    pass


# 10、管理员功能
def admin():
    pass


# 创建函数功能字典
func_dic = {
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


def run():
    """
    视图层 类似web前端/移动端功能
    :return:
    """
    while True:
        print("""
        ============ ATM + 购物车 ==========
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
        inp_cmd = input("请输入指令代码:").strip()
        if inp_cmd not in func_dic:
            print("请输入正确的指令!!!")
            continue
        func_dic.get(inp_cmd)()


