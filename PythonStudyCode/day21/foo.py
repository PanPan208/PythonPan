# @time: 2021/12/27 5:36 PM
# Author: pan
# @File: foo.py
# @Software: PyCharm


x = 1000

def get():
    print(f"x is {x}")
    return x


def change_x():
    global x
    x = 666
