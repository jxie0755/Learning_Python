# 学习如何使用python基本的I/O函数, 操作文件

import os
import sys
import shutil

# 使用os模块

# 相对路径就是从这个py文件所在的文件夹出发
# 我们常用’/‘来表示路径


# mkdir
try:
    os.mkdir("gopro")
except FileExistsError:
    pass

# 当前路径(其实路径是脚本所在的路径)
current_dir = os.getcwd()  # 留着备份
print(current_dir)  # >>> D:\Documents\GitHub\Learning_Python\ZStandardLibrary
print(type(current_dir))  # >>> 就是string

# chdir 可以用chdir()方法来改变当前的目录
os.chdir("gopro/") # 进入gopro文件夹
os.chdir("C:/Users/jxie0/Downloads/Baiduyun")

# getcwd()方法显示当前的工作目录
print(os.getcwd())
# >>> D:\Documents\GitHub\Learning_Python\ZStandardLibrary\gopro


# listdir 显示当前目录下的内容
for i in os.listdir(os.getcwd()):
    print(i)

# 重返当前脚本所在的绝对路径
# print(os.path.abspath(sys.argv[0]))
# os.chdir(str(os.path.abspath(sys.argv[0])))
# print(os.getcwd())

os.chdir(current_dir)
print(os.getcwd())


# 进入temp子文件夹, 并删除
os.chdir("temp")
print(os.listdir(os.getcwd()))

# os.chdir(current_dir + "/toberemove")
os.chdir(current_dir)

# 在上一层目录删除一个路径/文件
# os.rmdir("toberemove/")
print(os.getcwd())
# os.rmdir("temp")  # 如果路径不为空, 则不让删除
# 可以使用shutil库，该库为python内置库，是一个对文件及文件夹高级操作的库，可以与os库互补完成一些操作，如文件夹的整体复制，移动文件夹，对文件重命名等


# 为gopro路径创建100个txt文件
# os.chdir("gopro")
# print(os.getcwd())
# for i in range(1, 1001):
#     with open(f"{i}".rjust(4, "0") + ".txt", "a"):
#         pass


# for f in os.listdir(os.getcwd()):
# destination如果是路径就不改名字, 如果是文件名就复制并重命名
print("!!!!!!")
print(os.getcwd())
sourcedir = os.getcwd() + "/gopro/"
destdir = os.getcwd() + "/output"
print(destdir)
target = 30 # seconds
totalFram = 5 * 24
fileNum = len(os.listdir(sourcedir))
pickRate = fileNum // totalFram
print(pickRate)
count = 0
for f in os.listdir(sourcedir):
    if count % pickRate == 0:
        shutil.copy2(sourcedir + f, destdir)
    count += 1
