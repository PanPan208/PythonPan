# @time: 2022/1/10 4:54 PM
# Author: pan
# @File: 04函数的类型提示.py
# @Software: PyCharm

# def register(name: str, age: int, hobby: tuple) -> int:
#     print(name)
#     print(age)
#     print(hobby)
#     return 100
#
# register("pan", 20, ("music", "movie", "sport"))
# # 类型只会起到提示的作用
# # 至于你非要传入其他的类型 也是可以的
# register(100, [10, 20], True)


def register(name: "必须输入字符串", age: int, hobby: ('必须输入元组',)) -> '必须返回整形':
    print(name)
    print(age)
    print(hobby)
    return 100

register("pan", 20, ("music", "movie", "sport"))
register(100, [10, 20], True)

# 附注
# 返回函数的参数以及返回值的名称以及类型
print(register.__annotations__)

