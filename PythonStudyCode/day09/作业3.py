# 一.关系运算
# 　 有如下两个集合，
#    pythons是报名python课程的学员名字集合，
#    linuxs是报名linux课程的学员名字集合
# 　　pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# 　　linuxs={'wupeiqi','oldboy','gangdan'}
# 　　1. 求出即报名python又报名linux课程的学员名字集合
# 　　2. 求出所有报名的学生名字集合
# 　　3. 求出只报名python课程的学员名字
# 　　4. 求出没有同时这两门课程的学员名字集合 　　
pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
linuxs={'wupeiqi','oldboy','gangdan'}
# 1
# print(pythons & linuxs)
# print(pythons.intersection(linuxs))
# 2
# print(pythons | linuxs)
# print(pythons.union(linuxs))
# 3
# print(pythons - linuxs)
# print(pythons.difference(linuxs))
# 4
# print(pythons ^ linuxs)
# print(pythons.symmetric_difference(linuxs))


# 二 去重
# 1. 有列表l = ['a', 'b', 1, 'a', 'a'], 列表元素均为可hash类型，去重，
# 得到新列表, 且新列表无需保持列表原来的顺序
# l = ['a', 'b', 1, 'a', 'a']
# 方法一
# l = list(set(l))
# print(l)

# 方法二
# new_l = []
# for item in l:
#     if item not in new_l:
#         new_l.append(item)
# print(new_l)


# 2.在上题的基础上，保存列表原来的顺序
# new_l = []
# for item in l:
#     if item not in new_l:
#         new_l.append(item)
# print(new_l)


# 3.去除文件中重复的行，要保持文件内容的顺序不变


#  4.有如下列表，列表元素为不可hash类型，
#  去重，得到新列表，且新列表一定要保持列表原来的顺序
l = [
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]
new_l = []
for item in l:
    if item not in new_l:
        new_l.append(item)
print(new_l)
