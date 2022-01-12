# @time: 2022/1/10 6:11 PM
# Author: pan
# @File: src.py
# @Software: PyCharm


# 核心代码

from lib.common import logger

def login():
    print("登录功能")
    logger("用户进行了登录")

def register():
    print("注册功能")
    logger("用户进行了注册")

def withdraw():
    print("提现功能")
    logger("用户进行了提现")

def transfer():
    print("转账功能")
    logger("用户进行了转账")

func_dic = {
    '0': ['退出', exit],
    '1': ['登录', login],
    '2': ['注册', register],
    '3': ['提现', withdraw],
    '4': ['转账', transfer]
}


def run():
    print("程序开始")
    while True:
        for k in func_dic:
            print(k, func_dic[k][0])

        cmd = input('请输入指令:').strip()
        if cmd in func_dic:
            func_dic[cmd][1]()
        else:
            print("请重新输入指令!")


if __name__ == '__main__':
    run()

