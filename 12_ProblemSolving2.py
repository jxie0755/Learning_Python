# 照常规引用os和time
import os
import time
source = ['~/Documents/Account', '~/Documents/Books/Stocks', '~/Documents/Mind\ Maps']

# 给target创见一个子文件夹
target_dir = '/Users/Jxie0755/Resources/Backup' + os.sep + str(time.strftime('%Y%m%d'))
# 改进了一下zip名称的创见
target = target_dir + os.sep + time.strftime('Time_%H_%M_%S') + '.zip'

# 后面的输出维持原装
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
    print('Backup successful')
else:
    print('Backup FAILED')

