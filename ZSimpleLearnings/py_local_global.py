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

def f(x):
    def g(y):
        # nonlocal x
        z = x + y
        return z
    return g

print(f(4)(5))  # function to call x in previous frames
# >>> 9

def f(x):
    def g(y):
        # nonlocal x
        x = 5 + y
        return x
    return g

print(f(4)(5))  # function create x in new frames
# >>> 10  # still work



def f(x):
    def g(y):
        x = x + y
        return x
    return g

# function create the same variable in previous frames and use the value in previous frames
# print(f(4)(5)) # >>> error
# UnboundLocalError: local variable 'x' referenced before assignment

def f(x):
    def g(y):
        nonlocal x   # unless nonlocal it
        x = x + y
        return x
    return g

print(f(4)(5))
# >>> 9


x = 10
def f(x):
    def g(y):
        global x   # this pull x from global
        x = x + y
        return x
    return g

print(f(4)(5))
# >>> 15
print(x)  # this will permanantly change the global value
# >>> 15
