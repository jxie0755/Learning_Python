class Parent(object):

    def foo(self, x):
        return x ** 2


a = Parent()
print(a.foo(5))  # >>> 25

class Child(Parent):

    def foo(self, x):
        pre = Parent.foo(self, x)
        return pre + 1

b = Child()
print(b.foo(5))  # >>> 26


# 即使是无关的类都可以强制继承一个类的方法

class Other(object):
    pass

c = Other()

print(Parent.foo(c, 10)) # >>> 100
print(Child.foo(c, 10))  # >> 101

