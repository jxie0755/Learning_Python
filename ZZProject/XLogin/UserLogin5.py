# X-log系统 - 非函数化
# 包括两部分,新用户和已有用户,附带密码验证
# 密码表设计成两个独立文件,单独存放用户名和密码,在运行时组合成为密码表
# 同时还要设计一个logout的程序,在新用户和已有用户登录时都会创造一个python程序.
# 一旦登录成功,记录登录时间,并且生成一个logout文件,将登录用户名和记录登出时间的程序自动写入.
# logout文件运行后将自动删除, 设置如果logout文件还在,就不能重复登录
# 注意: 运行logout后由于文件被删除,会导致login必须要保存一次才可以再次运行,不然会报错

import time

current_time = time.strftime("%Y%m%d_%H:%M:%S")
user_name = input("Please enter your name: ")
file_name = "data/" + "D_" + user_name.replace(" ", "") + ".txt"
logout_final_name = user_name.replace(" ", "") + "_logout" + ".py"

def write_log_out():
    with open(logout_final_name, "w") as f_obj:
        f_obj.write("import time")
        f_obj.write("\nfrom os import remove")
        f_obj.write("\nfrom sys import argv")
        f_obj.write("\ncurrent_time = time.strftime("%Y%m%d_%H:%M:%S")")
        f_obj.write("\nuser_name = " + "\"" + user_name + "\"")
        f_obj.write("\nfile_name = "data/D_" + user_name.replace(" ", "") + ".txt"")
        f_obj.write("\nwith" + " open(file_name, "a") as f_obj:")
        f_obj.write("\n" + "    f_obj.write("\\n" + "logged out: " + current_time)")
        f_obj.write("\nprint(user_name, "successfully logged out!")")
        f_obj.write("\nremove(argv[0])")

try:
    with open(logout_final_name, "r") as f_obj:
        f_obj.readlines()
    print("You have already logged in")

except FileNotFoundError:
    # 先读取文件, 如果用户存在就欢迎
    try:
        with open(file_name, "r") as f_obj:
            log_info = f_obj.readlines()
        print("Welcome back, " + user_name + "!")
        while True:
            pass_word = input("Please enter your password:")
            user_list = []
            sn_list = []
            with open("data/USER.txt", "r") as f_obj:
                listK = f_obj.readlines()
            with open("data/SN.txt", "r") as f_obj:
                listV = f_obj.readlines()
            # 读取内容剥离转义符号, 写入两个list
            for k in listK:
                user_list.append(k.rstrip())
            for v in listV:
                sn_list.append(v.rstrip())
            # 合并两个list到一个dict中
            pass_book = dict(zip(user_list, sn_list))
            if pass_word != pass_book[user_name]:
                print("wrong password")
                continue
            else:
                print("log in successfully!")
                break
        # 欢迎用户后,继续记录本次登录时间
        with open(file_name, "a") as f_obj:
            f_obj.write("\n" + "logged in:  " + current_time)

        # 新建一个python程序,为本次登录创造一个logout.
        write_log_out()

    # 若不存在,则为新用户创建一个新用户文件,并记录登录时间
    except FileNotFoundError:
        print("Your username are not found in the system.")
        print("If you like, you can register with this username.")

        new_password = input("Please setup your password:")
        file_name = "data/" + "D_" + user_name.replace(" ", "") + ".txt"
        with open("data/USER.txt", "a") as f_obj:
            f_obj.write(str(user_name) + "\n")
        with open("data/SN.txt", "a") as f_obj:
            f_obj.write(str(new_password) + "\n")
        with open(file_name, "w") as f_obj:
            f_obj.write(str(user_name))
            f_obj.write("\n" + "logged in:  " + current_time)
        print("Hello," + str(user_name) + "!")

        # 不要忘记logout
        write_log_out()
        
