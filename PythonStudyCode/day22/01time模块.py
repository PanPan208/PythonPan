# @time: 2022/1/12 5:33 PM
# Author: pan
# @File: 01time模块.py
# @Software: PyCharm
"""
时间模块优先掌握的操作
"""
import time

# 1、时间戳
# 时间戳是从1970年开始到当前时间的一共时间的秒数或毫秒数
# 作用：主要用于时间计算
print(time.time())
print(type(time.time()))
# 1642040649.822137
# <class 'float'>


# 2、按照某种格式显示的时间
# %X 和 %H:%M:%S  效果一样
# %p 显示是上午还是下去 AM/PM
print(time.strftime('%Y:%m:%d %X'))
print(time.strftime('%Y:%m:%d %H:%M:%S %p'))

# 3、结构化时间 获取的是本地时间也就是 UTC+8
# time.localtime(secs=)
# 如果不提供secs 那么默认就是当前时间的时间戳
# 可以用于获取时间的某一部分
# time.struct_time(tm_year=2022, tm_mon=1,
# tm_mday=13, tm_hour=10, tm_min=27, tm_sec=19,
# tm_wday=3, tm_yday=13, tm_isdst=0)
# DST (Daylight Saving Time) 夏令时
res = time.localtime()
print(res)
print(res.tm_year)
print(res.tm_mon)
# UTC时间 格林尼治时间 世界时
# 不传如secs默认是当前时间
# 时间比中国的本地时间少8个小时
print(time.gmtime())


# 世界时间和本地时间
# 中国时区和世界时间也就是格林尼治时间相差8个小时
# 中国位于东8区
# print(time.localtime())
# print(time.localtime(333333333))
# print(time.gmtime())
# print(time.gmtime(333333333))


"""
时间模块需要掌握的操作
"""
print("============================")
# # 1、struct_time时间 ========>  时间戳
# s_time = time.localtime()
# print(s_time)
# 将结构化时间转换为时间戳
# print(time.mktime(s_time))
#
# # 2、时间戳 =========== struct_time
# tp_time = time.time()
# print(tp_time)
# 将对应的时间戳转换为结构化时间
# print(time.localtime(tp_time))


print("============================")
# # 1、struct_time ==============》 字符串时间
# s_time = time.localtime(3333333)
# print(s_time)
# 结构化时间转换为字符串时间 strftime
# print(time.strftime('%Y:%m:%d %X', s_time))
#
# # 2、 字符串时间 ================ 》  struct_time
# 字符串转换为结构化时间 strptime
# print(time.strptime('1980:01:02 10:22:22', '%Y:%m:%d %H:%M:%S'))


# ======================  需要掌握  ====================
# 1、字符串时间 转换为 时间戳
# 字符串时间 -》 struct_time -》 时间戳
str = '1980:01:02 10:22:22'
s_time = time.strptime(str, '%Y:%m:%d %H:%M:%S')
print(s_time)
tp_time = time.mktime(s_time)
print(tp_time)

# 2、时间戳 转换为 字符串时间
# 时间戳 - struct_time - 字符串
res = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(tp_time))
print(res)


# ================================
# 休息一段时间
# time.sleep(3)

# 英语格式的时间
# 传入的是结构化的时间
# 不传值 默认是time.localtime()
print(time.asctime())
print(time.asctime(time.localtime()))
# Thu Jan 13 10:27:22 2022
# 转换为英语格式的时间
# 需要传入的值是时间戳样式的
print(time.ctime())
print(time.ctime(time.time()))
