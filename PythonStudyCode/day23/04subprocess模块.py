# @time: 2022/1/14 4:31 PM
# Author: pan
# @File: 04subprocess模块.py
# @Software: PyCharm
"""
执行系统命令
os.system('dir .')
使用os的命令

第二种使用subprocss
"""
# import os
# os.system('dir .')


import subprocess

# 可以执行多个命令
# 多个命令之间使用 分号进行分割
# stdout相当于将执行命令 正确的结果放入到一个PIPE管道中
# stderr相当于将执行命令 错误的结果放入到一个PIPE管道中
obj = subprocess.Popen('echo 哈哈哈; ls /; ls /root',
                 shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)

# print(obj)

# 执行命令正确返回的内容
# 将执行的结果进行解码 防止出现乱码
res = obj.stdout.read()
# print(res)
print(res.decode("utf-8"))

# 执行命令错误返回的内容
err_res = obj.stderr.read()
# print(err_res)
print(err_res.decode("utf-8"))














