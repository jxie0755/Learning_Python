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

# 采用super()方式时，会自动找到第一个多继承中的第一个父类
bb = B()
# >>>
# A  # 来自继承A类init的print
# B  # 来自B类init的print

cc = C()
# >>>
# A  # 比之前少一个A,因为super()函数只继承第一个父类B,A的init被略过
# B  # 来自继承B类中的print
# C  # 来自C类中的init的print

