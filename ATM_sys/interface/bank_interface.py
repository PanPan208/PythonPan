# @time: 2022/1/21 3:48 PM
# Author: pan
# @File: bank_interface.py
# @Software: PyCharm
"""
银行相关接口
"""
from db import db_handle

from logging import config
from logging import getLogger
from conf import logging_settings

config.dictConfig(logging_settings.LOGGING_DIC)
logger = getLogger("银行流水")


# 提现接口(手续费5%)
def withdraw_interface(username, money):
    # 1 获取用户信息
    user_dic = db_handle.select_user(username)
    # 2、用户当前金额
    user_balance = int(user_dic.get('balance'))
    # 3、提现金额+手续费后的金额
    money2 = int(money) * 1.05

    # 4、判断余额中的钱够不够提现
    # 金额不够提现
    if user_balance < money2:
        msg = f"用户{username}: 余额不足！"
        # 5 记录日志
        logger.info(msg)
        return False, msg

    # 5、够提现 直接提现
    user_balance -= money2
    # 6、更新用户信息
    user_dic['balance'] = user_balance
    # 7、记录日志
    msg = f'用户{username}: 提现金额:${money}, 手续费为：${money2 - int(money)}'
    logger.info(msg)
    user_dic['flow'].append(msg)
    db_handle.save_user(user_dic)
    return True, msg


# 还款/充值接口
def repay_interface(username, inp_money):
    # 1 获取用户信息
    user_dic = db_handle.select_user(username)
    # 2、用户当前金额
    user_balance = int(user_dic.get('balance'))
    # 3、充值金额
    money = int(inp_money)

    # 4 充值
    user_balance += money
    # 5、更新用户信息
    user_dic['balance'] = user_balance
    # 6、记录日志
    msg = f'用户{username}: 充值金额为:${money}, 充值后余额为：${user_balance}'
    logger.info(msg)
    user_dic['flow'].append(msg)
    db_handle.save_user(user_dic)
    return True, msg


# 转账功能
def transfer_interface(username, to_user, to_money):
    # 1 获取当前用户信息
    user_dic = db_handle.select_user(username)
    # 转账用户的信息
    to_user_dic = db_handle.select_user(to_user)
    if not to_user_dic:
        msg = f'用户{to_user}: 不存在！！！'
        logger.warning(msg)
        return False, msg

    # 2、当前用户金额
    user_balance = int(user_dic.get('balance'))
    # 转账用户的金额
    to_user_balance = int(to_user_dic.get('balance'))
    # 3、转账的金额 并判断用户是否有足够的金额进行转账
    money = int(to_money)
    if user_balance < money:
        msg = f"用户{username}: 余额不足"
        logger.warning(msg)
        return False, msg

    # 4、对用户以及转账的用户金额进行修改
    user_balance -= money
    to_user_balance += money
    user_dic['balance'] = user_balance
    to_user_dic['balance'] = to_user_balance

    # 5、记录日志
    msg = f'转账成功！用户[{username}]:给用户[{to_user}]: 转账了${money}。'
    logger.info(msg)
    user_dic['flow'].append(msg)
    # 6、保存信息
    db_handle.save_user(user_dic)
    db_handle.save_user(to_user_dic)
    return True, msg


