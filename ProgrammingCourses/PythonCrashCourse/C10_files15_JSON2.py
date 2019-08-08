# 保存用户产生的数据 User generated data

import json

import time # 导入时间模块,记录登录时间
log_in_time = time.strftime("%Y%m%d_%H:%M:%S")

username = input("What's your name:")
filename = "username.json"
with open(filename, "w") as f_obj:
    json.dump(log_in_time, f_obj)
    json.dump(username, f_obj)
    print("We will remember you when you come back, " + username + "!")

# 注意,json.dump对字符串处理会自动加上双引号.不要试图避免.
# 写入json的内容,如果不加引号,以后是不好再被其他引用的.


# Greet user
import json

filename = "username.json"
with open(filename, "r") as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")