# @time: 2022/1/12 5:51 PM
# Author: pan
# @File: 02datetime模块.py
# @Software: PyCharm
"""
日期时间模块
"""
import datetime
# 本地时间 localtime
print(datetime.datetime.now())
# 对时间进行运算
# 可以是 + 多少天  几周 几个小时等等
print(datetime.datetime.now() + datetime.timedelta(days=3))
print(datetime.datetime.now() + datetime.timedelta(weeks=1))
print(datetime.datetime.now() + datetime.timedelta(hours=5))

# UTC时间
# 比本地时间也就是now时间少8个小时
print(datetime.datetime.utcnow())

# 将时间戳转换为字符串格式的时间
# 字符串的格式是固定的
print(datetime.datetime.fromtimestamp(333333333))

# ==============================  其他属性和方法


# 1、datetime相关属性
# 常量 最大年份 9999
print(datetime.MAXYEAR)
# 常量 最小年份 1
print(datetime.MINYEAR)


# 2、date类型
# 获取当前的日期
tod = datetime.date.today()
print(tod)  # 2022-01-13
print(tod.year)  # 2022
print(tod.month)  # 1
print(tod.day)  # 13
print(tod.__getattribute__('year'))
print(tod.__getattribute__('month'))
print(tod.__getattribute__('day'))

# 3 日期时间之间的比较
a = datetime.date(year=2022, month=1, day=1)
b = datetime.date(year=2022, month=1, day=3)
# equal 等于  a == b
print(a.__eq__(b))
# not equal 不等于  a != b
print(a.__ne__(b))
# g equal  大于等于  a >= b
print(a.__ge__(b))
# g 大于  a > b
print(a.__gt__(b))
# less equal 小于等于 a <= b
print(a.__le__(b))
# less 小于  a < b
print(a.__lt__(b))


# 4、获取两个时间相差多少天
print(a.__sub__(b))
print(a.__rsub__(b))
print(a.__sub__(b).days)


# 5 ISO 标准化时间
a = datetime.date.today()
print(a.isocalendar())
# 返回的一个元组 包含三个值
# year年数 - week number 一年的第几周 - week day 一周的第几天
# (2021, 52, 6)
print(a.isocalendar()[0])
print(a.isocalendar()[1])
print(a.isocalendar()[2])
# iso 8601标准时间
print(a.isoformat())
# 2022-01-13
# iso 标准时间  当前一周的第几天
# 周一1 ... 周日7
print(a.isoweekday())
# 周一为0 ... 周六为6
print(a.weekday())


# 6 返回结构化时间 和 struct time类似
print(a.timetuple())
print(a.timetuple().tm_year)
print(a.timetuple().tm_mon)


# 7 返回公元公历到现在的天数  公元1年1月1日为1
print(a.toordinal())
# 738168
n = a.toordinal()
# 将公历天数转换为时间
print(datetime.date.fromordinal(n))
# 2022-01-13

# 8 replace 替换产生一个原先的日期对象
# 不会改变原先的对象
b = a.replace(year=2020, month=1, day=1)
print(a)
print(b)


# 9 使用给定的时间戳 转换为时间
import time
t = time.time()
print(datetime.date.fromtimestamp(t))


# 10 返回当前时间 最大/最小时间
print(datetime.date.today())
# 2022-01-13
print(datetime.date.max)
# 9999-12-31
print(datetime.date.min)
# 0001-01-01


print("=====================  11 ")
# 11 日期的字符串输出
print(a.__format__('%Y-%m=%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%y-%m-%d'))
print(a.__format__('%D'))
# 01/13/22 固定格式
# 于format等价的是 strftime
print(a.strftime('%Y-%m/%d'))
# 只是简单的获取日期的字符串样式
print(a.__str__())
# 2022-01-13
# 获取英语格式的时间
print(a.ctime())
# Thu Jan 13 00:00:00 2022


# time
print("===================  time  ======================= ")
print("time".center(100, '='))
# 1 time 有 小时/分钟/秒/毫秒/时区信息
t = datetime.time(hour=10, minute=20, second=40, microsecond=888)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print(t.tzinfo)

# 2 根据属性获取对应的字段
print(t.__getattribute__('hour'))

# 3 时间之间的比较
t2 = datetime.time(11, 20, 30, 111)
print(t.__eq__(t2))


# 4 最大时间值
print(datetime.time.max)  # 23:59:59.999999
# 最小时间值
print(datetime.time.min)  # 00:00:00
# 时间间隔的最小单位
print(datetime.time.resolution)  # 0:00:00.000001


# datetime类
print("datetime".center(100, '='))
# datetime可以看成是date和time的合成体
# 其中大部分的属性和方法都是继承这个类的


# 1 获取当前时间
a = datetime.datetime.now()
print(a)
# 返回date
print(a.date())
# 返回time
print(a.time())
# 返回UTC 的结构化时间格式
print(a.utctimetuple())

# 2 可以使用一个date和一个time合并成一个datetime类
# combine
b = datetime.datetime.combine(a.date(), a.time())
print(b)


# 3 返回本地时间
print(datetime.datetime.now())
# 返回utc时间 相差8个小时
print(datetime.datetime.utcnow())


# 4 将一个字符串转换为datetime对象
print(datetime.datetime.strptime('2010-11-11 11:22:11', '%Y-%m-%d %H:%M:%S'))
# 2010-11-11 11:22:11


# 5 使用一个时间戳转换为datetime对象
print(datetime.datetime.utcfromtimestamp(time.time()))
# 2022-01-13 06:29:59.840243


