# @time: 2022/1/14 5:45 PM
# Author: pan
# @File: re正则模块.py
# @Software: PyCharm
"""
正则表达式：
正则就是用一些具有特殊意义的符号组合在一起来描述字符或字符串的方法，
或 正则就是用来描述一类事务的规则。
"""

import re

"""
大写的都是小写的非

\w 匹配字母数字以及下划线
\W 非
\s 匹配任何空白字符 等价于 [\t\n\r\f] 
\S 
\d 匹配任何数字 等价于 [0-9]
\D 匹配任何非数字

\A 匹配字符串开头
^ 匹配字符串开头 一般使用这个

\Z 匹配字符串结尾  如果存在换行只匹配到换行前结束的字符串
\z 匹配字符串结尾
$ 匹配字符串的末尾 一般使用这个

\G 匹配最后匹配完成的位置
\n 匹配一个换行符
\t 匹配一个制表符

. 匹配任意字符，除了换行符  当re.DOTALL被标记指定的时候可以匹配任何字符

[...] 用于匹配一组列出来的字符 例如 [abc] 匹配 'a', 'b' 或 'c'
[^...] 用于匹配不在[] 的字符

贪婪模式
* 用于匹配*前面的字符0个或多个表达式
+ 用于匹配1个或多个表达式
？ 用于匹配0个或1个
{n} 精准匹配n个前面的表达式
{n, m} 匹配n到m个前面的表达式  贪婪

a|b 匹配|左右两侧的数据  也就是a或者b
() 匹配括号中的表达式 也就是一个组
"""

# w
print(re.findall('\w', 'Hello Pan 12123'))
print(re.findall('\W', 'Hello Pan 12123'))

# \A ^
print(re.findall('\AHe', 'Hello Pan 12123'))
# \Z \z $
print(re.findall('123\Z', 'Hello Pan 12123'))

# .
print(re.findall('a.b', 'axb aXb a1b, a b, aaab, a\nb'))
# 使用re.S或re.DOTALL 可以匹配任何字符
print(re.findall('a.b', 'axb aXb a1b, a b, aaab, a\nb', re.DOTALL))


# * 用于匹配*前面的字符0个或多个表达式  贪婪模式
# a后面可以跟0个或多个b的都能被匹配
print(re.findall('ab*', 'a bb ab, abbbb, abb'))

# + 匹配前面的的字符1个或多个  贪婪模式
# a后面的b 会匹配1个或多个
print(re.findall('ab+', 'a bb ab, abbbb, abb'))

# ?
# a后面的b 只会匹配0个或1个
print(re.findall('ab?', 'a bb ab, abbbb, abb'))


# 匹配包括小数在内的所有字符
# 如果是10. 这样的字符需要手动进行再处理一下
print(re.findall('\d+\.?\d*', 'fads11fda1.12ddf.12fdf10.da2fdaf1'))


# []
# 匹配 1 * 或-
# - 如果不是连接符  放到前面或后面
# 不然会容易和数字或字符进行连接
print(re.findall('a[1*-]b', 'a1b a*b a-b'))
# ^ 取反
print(re.findall('a[^1*-]b', 'a1b a*b a-b a=b'))
# ab中间只能是数字
print(re.findall('a[0-9]b', 'a1b a*b a-b a=b'))
# ab中间只能是小写字符
print(re.findall('a[a-z]b', 'a1b a*b a-b a=b aeb'))
# ab中间只能是大写小写字符
print(re.findall('a[a-zA-Z]b', 'a1b a*b a-b a=b aeb aEb'))

# \\ 会自动转译
# a\\c 转译表示的 a\c
# 使用r也就是rawString也就是使用原字符串 不会进行转译
# r'a\\c' 等价于 'a\\\\c'
# print(re.findall('a\\c', 'a\c'))
print(re.findall(r'a\\c', 'a\\c'))
print(re.findall('a\\\\c', 'a\c'))


# () 分组
# 匹配a后面b可以跟1个b或多个b  贪婪
print(re.findall('ab+', 'ababbab123'))
# 匹配的是结尾是123的 ab
print(re.findall('(ab)+123', 'ababbabab123'))
# ?: 可以让结果为匹配的全部内容
# 也就是 返回的结果会加上后面的123
print(re.findall('(?:ab)+123', 'ababbab123'))

# .*? 可以匹配任何字符
# 返回的是括号中匹配的内容
print(re.findall('href="(.*?)"', '<a href="http://www.baidu.com">点击</a>'))
# 加上 ?: 会加上前面的 href="XXX"  其中XXX为()中匹配的内容
print(re.findall('href="(?:.*?)"', '<a href="http://www.baidu.com">点击</a>'))

# ｜ 匹配 y或者ies
# ?: 表示返回的结果 会加上 commpanXXX
print(re.findall('compan(?:y|ies)', 'Too many companies have gone bankrupt, and the next one is my company'))






