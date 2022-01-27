# @time: 2022/1/21 3:48 PM
# Author: pan
# @File: user_interface.py
# @Software: PyCharm
"""
逻辑接口层
用户相关接口
"""
import os
import json
from lib import common
from db import db_handle
from conf import settings

from logging import config
from logging import getLogger
from conf import logging_settings

config.dictConfig(logging_settings.LOGGING_DIC)
logger = getLogger("用户相关日志")


# 注册接口
def register_interface(username, password, balance=1000):
    """
    注册接口 首先判断用户是否已经存在 如果已经存在提示注册失败
    如果用户不存在再进行注册
    密码需要使用md5进行加密
    :param username:
    :param password:
    :param balance:
    :return:
    """
    user_dic = db_handle.select_user(username)
    if user_dic:
        # 1、如果返回的是一个字典 说明已经有该用户的数据了
        msg = f"用户名: {username} 已经存在"
        logger.warning(msg)
        return False, msg

    # 2、用户名不存在 继续进行注册
    # 3、首先对密码进行加密
    md5_password = common.get_pwd_md5(password)

    # 4、组织用户信息json数据
    user_dic = {
        'username': username,
        'password': md5_password,
        'balance': balance,
        # 用于记录用户流水的列表
        'flow': [],
        # 用于记录用户购物车
        'shop_car': {},
        # locked：用于记录用户是否被冻结
        # False: 未冻结   True: 已被冻结
        'locked': False
    }
    # 5、保存流水日志
    msg = f'用户：{username} 注册成功'
    logger.info(msg)
    user_dic['flow'].append(msg)
    # 6、保存用户信息到对应的文件
    db_handle.save_user(user_dic)
    return True, msg


# 登录接口
def login_interface(username, password):
    # 1、获取用户信息
    user_dic = db_handle.select_user(username)
    # 2、用户存在可以进行登录
    if user_dic:
        if user_dic.get('locked'):
            msg = f"用户:{username} 已经被冻结了不能进行登录哦!!!"
            return False, msg

        # 3、判断加密后的密码使否一致
        password = common.get_pwd_md5(password)
        user_password = user_dic.get("password")
        # 4、密码一致 登录成功
        if password == user_password:
            msg = f'用户: {username} 登录成功'
            logger.info(msg)
            return True, msg
        else:
            msg = f"用户： {username} 密码输入错误"
            logger.error(msg)
            return False, msg
    else:
        msg = f"用户： {username} 不存在"
        logger.warning(msg)
        return False, msg


# 查看用户余额
def check_balance_interface(username):
    # 1、获取用户信息
    user_dic = db_handle.select_user(username)
    # 2、返回该用户的金额 需要什么返回什么
    return user_dic.get("balance")


# 查看流水flow
def check_flow_interface(username):
    # 1、获取用户信息
    user_dic = db_handle.select_user(username)
    # 2、返回该用户的金额 需要什么返回什么
    return user_dic.get("flow")


# 查看购物车信息
def check_shop_list_interface(username):
    # 1、获取用户信息
    user_dic = db_handle.select_user(username)
    # 2、返回该用户的金额 需要什么返回什么
    return user_dic.get("shop_car")

