import time

log_in_time = time.strftime('%Y%m%d_%H:%M:%S')
user_name = input("What's your name: ")
file_name = 'data/D_' + user_name.replace(' ', '') + '.txt'

# 先读取文件, 如果用户存在就欢迎
try:
    with open(file_name, 'r') as f_obj:
        log_info = f_obj.readlines()
    print("Welcome back, " + user_name + "!")

    while True:
        pass_word = input('Please enter your password:')
        user_list = []
        sn_list = []
        with open('data/USER.txt', 'r') as f_obj:
            listK = f_obj.readlines()
        with open('data/SN.txt', 'r') as f_obj:
            listV = f_obj.readlines()

        # 读取内容剥离转义符号, 写入两个list
        for k in listK:
            user_list.append(k.rstrip())
        for v in listV:
            sn_list.append(v.rstrip())

        # 合并两个list到一个dict中
        if len(user_list) == len(sn_list):  # 加一个检查项
            # 注意zip函数用法
            pass_book = dict(zip(user_list, sn_list))

        if pass_word != pass_book[user_name]:
            print('wrong password')
            continue
        else:
            print('log in successfully!')
            break

    # 欢迎用户后,继续记录本次登录时间
    with open(file_name, 'a') as f_obj:
        f_obj.write('\n' + 'logged in: ' + log_in_time)

# 若不存在,则为新用户创建一个新用户文件,并记录登录时间
except FileNotFoundError:
    user_list = []
    sn_list = []
    with open('data/USER.txt', 'r') as f_obj:
        listK = f_obj.readlines()
    with open('data/SN.txt', 'r') as f_obj:
        listV = f_obj.readlines()

    # 读取内容剥离转义符号, 写入两个list
    for k in listK:
        user_list.append(k.rstrip())
    for v in listV:
        sn_list.append(v.rstrip())

    # 合并两个list到一个dict中
    pass_book = dict(zip(user_list, sn_list))

    print('You need to setup your new ID')
    while True:
        user_name = input('Please input your new user ID: ')
        if user_name in user_list:
            print('this username has been taken, please input a new one')
            continue
        else:
            break
    new_password = input('Please setup your password:')

    with open('data/USER.txt', 'a') as f_obj:
        f_obj.write(str(user_name) + '\n')
    with open('data/SN.txt', 'a') as f_obj:
        f_obj.write(str(new_password) + '\n')

    with open(file_name, 'w') as f_obj:
        f_obj.write(str(user_name))
        f_obj.write('\n' + 'logged in: ' + log_in_time)
    print("Hello," + str(user_name) + '!')
