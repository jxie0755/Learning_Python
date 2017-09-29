# 创立一个用户登录系统,按照用户名创立文件,并记录登录时间
# JSON版, 输出记录在json文件中

import json
import time

log_in_time = time.strftime('%Y%m%d_%H:%M:%S')
username = input("What's your name: ")
filename = 'D_' + username.replace(' ', '') + '.json' # 改为.json格式

try:
    with open(filename, 'r') as f_obj:
        loginfo = f_obj.readlines()
    print("Welcome back, " + username + "!")

except FileNotFoundError:
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)     # 用json.dump输入数据
        f_obj.write('\n')              # 强行用write换行符来换行
        json.dump(log_in_time, f_obj)
    print("Hello," + username + '!')

else:
    with open(filename, 'a') as f_obj:
        f_obj.write('\n')
        json.dump(log_in_time, f_obj)