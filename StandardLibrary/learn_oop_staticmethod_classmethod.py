# Python面向对象编程中，类中定义的方法可以是 @classmethod 装饰的类方法，也可以是 @staticmethod 装饰的静态方法，用的最多的还是不带装饰器的实例方法
# 如果把这几个方法放一块，对初学者来说无疑是一头雾水，那我们该如何正确地使用它们呢？

# 先来看一个简单示例：

class Test(object):
    def m1(self, n): # m1 是实例方法, 第一个参数必须是 self（约定俗成的）
        print("self:", self, "n=", n)

    @classmethod
    def m2(cls, n): # m2 是类方法，第一个参数必须是cls（同样是约定俗成）
        print("cls:", cls, "n=", n)

    @staticmethod
    def m3(n):     # m3 是静态方法，参数根据业务需求定，可有可无
        print("staticmethod", "n=", n)

# 我在类中一共定义了3个方法，，。，。

a = Test()
a.m1(1) # >>> self: <__main__.Test object at 0x1086ac630> n= 1
# Test.m1(1) 不work, 实例方法必须要基于实例

Test.m2(2) # >>> cls: <class '__main__.Test'> n= 2
a.m2(2)    # >>> cls: <class '__main__.Test'> n= 2   都work, 类方法可以基于类或者类的实例

Test.m3(3)  # >>> staticmethod n= 3
a.m3(3)     # >>> staticmethod n= 3  都work,静态方法和类方法非常类似
