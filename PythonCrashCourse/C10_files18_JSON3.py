# User login
# 这一版本是如果找不到文件名就让输入用户名
# 如果找到文件,就直接welcome,缺少一个查询的步骤
# 重构: 用函数greet_user()封装
# 再拆分成两个函数. 用greet_user()来运行get_stored_user()若不能得到username就新建用户名

import json


def get_stored_username():
    """如果储存了用户名,就获取它"""
    filename = 'username.json'
    try:
        with open(filename, 'r') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
        # 这个函数要么返回预期值,要么返回None


def greet_user():
    """问候用户,并指出其名字"""

    # 首先运行第一个函数得到username
    username = get_stored_username()

    # 如果得到了就欢迎
    if username:
        print("Welcome back, " + username + "!")

    # 如果不能得到就输入新用户名
    else:
        username = input("What's your name:")
        filename = filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We will remember you when you come back, " + username + "!")


greet_user()