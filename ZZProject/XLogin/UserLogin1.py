"""创立一个用户登录系统,按照用户名创立文件,并记录登录时间"""

import time
# 创立一个记录时间的变量
log_in_time = time.strftime("%Y%m%d_%H:%M:%S")

# 创造用户名,让用户自己输入
username = input("What's your name: ")
# 用户名文件取名-去掉空格
filename = "D_" + username.replace(" ", "") + ".txt"

# 先读取文件, 如果用户存在就欢迎
try:
    with open(filename, "r") as f_obj:
        loginfo = f_obj.readlines()
    print("Welcome back, " + username + "!")

# 若不存在,则为新用户创建一个新用户文件,并记录登录时间
except FileNotFoundError:
    with open(filename, "w") as f_obj:
        f_obj.write(username)
        f_obj.write("\n" + log_in_time)
    print("Hello," + username + "!")

# 欢迎用户后,继续记录本次登录时间
else:
    with open(filename, "a") as f_obj:
        f_obj.write("\n" + log_in_time)
