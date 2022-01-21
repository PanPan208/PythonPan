# @time: 2022/1/20 3:10 PM
# Author: pan
# @File: 02logging模块2.py
# @Software: PyCharm
"""
logging模块中的内容

#logger：产生日志的对象
#Filter：过滤日志的对象
#Handler：接收日志然后控制打印到不同的地方，
FileHandler用来打印到文件中，StreamHandler用来打印到终端
#Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，
以此来控制不同的Handler的日志格式
"""

import logging

# 一般不常用这种方式 而是使用一个LOGGING_DIC字典

# 1、产生一个logger对象
logger = logging.getLogger(__file__)

# 2、 Filer对象  过滤相关不常用
# logger.filter()

# 3、Handler对象 接收logger传来的日志 然后控制输出
handler1 = logging.FileHandler('t1.log')  # 打印到文件t1
handler2 = logging.FileHandler('t2.log')  # 打印到文件t2
handler3 = logging.StreamHandler()  # 打印到终端

# 4、Formatter对象：日志格式
formmater1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                               datefmt='%Y-%m-%d %H:%M:%S %p',)
formmater2 = logging.Formatter('%(asctime)s :  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',)
formmater3 = logging.Formatter('%(name)s %(message)s',)

# 5、为Handler绑定格式对象
handler1.setFormatter(formmater1)
handler2.setFormatter(formmater2)
handler3.setFormatter(formmater3)

# 设置等级
handler1.setLevel(20)


# 6、将Handle添加到logger上
logger.addHandler(handler1)
logger.addHandler(handler2)
logger.addHandler(handler3)

# 设置等级
logger.setLevel(10)

# logger和handler都可以设置levael
# 但是要注意他们的等级
# Logger is also the first to filter the message based on a level
# — if you set the logger to INFO, and all handlers to DEBUG,
# you still won't receive DEBUG messages on handlers
# — they'll be rejected by the logger itself.
# If you set logger to DEBUG, but all handlers to INFO,
# you won't receive any DEBUG messages either
# — because while the logger says "ok, process this",
# the handlers reject it (DEBUG < INFO).

# 7、测试
logger.debug("测试debug")
logger.info("测试info")
logger.warning("测试警告信息warning")
logger.error("测试错误信息")
logger.critical("严重错误")







