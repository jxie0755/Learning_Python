class A(object):
    def __init__(self, name):
        self.name = name

    def foo(self, x):
        return x*2

class B(A):
    def foo(self, x):
        temp = super().foo(2)
        return temp + 10

bb = B('b')
print(bb.foo(2))