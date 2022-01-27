# @time: 2022/1/21 3:46 PM
# Author: pan
# @File: settings.py
# @Software: PyCharm
"""
项目配置文件
"""

import os

# ATM项目根路径
BASE_PATH = os.path.dirname(
    os.path.dirname(__file__)
)

# 获取user_data的文件路径
USER_DATA_PATH = os.path.join(BASE_PATH, 'db', 'user_data')


# 日志存储路径
LOG_PATH = os.path.join(BASE_PATH, 'log', 'log.log')

# 商品路径
SHOPPING_DATA_PATH = os.path.join(BASE_PATH, 'db', 'shop_data', 'shop_data.json')




