# User login
# 这一版本是如果找不到文件名就让输入用户名
# 如果找到文件,就直接welcome,缺少一个查询的步骤

import json

filename = "username.json"
try:
    with open(filename, "r") as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name:")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
        print("We will remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")