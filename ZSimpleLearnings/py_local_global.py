# nonlocal的用法
# 嵌套函数对于其外层作用域中的变量是有访问权限的
def outside():
    msg = "Outside!"

    def inside():
        print(msg)  # msg可以搜寻外层变量

    inside()
    print(msg)

outside()
# >>>
# Outside!
# Outside!

def outside():
    msg = "Outside!"
    def inside():
        msg = "Inside!"  # 并非改变outside的变量,而是新建了一个同名的变量
        print(msg)
    inside()
    print(msg)

outside()
# >>>
# Inside!    # 来自inside
# Outside!   # 来自outside, 不是同一个frame,而且不受inside影响


def outside():
    msg = "Outside!"
    def inside():
        nonlocal msg      # 加入nonlocal的意思就是不要新建,而是从外层修改
        msg = "Inside!"
        print(msg)
    inside()
    print(msg)

outside()
# >>>
# Inside!
# Inside!

# 多层nonlocal
def f():
    x = 100
    def g():
        nonlocal x
        x = 50
        print(x)
        def h():
            nonlocal x
            x = x + 1
            return x
        return h

    return g

print(f()()())
# >>> 50  # from the first time
# >>> 51  # x changed again based on the last frame


# 在有字典时,没有必要nonlocal
def outside():
    d = {"outside": 1}
    def inside():
        d["inside"] = 2
    inside()
    print(d)

outside()
# >>>
# {'outside': 1, 'inside': 2}   # 没有使用nonlocal仍然从内部改变了外层变量
# 解释: 字典插入并不是赋值操作，而是方法调用（method call）。调用字典对象中的__setitem__方法

# 在许多Python程序中，很少用到非局部语句
# 但是，有了这种语句之后，我们就可以减少不同作用域之间变量名的冲突。非局部语句，也让我们更加容易地访问、操作外层作用域中的变量。



# global语句
# Python中能改变变量作用域的是关键字有def，class和lamda，其内部变量为封闭作用域
# if/elif/else，while/for，try/except/else/finally等不改变变量的作用域，其内变量与外部变量作用域一致

# global是一个声明语句，该声明在当前整个代码块中都有效
# 在同一代码块中，列在global语句中的所有标识符不能在该global语句前出现
# 列在global 语句后的标识符不能被定义成形参, 不能出现在for循环控制的目标、类定义和函数定义，或者import语句中

# 例子
x = 100
def f():
    def g():
        global x
        x = x * 99
        return x
    return g

print(f()())
# >>> 9900
print(x)
# >>> 9900


# 若不加global
x = 100
def f():
    def g():
        # global x
        x = x * 99
        return x
    return g

# print(f()())
# >>> UnboundLocalError: local variable 'x' referenced before assignment
print(x)
# # >>> 100


# 若用nonlocal
x = 100
def f():
    def g():
        nonlocal x
        # 注意, nonlocal statement会在run时在global层面检测,如果错误则没有任何代码会被执行
        x = x * 99
        return x
    return g

# print(f()())
# >>> SyntaxError: no binding for nonlocal 'x' found
# 注意这里nonlocal只搜索外部一层的, 不会继续寻找global

print(x)
# >>> won't be executed


# On the other hand, global does not care at all
x = 100
def f():
    global x
    global xx  # no xx as variable
    x = 99
    return x

print(f())
# >>> 99
print(x)
# >>> 99




# 赋值和申明顺序

# global
x = 50
def f():
    global x     # 先申明后改变,这可以
    x = 100
    return x+1

print(f())
# >> 101

x = 50
def f():
    x = 100     # 先新建一个同名变量,再global则不行
    global x
    return x+1

print(f())
# >> name 'x' is assigned to before global declaration

# nonlocal 也是同理
def f():
    x = 100
    def g():
        nonlocal x
        x = 50
        return x
    return g

print(f()())
# >>> 50

def f():
    x = 100
    def g():
        x = 50
        nonlocal x
        return x
    return g

print(f()())
# >>> SyntaxError: name 'x' is assigned to before nonlocal declaration
