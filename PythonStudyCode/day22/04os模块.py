# @time: 2022/1/12 5:53 PM
# Author: pan
# @File: 04os模块.py
# @Software: PyCharm
"""
os 系统模块
"""
import os


# 获取正在使用的平台的名称
# windows是 nt
# Max/Unix是 posix
# print(os.name)

# 操作系统的路径分隔符 默认是 /
# os.sep = "*"
# print(os.sep)

# 获取当前的工作目录
# 也就是当前脚本工作的目录
# print(os.getcwd())

# 设置和获取环境变量
# os.environ["aaaaaaaaa"] = "1"
# print(os.environ)


# # listdir 列出指定文件夹下的所有文件
# res = os.listdir(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22')
# print(res)
# # 如果指定路径为一个点 代表当前路径文件下的所有文件
# res = os.listdir('.')
# print(res)
# 返回当前路径  '.'
# print(os.curdir)


# # stat 获取文件的属性
# print(os.stat(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))
# # chmod  修改文件的属性
# print(os.chmod(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))

# remove
# 移除一个文件（不能是文件夹）
# os.remove(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/aa/aa.py')

# 创建一个不存在的目录  如果已经存在会报错
# os.mkdir('aa/a.py')
# 删除一个目录 如果目录不存在会报错
# os.rmdir('aa/a.py')
# 删除多个目录
# os.removedirs(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/aa')


# 运行shell脚本命令
# 和在终端运行是一样的
# os.system('ls .')


# path 相关
print("os path".center(100, "="))

# 判断是否是一个文件夹
print(os.path.isdir(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))
# 判断是否是一个文件
print(os.path.isfile(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))
# 判断文件是否存在
print(os.path.exists(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))


# 将一个文件路径进行分割 文件名和文件路径进行分割
# 前面是路径 后面是文件名
print(os.path.split(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))
# 如果只是有路径也会进行分割
# 将最后一个斜杠后的内容 作为名字进行分割
print(os.path.split(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22'))
# 将文件的路径和扩展名进行分割
# 签名是文件路径 后面是扩展名
print(os.path.splitext(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))
# 返回路径下 文件的名字
print(os.path.basename(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))
# 返回路径下 文件的路径
print(os.path.dirname(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))
# 连接目录路径和文件名和路径
print(os.path.join(r'/a/b/c', 'tt.py'))


# 返回文件的大小 size
# 3026kb
print(os.path.getsize(r'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day22/01time模块.py'))

# 返回文件的绝对路径
print(os.path.abspath(r'01time模块.py'))
# 判断是否是绝对路径
print(os.path.isabs(r'01time模块.py'))
# 规范一个文件路径字符串格式
print(os.path.normpath(r'01time模块.py'))


# 路径的使用
print("path的使用".center(100, "="))

# 1 获取项目路径 （推荐使用）
BASE_PATH = os.path.dirname(os.path.dirname(
    __file__
))
print(BASE_PATH)

# 2 使用normpath进行获取项目根路径
# .. 返回上一个路径
PATH = os.path.normpath(os.path.join(
    __file__,
    '..',
    '..'
))
print(PATH)


# 3 在python3.5之后 提供一个一个库可以进行获取
# 不兼容python2.x
from pathlib import Path
# 当前文件路径的父路径的父路径
res = Path(__file__).parent.parent
print(res)


