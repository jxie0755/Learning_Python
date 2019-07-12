# https://www.jianshu.com/p/14b8ebf93b73


# __new__方法
# _init__其实不是实例化一个类的时候第一个被调用 的方法
# 当使用 Persion(name, age) 这样的表达式来实例化一个类时，最先被调用的方法 其实是 __new__ 方法

# __init__是在类实例创建之后调用, 而 __new__方法正是创建这个类实例的方法
# __new__ 方法创建实例对象供__init__ 方法使用，__init__方法定制实例对象

print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
class newStyleClass(object):
    # In Python2, we need to specify the object as the base.
    # In Python3 it's default.

    def __new__(cls):
        print("__new__ is called")
        return super(newStyleClass, cls).__new__(cls)

    def __init__(self):
        print("__init__ is called")
        print("self is: ", self)

a = newStyleClass()
print(a)
# >>>
# __new__ is called
# __init__ is called
# self is:  <__main__.newStyleClass object at 0x0000027C728C5588>
# <__main__.newStyleClass object at 0x0000027C728C5588>

# __new__函数首先被调用，构造了一个newStyleClass的实例，接着__init__函数在__new__函数返回一个实例的时候被调用，并且这个实例作为self参数被传入了__init__函数

# 这里需要注意的是，如果__new__函数返回一个已经存在的实例（不论是哪个类的），__init__不会被调用:
class returnExistedObj(object):
    def __new__(cls):
        print("__new__ is called")
        return object.__new__(object)

    def __init(self):
        print("__init__ is called")

b = returnExistedObj()
print(b)
# >>>
# __new__ is called
# <object object at 0x000001755B15C0C0>

# 如果我们在__new__函数中不返回任何对象，则__init__函数也不会被调用
class notReturnObj(object):
    def __new__(cls):
        print("__new__ is called")

    def __init__(self):
        print("__init__ is called")

c = notReturnObj()
print(c)
# >>>
# __new__ is called
# None

# 可见如果__new__函数不返回对象的话，不会有任何对象被创建，
# __init__函数也不会被调用来初始化对象


# 总结
# __init__不能有返回值
# __new__函数直接上可以返回别的类的实例
# 只有在__new__返回一个新创建属于该类的实例时当前类的__init__才会被调用



# 一般用不上__new__方法，__new__方法可以用在下面二种情况:
# 1. 继承不可变数据类型时需要用到__new__方法(like int, str, or tuple
# 2. 用在元类，定制创建类对象
