# @time: 2021/12/10 3:31 下午
# Author: pan
# @File: 作业.py
# @Software: PyCharm

# 1、编写文件修改功能，调用函数时，传入三个参数（修改的文件路径，要修改的内容，修改后的内容）既可完成文件的修改
# def func1(name, res_content, dis_content):
#     with open(r"{}".format(name), mode="rt") as f1:
#         res = f1.read()
#         data = res.replace(res_content, dis_content)
#     with open(r"{}".format(name), mode="wt") as f2:
#         f2.write(data)

# /Users/izzld/Desktop/PythonPan/PythonStudyCode/day13/作业.py
# import os
# def func2(name, content1, content2):
#     with open("{}".format(name), mode="rt") as f1, \
#         open("copy_test.txt", mode="wt") as f2:
#         for line in f1:
#             f2.write(line.replace(content1, content2))
#     os.remove(name)
#     os.rename("copy_test.txt", "11.txt")


# 2、编写tail工具
# tail -f access.log
import time
def tail_log():
    with open(r"access.log", mode="rb") as f:
        # f.seek(0, 2)
        print(f.read())
        while True:
            res = f.readline()
            if not len(res) == 0:
                print(">>>>", res.decode("utf-8"))
            else:
                time.sleep(0.5)


# tail_log()

# 3、编写登录功能

# 4、编写注册功能

# 5、编写用户认证功能