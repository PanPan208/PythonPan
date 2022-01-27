# @time: 2022/1/21 3:47 PM
# Author: pan
# @File: db_handle.py
# @Software: PyCharm
"""
对数据的相关操作
比如对数据的增删改查
"""

import os
import json
from conf import settings


# 根据用户名查询用户是否存在
def select_user(username):
    # 1、用户信息文件路径 用户名.json
    username_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )

    # 2、判断用户文件是否已经存在
    if os.path.exists(username_path):
        # 有文件 返回文件中的用户信息  没有文件默认返回None
        with open(username_path, mode="rt", encoding="utf-8") as f:
            user_dic = json.load(f)
            return user_dic
    # 默认返回None


# 保存用户信息json
def save_user(user_dic):
    # 1、用户信息文件路径 用户名.json
    username = user_dic.get("username")
    username_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )

    # 2、将用户信息进行存储到文件夹 user_data中 一个用户使用一个json文件
    # 存储格式 用户名.json, pan.json, zhao.json
    with open(username_path, mode="wt", encoding="utf-8") as f:
        # 3、ensure_ascii=False 让文件中的中文显示更加美观
        json.dump(user_dic, f, ensure_ascii=False)

