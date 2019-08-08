"""
创立一个用户登录系统,按照用户名创立文件,并记录登录时间
改进部分: 增加一个密码的输入和核对程序
密码本改进!!!! 独立用户名和密码本 方法见: password book idea
保存为M_Xlogin.py

创建login 函数化
"""


import time

import M_passbook


def Xlogin():

    log_in_time = time.strftime("%Y%m%d_%H:%M:%S")
    user_name = input("What's your name: ")
    file_name = "data/D_" + user_name.replace(" ", "") + ".txt"

    # 先读取文件, 如果用户存在就欢迎
    try:
        with open(file_name, "r") as f_obj:
            log_info = f_obj.readlines()
        print("Welcome back, " + user_name + "!")

        while True:
            pass_word = input("Please enter your password:")
            M_passbook.read_passbook()
            if pass_word != M_passbook.pass_book[user_name]:
                print("wrong password")
                continue
            else:
                print("log in successfully!")
                break

        # 欢迎用户后,继续记录本次登录时间
        with open(file_name, "a") as f_obj:
            f_obj.write("\n" + "log in: " + log_in_time)

    # 若不存在,则为新用户创建一个新用户文件,并记录登录时间
    except FileNotFoundError:
        M_passbook.read_passbook()
        print("You need to setup your new ID")
        while True:
            new_user_name = input("Please input your new user ID: ")
            if new_user_name in user_list:
                print("this username has been taken, please input a new one")
                continue
            else:
                break

        new_password = input("Please setup your password:")

        with open(file_name, "w") as f_obj:
            f_obj.write(new_user_name)
            f_obj.write("\n" + log_in_time)
        print("Hello," + new_user_name + "!")

        M_passbook.update_passbook()

# 创建logout 函数化

def Xlogout():
    with open(M_passbook.file_name, "a") as f_obj:
        f_obj.write("\n" + "log out: " + M_passbook.log_in_time)
