# @time: 2022/1/12 10:08 AM
# Author: pan
# @File: db_handle.py
# @Software: PyCharm
"""
对数据操作的功能
"""
import os
from conf import setting


# 根据用户名查询用户信息
def select_user(user_name):
    with open(setting.USER_DB_PATH, mode="rt", encoding="utf-8") as f:
        for line in f:
            user_data = line.strip().split(":")
            if user_data[0] == user_name:
                return user_data


# 添加注册用户
def add_user(user_name, user_pwd, user_money=0):
    with open(setting.USER_DB_PATH, mode="at", encoding="utf-8") as f:
        f.write(f'{user_name}:{user_pwd}:{user_money}\n')


# 更新用户信息
def update_user(old_data, new_data):
    with open(setting.USER_DB_PATH, mode="rt", encoding="utf-8") as r_f, \
            open(setting.USER_TEMP_DB_PATH, mode="wt", encoding="utf-8") as w_f:
        for line in r_f:
            if old_data == line:
                w_f.write(new_data)
            else:
                w_f.write(line)
    # 数据修改之后 将临时文件改为用户信息文件
    os.renames(setting.USER_TEMP_DB_PATH, setting.USER_DB_PATH)


# 获取小说列表数据
def select_story_list():
    with open(setting.STORY_LIST_PATH, mode="rt", encoding="utf-8") as f:
        # 将获取的数据str转换为对应的格式
        story_dic = eval(f.read())
        return story_dic


# 根据小说名字获取小说内容
def show_fiction_content(fiction_name):
    fiction_path = os.path.join(setting.FICTION_PATH, fiction_name)
    with open(fiction_path, mode="rt", encoding="utf-8") as f:
        res = f.read()
        return res


# 日志信息记录
def update_logging(msg):
    with open(setting.LOG_PATH, mode="at", encoding="utf-8") as f:
        f.write(msg)
        f.flush()
