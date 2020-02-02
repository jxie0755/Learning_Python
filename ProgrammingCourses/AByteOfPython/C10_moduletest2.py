mymodule2 = __import__("09_function1b")

x=10
mymodule2.say_hello(x)
mymodule2.print_max(10, 20)

a = 100
b = 200
mymodule2.print_max(a, b)

# 注意引用模块时, 模块本身不能有实际输出内容, 不然会全部输出. 模块最后只带函数, 然后引用就引用函数计算. 
