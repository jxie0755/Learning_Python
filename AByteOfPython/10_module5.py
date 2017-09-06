# 使用以下命令可以import奇怪的module名字！！

mymodule = __import__("10_module4")

mymodule.say_hi()
print('Version', mymodule.__version__)

print(dir(mymodule))

# 一个普通python模块之中包含了不少__XX__的抬头文件，包括有：
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__']
