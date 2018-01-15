# super主要用于继承时,不写父类名称,这样父类被改变时,减少代码改动

# 经典方式
class A():
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        A.__init__(self)  # 经典方式直接call父类A的init方法
        print('B')

class C(B, A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C')

bb = B()
# >>>
# A  # 来自继承A类init的print
# B  # 来自B类init的print

cc = C()
# >>>
# A  # 来自继承A类init的print
# A  # 来自继承B类中的init的A.init的print
# B  # 来自继承B类中的print
# C  # 来自C类中的init的print

# 采用新式类，要求最顶层的父类一定要继承于object，这样就可以利用super()函数来调用父类的init()等函数
print()
class A(object):
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        super().__init__()
        print('B')

class C(B, A):
    def __init__(self):
        # A.__init__(self)  # 只有补一个A类的init在前面才可以跟上例相同输出结果
        super().__init__()  # 只会寻求第一个父类,这里也就是B类
        print('C')

# 采用super()方式时，会自动找到第一个多继承中的下一个类(不是父类!)
bb = B()
# >>>
# A  # 来自A类init的print
# B  # 来自B类init的print

cc = C()
# >>>
# A  # 来自B类中的super()下一个类为A,所以来自A的init的print
# B  # 来自继承B类中的print
# C  # 来自C类中的init的print



# Another example
print()
class Person(object):
    def show_my_power(self):
        print("I am a person, I can walk!")

class Singer(Person):
    def show_my_power(self):
        super().show_my_power()
        print("I am a singer, I can sing!")

class Actor(Person):
    def show_my_power(self):
        super().show_my_power()
        print("I am an actor, I can act!")

class Artist(Singer, Actor):
    pass

if __name__ == "__main__":
    a = Artist()
    a.show_my_power()

# >>>
# I am a person, I can walk !
# I am an actor, I can act !
# I am a singer, I can sing !

# 注意顺序问题,竟然是先出最高父类,再出第二父类,顺序逆向, 原因:
# super在singer power之前, super追寻到actor,actor中super又在actor power之前,所以最先print的是person power

# 不同于特殊方法init, 这里的show_my_power将展示所有父类的方法,而不是只输出第一顺序父类
# 如果Singer和Actor不用super语句,那么只会输出Singer的show_my_power(第一顺序父类)

# 方法解析顺序（Method Resolution Order, MRO）列表，它代表了类继承的顺序
# 并遵循以下三条原则：
# *子类永远在父类前面
# *如果有多个父类，会根据它们在列表中的顺序被检查
# *如果对下一个类存在两个合法的选择，选择第一个父类
print(Artist.mro())  # >>>
# [<class '__main__.Artist'>,
# <class '__main__.Singer'>,
# <class '__main__.Actor'>,
# <class '__main__.Person'>,
# <class 'object'>]

# 由于python3简写了super(), 实际上是super(class, self), 而这里没有父类子类概念,只搜索class在MRO中的下一个类

class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")

class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")

print(C.mro())  # >>>
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
c = C()  # >>>
# enter C
# enter A
# enter B
# enter Base
# leave Base
# leave B
# leave A
# leave C
