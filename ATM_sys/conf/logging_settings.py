# @time: 2022/1/17 4:40 PM
# Author: pan
# @File: settings.py
# @Software: PyCharm
"""
日志配置字典 LOGGING_DIC
"""

import os
from conf import settings

# 格式 - 可以用于定义日志输出的格式
# 1、定义三种日志输出格式，日志中可能用到的格式化串如下
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息

# 2、强调：其中的%(name)s为getlogger时指定的名字
# 标准样式
standard_format = '%(asctime)s - %(threadName)s:%(thread)d - ' \
                  '日志名字:%(name)s - %(filename)s:%(lineno)d -' \
                  '%(levelname)s - %(message)s'

# 简单样式
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

# 测试样式
test_format = '[%(asctime)s] %(message)s'


# 3、日志配置字典
LOGGING_DIC = {
    # 版本
    'version': 1,
    # ？
    'disable_existing_loggers': False,
    # 日志输出样式设置
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    # 过滤日志对象
    'filters': {},
    # handlers是日志的接收者 不同的handlers会将日志输出到不同的位置
    'handlers': {
        # 打印到控制台的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕控制台
            'formatter': 'simple',
        },
        # 打印到文件的日志
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',  # 保存到文件
            'filename': settings.LOG_PATH,
            # os.path.join(os.path.dirname(os.path.dirname(__file__)),'log','a2.log')
            'encoding': 'utf-8',
            'formatter': 'test',
        },
        # 默认打印日志
        'default': {
            'level': 'DEBUG',
            # 使用日志轮转文件 大于某一个值的时候 会将日志保存的其他文件中
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            # 'maxBytes': 1000,  # 默认单位是kb
            'backupCount': 5,  # 轮转文件的个数
            'filename': settings.LOG_PATH,
            # os.path.join(os.path.dirname(os.path.dirname(__file__)),'log','a2.log')
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
    },
    # loggers是日志的产生者，产生的日志会传递给handler然后控制输出
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        'kkk': {
            'handlers': ['console', 'file'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '终端提示': {
            'handlers': ['console', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        # '' 如果未发现对应的日志名称 会默认到该日志配置上
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
    },
}








