"""
用于优化代码重用
https://www.zhihu.com/question/26930016/answer/99243411
"""

def sq(x):
    print(x**2)

# 第一版函数
def foo():
    print("i am foo")
def bar():
    print("i am bar")

# 第二版函数,加入新功能(嵌套一个函数)
# def foo():
#     print("i am foo")
#     sq(4)
# foo()
# >>>
# i am foo
# 16

# 若还有很多函数都需要外加这个sq(4)函数怎么办?? 是否把其他每个函数都加一行sq(4)?

# 新建一个函数,把所有其他需要加sq(4)的函数包装起来
def sqX(function):
    function()
    sq(4)

sqX(foo)
# >>>
# i am foo
# 16

# 如果每个函数都写成sqX(foo),sqX(bar)这样看起来太丑陋
# 使用decorator方法
def sqX(func):
    def __decorator():
        func()
        sq(4)
    return __decorator

@sqX
def foo():
    print("i am foo")
foo()
# >>>
# i am foo
# 16

@sqX
def bar():
    print("i am bar")
bar()
# >>>
# i am bar
# 16

# 这样只需要在原函数定义前面加一个@sqX即可,所有运行foo()和bar()的代码均可维持不变



# 用于避免代码重构所带来的问题
# http://codingpy.com/article/python-properties-refactoring/

# 第一版本
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

# 被人应用
m1 = Money(27, 12)
print(m1.dollars, "dollars,", m1.cents, "cents")
# >>> 27 dollars, 12 cents

# 第二版本
class Money:
    def __init__(self, dollars, cents):  # 改进__init__方法
        self.total_cents = dollars * 100 + cents
# 这一修改带来一个后果: 引用Money类的每一行代码都必须要调整 (特别是被其他团队复用代码的情况)

# 被应用的代码将不能再运行,除非修改
m1 = Money(27, 12)
# print(m1.dollars, "dollars,", m1.cents, "cents")
# >>> AttributeError: "Money" object has no attribute "dollars"

# 第二版本优化
class Money:
    def __init__(self, dollars, cents):  # 与第二版本相同的__init__方法
        self.total_cents = dollars * 100 + cents

    # Getter and setter for dollars...
    @property
    def dollars(self):
        return self.total_cents // 100
    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents

    # And the getter and setter for cents.
    @property
    def cents(self):
        return self.total_cents % 100
    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollars + new_cents

# 修改了__init__方法,但是通过装饰器,重设dollar和cents属性
# 不再需要修改应用代码
m1 = Money(27, 12)
print(m1.dollars, "dollars,", m1.cents, "cents")
# >>> 27 dollars, 12 cents
