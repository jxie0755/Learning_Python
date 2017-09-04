# 仍然是导入相同的基础设定

import os
import time
source = ['~/Documents/Account', '~/Documents/Books/Stocks', '~/Documents/Mind\ Maps']
target_dir = '/Users/Jxie0755/Resources/Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('Time_%H_%M_%S')

if not os.path.exists(today):
    os.mkdir(today)

# 增加一个comment内容
comment = input('Enter a comment -->') # 提供输入口
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
    print('Backup successful')
else:
    print('Backup FAILED')
