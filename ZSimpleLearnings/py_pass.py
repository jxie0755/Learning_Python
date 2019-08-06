"""This is to learn how to use pass in python"""


# 当你在编写一个程序时，执行语句部分思路还没有完成，这时你可以用pass语句来占位，也可以当做是一个标记，是要过后来完成的代码。比如下面这样：
# bypass the unfinished function
def fun(x):
    for i in range(5):
        pass

print("hello world")  # >>> hello world

# 定义一个函数iplaypython，但函数体部分暂时还没有完成，又不能空着不写内容，因此可以用pass来替代占个位置


# 写一个OOP子类,用于完全继承父类,省略多态
class Person(object):
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

print(type(Student))  # >>> <class "type">
print(Student.mro())  # >>> [<class "__main__.Student">, <class "__main__.Person">, <class "object">]

# 子类拥有OOP继承结构,并完全继承父类, 只是没有其他改写
denis = Student("Denis Xie")
print(denis.name)  # >>> Denis Xie

# pass基本就是用于确立程序结构时,留下代码残缺导致无法运行
