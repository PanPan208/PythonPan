# @time: 2022/1/10 6:10 PM
# Author: pan
# @File: setting.py
# @Software: PyCharm

# 配置文件 一般是设置一些基础常量、define等

import os

# 项目包的路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# log日志文件的路径
LOG_PATH = r'%s/log/user.log' % BASE_DIR