# @time: 2022/1/20 10:51 AM
# Author: pan
# @File: re模块2.py
# @Software: PyCharm

import re

# 1、匹配所有的e
print(re.findall('e', 'alex make love'))

# 2、search只会找到第一个匹配内容 然后返回的是一个对象
# 使用group() 返回该对象的内容
print(re.search('e', 'alex make love').group())


# 3、match 只会在字符串的开头进行匹配 类似加了个^
# 如果没有匹配到内容返回None, 匹配到内容返回一个对象  同search
# 在字符串开始处进行匹配 可以使用search+^代替match
print("=====>", re.match('e', 'ealex make love').group())
# 同上面的match 返回一个None或一个对象
print("=====>", re.search('^e', 'ealex make love'))


# 4 split 分割
# 先按a进行分割 得到  ''  'bcde'
# 然后对'' 和 'bcde' 分别使用b进行分割  '' '' 'cde'
print(re.split('[ab]', 'abcde'))


# 5 sub 替换字符串中的内容
# sub后面不提供n 默认替换所有的a
print(re.sub('a', 'A', 'alex make love'))
# 指定n等于1 则只会替换第一个a
print(re.sub('a', 'A', 'alex make love', 1))
# 返回替换后的字符串和一共需要替换的个数 组成一个数组
# ('Alex mAke love', 2)
print(re.subn('a', 'A', 'alex make love'))


# 6 compile 返回匹配规则的一个对象
# \d 匹配所有的数字
# {2} 指定匹配的个数
# 指定匹配规则是 两个数字
obj = re.compile('\d{2}')
# 12
print(obj.search('abc123eeee').group())
# [12]
print(obj.findall('abc123eeee'))





