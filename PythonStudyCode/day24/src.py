# @time: 2022/1/17 5:50 PM
# Author: pan
# @File: src.py
# @Software: PyCharm
import logging
"""
logging模块的使用

"""

import settings

# import logging

# config/getLogger
# 不在logging模块的init文件中
# 所以需要单独进行导入
from logging import config
from logging import getLogger

# 或使用该种方式导入 会将getLogger一起导入
# 使用的时候需要带上前缀
# import logging.config
# logging.getLogger()

# 配置logging字典
config.dictConfig(settings.LOGGING_DIC)


# 获取kkk配置logger
# logger1 = getLogger('kkk')
# logger1.info("这是一条info信息")


# logger配置 只会在终端输出
# logger2 = getLogger('终端提示')
# logger2.info("这是一条info信息 只会在终端输出")


# 因为未找到对应的logger名称 所以会匹配到 ''
logger3 = getLogger('用户交易信息')
logger3.info("这是一条用户交互信息")





