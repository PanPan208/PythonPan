# @time: 2022/1/14 3:20 PM
# Author: pan
# @File: 02configparser模块.py
# @Software: PyCharm
"""
configparser
获取配置文件中的信息 test.ini
# 一般很少进行修改配置文件中的设置
# 我们可以做一个设置界面 供用户进行修改配置文件

ini配置文件中的内容都是
key = value
或
key : value
的格式
"""

import configparser

config = configparser.ConfigParser()
config.read('test.ini')

# 1 获取setions的内容
print(config.sections())
# ['section1', 'section2']

# 2 获取某一个setions下的options
# 如果没有对应的section名字 会报错
# options获取的是section中的key的列表
print(config.options('section1'))


# 3、获取setions下的items
# key和value会组成一个元组 然后放到一个列表中
print(config.items('section1'))


# 获取指定key的value值
# get
name = config.get('section1', 'user')
print(name, type(name))

# getint
age = config.getint('section1', 'age')
print(age, type(age))

# getboll
admin = config.getboolean('section1', 'is_admin')
print(admin, type(admin))

# getfloat
salary = config.getfloat('section1', 'salary')
print(salary, type(salary))












