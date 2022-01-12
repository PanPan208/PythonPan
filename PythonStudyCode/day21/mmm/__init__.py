# @time: 2022/1/10 5:16 PM
# Author: pan
# @File: __init__.py.py
# @Software: PyCharm

print("我是mmm包")

x = 100
y = 200

def say():
    print("我是mmm包中的say函数")


# 将mmm包文件夹加入到环境变量中
import sys
sys.path.append(f'/Users/izzld/Desktop/PythonPan/PythonStudyCode/day21/mmm')


# print(__name__)
# 1、当该文件被当成执行程序运行 name返回的是 __main__
# 2、当该文件被当成模块被导入的时候 name返回的 mmm
# 快捷键 main
if __name__ == '__main__':
    print("文件被执行")
    say()
else:
    print("文件被当成模块导入")
    pass



