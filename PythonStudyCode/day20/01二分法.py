# @time: 2021/12/27 3:26 PM
# Author: pan
# @File: 01二分法.py
# @Software: PyCharm

"""
算法：一种高效的解决问题的办法
常用的算法有：冒泡排序、二分法查找数据等等

需求：有一个按照从小到大进行排序的列表 如何快速的从中查找到对应的数据
"""

# nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
# find_num = 10
# print(nums)

# 方案1
# 循环遍历列表 一个一个的查找
# 效率低 如果是一个很大的列表 恰好需要查找的数据又在最后面
# 需要循环遍历很多次才可以查找到数据
# for num in nums:
#     print(f"num = {num}")
#     if find_num == num:
#         print("find it")
#         break


# nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
nums = [-3, 4, 13, 10, -2, 7, 89]
nums.sort()
# 对于不是从小到大排列的数据 需要先进行排序再进行查找
find_num = 10
print(nums)
# 方案2
# 使用二分法进行查找数据
def binary_search(l, find_num):
    print(l)
    if len(l) == 0:
        print("列表中没有该数据")
        return

    # 使用整除获取到中间数据的index
    mid_index = len(l) // 2
    if find_num > l[mid_index]:
        # 需要查找的数据在右侧
        binary_search(l[mid_index+1:], find_num)
    elif find_num < l[mid_index]:
        # 需要查找的数据在左侧
        binary_search(l[:mid_index], find_num)
    else:
        # 查找到了对应的数据
        print("find it")

# binary_search(nums, 10)
# binary_search(nums, 89)
binary_search(nums, 1000)