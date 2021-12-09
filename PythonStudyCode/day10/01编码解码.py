# coding: UTF-8

x = "上"

# 将编码格式转换为 gbk
# unicode -> gbk
res = x.encode("gbk")
print(res, type(res))
# b'\xc9\xcf' <class 'bytes'>

# 解码 指定解码格式
print(res.decode('gbk'))
#  上
