# 一款程序来备份我所有的重要文件
import os
import time

# 1. 指定列表
source = ['~/Documents/Account', '~/Documents/Books/Stocks', '~/Documents/Mind\ Maps']
# 路径名字含有空格按照mac terminal标准处理
# 若路径中有空格,请使用双引号,这里不必全称目录,可以使用"~/"

# 2. 指定备份存放目录
target_dir = '/Users/Jxie0755/Resources/Backup'
# 这里必须要用全称目录!

# 如果目标目录不存在,则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 3. 指定文件打包
# 4. 同时设定zip包名称由日期和时间组成
target = target_dir + os.sep + time.strftime('%Y%m%d_%a_%X') + '.zip'

# 5. 使用zip命令打包文件
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
    print('Sucessful backup to', target)
else:
    print('Backup FAILED')
