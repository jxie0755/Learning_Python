# http://www.cnblogs.com/Jerry-Chou/archive/2012/05/23/python-decorator-explain.html


# 问题起源
def login():
    print('in login')

def printdebug(func):
    print('enter the login')
    func()
    print('exit the login')

printdebug(login)
# >>>
# enter the login
# in login
# exit the login
# 这个方法讨厌的是每次调用login时，都通过printdebug来调用，但毕竟这是可行的


# 既然函数可以作为返回值，可以赋值给变量，我们可以让代码优美一点
def login():
    print('in login')

def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator  # function as return value
debug_login = printdebug(login)  #function assign to variable

debug_login()  # 这样call这个debug的函数就显得更直观了
# >>>
# enter the login
# in login
# exit the login
# 将原先的两个函数printdebug和login绑定到一起，成为debug_login,这种耦合叫内聚


# Python的解决方案是提供一个语法糖(Syntax Sugar)，用一个@符号来结合它们
def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator

@printdebug  # combine the printdebug and login
def login():
    print('in login')

login()  # make the calling point more intuitive
# >>>
# enter the login
# in login
# exit the login


# 传入参数
def printdebug(func):
    def __decorator(arg):    #add parameter receive the user information
        print('enter the login')
        func(arg)  # pass arg to login
        print('exit the login')
    return __decorator

@printdebug
def login(user):
    print('in login: ' + user)

login('Denis')
# >>>
# enter the login
# in login: Denis
# exit the login


# 装饰器本身有参数
def printdebug(level):  # add wrapper to recevie decorator's parameter
    def printdebug(func):
        def __decorator(arg):
            print('enter the login, level: ', level)
            func(arg)
            print('exit the login')
        return __decorator
    return printdebug    #return original decorator

@printdebug(level=5)   #decorator's parameter, debug level set to 5
def login(user):
    print('in login: ' + user)

login('Denis')
# >>>
# enter the login, level:  5
# in login: Denis
# exit the login


# 装饰有返回值的函数
def printdebug(func):
    def __decorator(user):
        print('enter the login')
        result = func(user)  # recevie the native function call result
        print('exit the login')
        return result        # return to caller
    return __decorator

@printdebug
def login(user):
    print('in login:' + user)
    msg = 'success' if user == 'Denis' else 'fail'
    return msg  # login with a return value

result1 = login('Denis');
print(result1)
print()
result2 = login('Cindy');
print(result2)
# >>>
# enter the login
# in login:Denis
# exit the login
# success

# enter the login
# in login:Cindy
# exit the login
# fail


# 应用多个装饰器
def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator

def others(func):    # define a other decorator
    def __decorator():
        print('***other decorator***')
        func()
    return __decorator

@others         #apply two of decorator
@printdebug
def login():
    print('in login:')

@printdebug    #switch decorator order
@others
def logout():
    print('in logout:')

login()
print()
logout()
# >>>
# ***other decorator***
# enter the login
# in login:
# exit the login

# enter the login
# ***other decorator***
# in logout:
# exit the login


# 什么情况下装饰器不适用？装饰器不能对函数的一部分应用，只能作用于整个函数
# 一个变通的办法是“提取函数”，我们将函数中的一行语句提取成函数，然后对提取出来的函数应用装饰器
def printdebug(func):
    def __decorator(user):
        print('enter the login')
        result = func(user)
        print('exit the login')
        return result
    return __decorator

def login(user):
    print('in login:' + user)
    msg = validate(user)  # exact to a method
    return msg

@printdebug  #apply the decorator for exacted method
def validate(user):
    message = "success" if user == "Cindy" else "fail"
    return message

result1 = login('Denis');
print(result1)
# >>>
# in login:Denis
# enter the login
# exit the login
# fail


# 另外:
# 装饰器在OOP中的应用Module/Learn_OOP.py中有介绍