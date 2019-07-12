# ProblemSolving 2:
# 一款程序来备份我所有的重要文件
# 改进目标:为备份创立一个日期的子文件夹,便于管理

# 照常规引用os和time
import os
import time
source = ["~/Documents/Account", "~/Documents/Books/Stocks", "~/Documents/Mind\ Maps"]
target_dir = "/Users/Jxie0755/Resources/Backup"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 增加一个创立子文件夹的路径
today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("Time_%H_%M_%S")

# 额外增加一个强制新建子文件夹的命令
if not os.path.exists(today):
    os.mkdir(today)

target = today + os.sep + now + ".zip"

# 5. 使用zip命令打包文件
zip_command = "zip -r {0} {1}".format(target, " ".join(source))

# 运行备份
print("Zip command is:")
print(zip_command)
print("running:")
if os.system(zip_command) == 0:
    print("Sucessful backup to", target)
else:
    print("Backup FAILED")
