# @time: 2022/1/14 5:30 PM
# Author: pan
# @File: 01logging模块.py
# @Software: PyCharm
"""
日志模块
"""

import logging

logging.basicConfig(
    # 1、日志输出的文件位置 终端/文件
    # 如果不设置默认是终端显示
    # filename="access.log",
    # 文件的读写方式 默认是'a'追加模式 也可以改为'w'
    filemode='a',

    # 2、日志显示的内容格式  可以自己设置
    # asctime - name - levelname - module: message
    # 时间 - 用户名 - 错误名称 - 出现错误的模块 ： 错误信息
    # 2022:01:14 17:36:51 PM - root - ERROR - 05logging模块: 出现error错误 等级40
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',

    # 3、日期格式
    datefmt="%Y:%m:%d %H:%M:%S %p",

    # 4 日志等级
    # 只会显示大于等于设置的等级的logging信息
    # 如果不设置 默认设置的等级是30
    # critical = 50
    # error = 40
    # warning = 30
    # info = 20
    # debug = 10
    level=10,

    # 5
    # stream：用指定的stream创建StreamHandler。
    # 可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。
    # 若同时列出了filename和stream两个参数，则stream参数会被忽略。
)

logging.NOTSET
logging.debug("调试出现的bug 等级是10")
logging.info("消息信息 等级20")
logging.warning("警告信息 等级是30")
logging.error("出现error错误 等级40")
logging.critical("出现了严重的bug！！！！ 等级是50")



