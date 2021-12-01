"""
作业
"""

# # 9*9 乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{}*{}={}".format(j, i, i*j).ljust(6, " "), end=" ")
#     print()

# 打印金字塔
"""  
max_level = 5
        *             第一行  4个空格 1个* 
      * * *           第二行  3个空格 3个* 
    * * * * *         第三行  2个空格 5个*
  * * * * * * *       第四行  1个空格 7个*
* * * * * * * * *     第五行  0个空格 9个*
"""
# max_level = 10
# for i in range(max_level):
#     print(" "*(max_level - i - 1), "*"*(2 * i + 1))


# 字符串
name = " aleX"
name = name.strip()
print(name.strip())
print(name)
print(name.startswith("al"))
print(name.endswith("X"))
print(name.replace("l", "p"))
print(name.split("l"))
print(name.lower())
print(name.upper())
print(name.swapcase())
print(name[1])
print(name[0:3])
print(name[-3:-1])
print(name.find("e"))
print(name[0:len(name) - 1])
