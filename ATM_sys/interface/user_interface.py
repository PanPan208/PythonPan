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


# 注册接口
def interface_register(username, password, balance=1000):
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
        return False, "用户名已经存在"

    # 用户名不存在 继续进行注册
    # 对密码进行加密
    md5_password = common.get_pwd_md5(password)

    # 组织用户信息json
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
    # 保存用户信息到对应的文件
    db_handle.save_user(user_dic)
    return True, f'{username} 注册成功'


# 登录接口
def interface_login(username, password):
    # 1、获取用户信息
    user_dic = db_handle.select_user(username)
    if user_dic:
        md5_pwd = common.get_pwd_md5(password)
        user_password = user_dic.get("password")
        # 密码一致 登录成功
        if md5_pwd == user_password:
            return True, f'{username} 登录成功'
        else:
            return False, "密码输入错误"
    else:
        return False, "用户名错误"


