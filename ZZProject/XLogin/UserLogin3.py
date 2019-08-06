"""
创立一个用户登录系统,按照用户名创立文件,并记录登录时间
改进部分: 增加一个密码的输入和核对程序
密码表还不完善, 需要独立分割开来,并能update新用户名和密码
"""

import time

# 创立一个记录时间的变量
log_in_time = time.strftime("%Y%m%d_%H:%M:%S")
# 创造用户名,让用户自己输入
username = input("What's your name: ")
# 用户名文件取名-去掉空格
filename = "D_" + username.replace(" ", "") + ".txt"
UserPassList = {"Denis Xie": "123", "Cindy Tian": "456"}
# 先读取文件, 如果用户存在就欢迎
try:
    with open(filename, "r") as f_obj:
        loginfo = f_obj.readlines()
    print("Welcome back, " + username + "!")
    while True:
        SN = input("Please enter your password:")
        if SN != UserPassList[username]:
            print("wrong password")
            continue
        else:
            print("log in successfully!")
            break
    # 欢迎用户后,继续记录本次登录时间
    with open(filename, "a") as f_obj:
        f_obj.write("\n" + log_in_time)

# 若不存在,则为新用户创建一个新用户文件,并记录登录时间
except FileNotFoundError:
    SN = input("Please setup your password:")
    UserPassList[username] = SN
    with open(filename, "w") as f_obj:
        f_obj.write(username)
        f_obj.write("\n" + log_in_time)
    print("Hello," + username + "!")
