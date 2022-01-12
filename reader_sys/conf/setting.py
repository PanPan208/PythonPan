# @time: 2022/1/12 10:07 AM
# Author: pan
# @File: setting.py
# @Software: PyCharm
"""
一些公共配置文件
"""
import os

# 项目跟目录路径
# __file__ 当前文件的绝对路径
# dirname 文件的路径名
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

# 数据文件的绝对路径
DB_PATH = os.path.join(ROOT_PATH, "db")
USER_DB_PATH = os.path.join(DB_PATH, "db.txt")
USER_TEMP_DB_PATH = os.path.join(DB_PATH, "temp.txt")
# 小说数据文件路径
FICTION_PATH = os.path.join(DB_PATH, "fiction")
STORY_LIST_PATH = os.path.join(DB_PATH, "story_class.txt")

# 日志记录路径
LOG_PATH = os.path.join(ROOT_PATH, "log/log.txt")

