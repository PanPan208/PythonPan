# @time: 2022/1/13 4:21 PM
# Author: pan
# @File: 06shutil模块.py
# @Software: PyCharm
"""
文件操作
高级操作功能
"""
import shutil

# 将一个文件copy内容到另一个文件
# 目标文件无需存在
# shutil.copyfileobj(open(r'aa/test1.txt', mode='r'), open(r'aa/test2.txt', mode='w'))


# 将一个文件进行copy
# 目标文件也无需存在
# shutil.copyfile(r'aa/test1.txt', r'aa/test3.txt')


# copy文件和权限
# shutil.copy(r'aa/test1.txt', r'aa/test4.txt')
# copy文件和状态信息
# shutil.copy2(r'aa/test1.txt', r'aa/test4.txt')

# 仅仅copy权限 其他不变
# 目标文件必须存在
# shutil.copymode()

# 仅仅copy状态信息
# shutil.copystat()


# 递归的去copy文件夹
# shutil.copytree()
# copy的时候可以忽略的文件
# shutil.ignore_patterns()


# 递归的去删除文件
# shutil.rmtree(r'aa')
# 递归的去移动文件
# shutil.move('test1', 'test2')


# 文件解压缩
# 将aa文件下的内容 打包成tar 放到当前文件夹下
# res = shutil.make_archive(r'temp', 'gztar', root_dir=r'aa')
# 打包压缩后放到temp文件夹下面
# res = shutil.make_archive(r'temp/a_a', 'gztar', root_dir=r'aa')


# zipfile  压缩是zip格式
import zipfile
# 压缩
# 压缩的时候 模式是w
z = zipfile.ZipFile('pan.zip', 'w')
z.write(r'aa/test1.txt')
z.write('01time模块.py')
z.close()

# 解压
# 解压的时候 使用的模式是r
z = zipfile.ZipFile('pan.zip', 'r')
z.extractall('panpan_zip_file')
z.close()


# 另一个压缩解压的库
# 压缩是 tar格式
import tarfile
# 压缩
# open 命名一个压缩后的名称
# add 将文件添加压缩包中 并重新取一个名字
# 可以多次进行添加 知道close
t = tarfile.open(r'pan_tar.tar', 'w')
t.add('aa/test1.txt', arcname='a.txt')
t.add('aa/test2.txt', arcname='test2.txt')
t.close()


# 解压
# 模式使用 r
# 解压到指定的文件夹下
t = tarfile.open(r'pan_tar.tar', 'r')
t.extractall('panpan_tar_file')
t.close()



