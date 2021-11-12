
print("Hello World 1111")

if 10 > 2:
    print("啊哈哈")
else:
    print("aaaaa")


# a = int(input("请输入一个数字:"))
a = 10
if a > 10:
    var = {
        print("a > 10")
    }
elif a == 10:
    print("a = 10")
else:
    # print("a < 10")
    pass


# namelist = ['Sophia','Emma','Olivia','Ava','Mia','Isabella','Zoe','Lily','Emily','Madison','Jackson','Aiden','Liam','Lucas','Noah','Mason','Ethan','Caden','Logan','Jacob']
# for i in namelist:
#     print(i)


'''
多行注释
Hello World
这是第一个Python程序
Life is short, you need python!

集成开发环境：
IDE integrated development environment
'''


# range是从0开始到x-1的整数序列
# range(5) 是 0-4
for i in range(5):
    # print(i)
    pass


# 取某个区间的数序列
# [a, b) 包括头 不包括尾
for a in range(1,6):
    # print(a)
    pass

# 例子
# for index in range(1, 11):
#     print("书桓走的第{}天, miss her".format(index))


# while循环 只要满足while后面的条件 就一直进行下去
# n = 1
# while n < 10:
#     print("n = {}".format(n))
#     n += 1


# break 跳出整个循环
# continue 跳出当前循环 继续下一次的循环
# for i in range(10):
#     if i == 5:
#         # break
#         continue
#     print(i)



#  逢7过函数
# 当数字可以被7整除 并且数字中包含7 不打印
def jump7():
    for i in range(101):
        # if i % 7 == 0:
        #     continue
        # if str(i).__contains__('7'):
        #     continue
        # print(i)

        # i%7==0 可以被7整除
        # i%10==7 个位上是7
        # i//10==7 十位上是7
        if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
            continue
        print(i)
jump7()


