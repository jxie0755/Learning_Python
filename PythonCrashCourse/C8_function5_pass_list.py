# Passing list to function
# list as arguments

def greet_users(names):    # 提前假定参数是一个list了,随后:
    for name in names:     # 用遍历的方式,来处理这个变量,就是说明这个参数为list
        msg = "Hello," + name.title() + "!"
        # 此处记得要用加号,定义的是字符串,不要用逗号
        print(msg)

usernames = ["denis", "cindy", "adrienne"]
greet_users(usernames)     # 如果参数不是一个list,函数中的for in loop无法运行.
