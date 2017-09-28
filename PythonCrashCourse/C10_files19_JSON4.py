# User login
# 这一版本是如果找不到文件名就让输入用户名
# 如果找到文件,就直接welcome,缺少一个查询的步骤
# 再次重构: 函数greet_user()逻辑: 先找已有的用户名,如果有就welcome,如果没有就得到新用户名,然后告知已经记住,下次welcome.

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

def get_new_username():
    # 拆分成一个专门用于得到新用户名的函数
    username = input("What's your name:")
    filename = filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户,并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + "!")


greet_user()
# 用函数式拆分成小的代码块,一是方便引用,而是理清逻辑