# 学习如何使用python基本的I/O函数, 操作文件

import os
import sys
import shutil

# 使用os模块

# 系统信息查询

print(os.name) # >>>  nt
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统

# 要获取详细的系统信息，可以调用uname()函数
# print(os.uname())
# uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的

# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
# print(os.environ)



# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下


print("\n文件/路径 操作")
# 相对路径就是从这个py文件所在的文件夹出发
# 我们常用’/‘来表示路径


# 查看当前目录的绝对路径.初始时是脚本所在的路径:
print(os.path.abspath("."))
# 等同于
print(os.getcwd())


# 直接创造新路径
# mkdir
try:
    os.mkdir("gopro")
except FileExistsError:
    pass


# 合成两个路径
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
new_directory = os.path.join("./temp/New folder", "WTF")
try:
    os.mkdir(new_directory)  # 然后根据这个新路径创造出来
except FileExistsError:
    pass


# 分拆一个路径
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
print(os.path.split("/Users/dxie/testdir/file.txt"))
# >>> ("/Users/dxie/testdir", "file.txt")  输出为一个tuple
# 通过这个可以得到上一层路径和文件名, 非常方便
print(os.path.split("/Users/dxie/testdir/"))
# >>> ("/Users/dxie/testdir", "")   对于纯路径, 也可以获得上一层路径
# splitext分拆路径得到文件扩展名
print(os.path.splitext("/Users/dxie/testdir/file.pdf"))  # 可以直接让你得到文件扩展名，很多时候非常方便
# >>> ("/Users/dxie/testdir/file", ".pdf")


# Rename and move
try:
    os.rename("./temp/1.txt", "23333.txt")   # 可以换路径, 这样就是相当于移动了
except FileExistsError:
    pass
except FileNotFoundError:
    pass

current_dir = os.getcwd()  # 留着备份
print(current_dir)  # >>> D:\Documents\GitHub\Learning_Python\ZStandardLibrary
print(type(current_dir))  # >>> 就是string



# isdir 判断是路径会否真实存在
print(os.path.isdir("C:/Users/jxie0/Downloads/Baiduyun"))  # >>> True
print(os.path.isdir("C:/Users/jxie0/Downloads/Baiun"))     # >>> Flase
print(os.path.isdir("./temp/2.txt"))  # >>> False   文件即使存在也是False
# isfile 判断文件是否真实存在
print(os.path.isfile("./temp/2.txt"))
print(os.path.isfile("./temp/6.txt"))


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
