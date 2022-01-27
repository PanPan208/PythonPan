# @time: 2022/1/21 3:48 PM
# Author: pan
# @File: shop_interface.py
# @Software: PyCharm

import json
from conf import settings
from db import db_handle


# 获取商品列表
def get_shopping_list_interface():
    with open(settings.SHOPPING_DATA_PATH, mode="rt", encoding="utf-8") as f:
        shop_dic = json.load(f)
        return shop_dic


# 请求保存购物车功能
def save_shop_car_interface(user_name, shop_car):
    # 1、获取用户信息
    user_dic = db_handle.select_user(user_name)
    # 2、修改用户商品信息
    user_dic['shop_car'] = shop_car
    # 3、保存用户商品信息
    db_handle.save_user(user_dic)


# 请求购买商品 也就是清空购物车
def pay_shop_car_interface(user_name):
    # 1、获取用户信息
    user_dic = db_handle.select_user(user_name)
    # 2、修改用户商品信息
    shop_car = user_dic['shop_car']
    # 3、购物车一共需要多少钱购买
    total_money = 0
    for key, value in shop_car.items():
        total_money += value[0] * value[1]
    balance = int(user_dic['balance'])
    # 4、用户余额不足购买
    if balance < total_money:
        return False, f'用户:{user_name}, 金额不足! 请充值后再进行购买'
    # 5、用户有足够的钱 进行购买 扣除金额 进行购买
    balance -= total_money
    user_dic['balance'] = balance
    # 6、购买之后 更新用户信息
    db_handle.save_user(user_dic)
    return True, f'用户:{user_name} 购买成功'
