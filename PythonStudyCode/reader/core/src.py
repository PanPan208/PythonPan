# @time: 2022/1/11 4:54 PM
# Author: pan
# @File: src.py
# @Software: PyCharm

# import sys
# print(sys.path)

# 直接使用import导入会出现bug
# import login

# from core import login
from core.login import register

# def register():
#     print("账号注册...")

def rechange():
    print("充值功能")

def read():
    print("阅读功能")

func_dic = {
    '0': ['退出程序', exit],
    '1': ['账号注册', register],
    "2": ["阅读小说", read]
}

def run():
    while True:
        for k in func_dic:
            print(f'{k} {func_dic[k][0]}')

        cmd = input("请输入程序指令:").strip()
        if cmd in func_dic:
            func_dic[cmd][1]()
        else:
            print("请重新输入!!!")

if __name__ == '__main__':
    run()