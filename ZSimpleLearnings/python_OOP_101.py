
# 一篇文章搞懂Python中的面向对象编程
# http://yangcongchufang.com/%E9%AB%98%E7%BA%A7python%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/python-object-class.html


print()
print('基础知识')

# 类(Class)和实例(Instance)是面向对象最重要的概念
# simplest way of creating a class
class Student(object):
    pass

print(Student)  # >>> <class '__main__.Student'>
denis = Student()
print(denis)    # >>> <__main__.Student object at 0x7f510c8f8400>

# 可以自由地给一个实例变量绑定属性

denis.name = 'Denis Xie'
print(hasattr(denis, 'name'))  #>>>  True

# 类同时也可以起到模板的作用，我们可以在创建一个类的时候，把一些认为公共的东西写进类定义中去，在python中通过一个特殊的__init__方法实现
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

# __init__方法的第一个参数永远都是self,表示创建实例本身
# 在__init__方法内部，可以把各种属性绑定到self，因为self指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
denis = Student('Denis Xie', 99)
print(denis.name)  # >>> Denis Xie
print(denis.score)  # >>> 99

# 和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时不用传递该参数。
# 除此之外，类的方法和普通函数没有什么区别。

# 面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。
# 我们可以通过外部函数来访问这些数据
def print_score(std):
    print(f"{std.name} has a score of {std.score}")

print_score(denis)  # >>> Denis Xie has a score of 99

# 既然我们创建的实例里有自身的数据，如果想访问这些数据，就没必要从外面的函数去访问
# 可以在Student类内部去定义这样一个访问数据的函数，这样就把“数据”和 "函数"给封装起来了。

# 这些封装数据的内部函数和Student类本身关联起来的，我们称之为类的方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f"{self.name} has a score of {self.score}")

denis = Student('Denis Xie', 99)
denis.print_score()  # >>> Denis Xie has a score of 99

# 数据和逻辑都被封装起来，直接调用方法即可，但却可以不用知道内部的细节

# 总结:
# *类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
# *方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# *通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

# *和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
denis = Student('Denis Xie', 99)
cindy = Student('Cindy Tian', 100)
denis.gender = 'male'
print(denis.gender)  # >>> male  # attribute only for denis
# print(cindy.gender)    # >>> AttributeError: 'Student' object has no attribute 'gender'



print()
print('访问限制')

# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性

# change data from outside codes
denis.name = 'Jia Xie'
denis.score = 59
denis.print_score()  # >>> Jia Xie has a score of 59

# 如果想让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以双下划线开头，就变成了一个私有变量(private)，只有内部可以访问，外部不能访

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print(f"{self.__name} has a score of {self.__score}")


denis = Student('Denis Xie', 99)
# print(denis.__name)   # >>> AttributeError: 'Student' object has no attribute '__name'
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮

# 注意private attribute必须在class中定义,不然从外部是无法写入的,这里__gender仍然是public attribute
denis.__gender = 'male'
denis.__gender = 'female'
print(denis.__gender)  # >>> female

# 如果外部还需要访问到这两个内部状态的话，可以给Student类增加get_name和get_score这样的方法。
# 如果外部还有修改需求的话，就给该类再增加set_score或set_name方法。用这样的方式去get() set() 一个内部保护变量
# 具体代码不再赘述

# *需要注意的是，Python中如果变量名以双下划线开头和结尾的，是特殊变量__special__是可以直接从类外部访问的。
# *有时你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的.
# 但按照约定俗成的规定，意思就是"虽然我可以被访问，但是，请把我视为私有变量"
# *双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量

class Student(object):
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender__ = gender

    def print_score(self):
        print(f"{self.__name} has a score of {self.__score}")

denis = Student('Denis Xie', 99, 'male')
print(denis.__gender__)  # >>> male        # __special__可以从外部访问
print(denis._Student__name)  # >>> Denis Xie   # __private 仍然从外部访问

# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名
# Python的访问限制其实并不严格，主要靠自觉, 防君子不防小人

print(dir(denis))  # 可以发现private变量名字是如何被解释器改变的


print()
print('继承和多态')

# create a class Animal(), and a subclass Dog()
class Animal(object):
    def run(self):
        print('running...')

class Dog(Animal):
    pass

little_dog = Dog()
little_dog.run()  # >>> running...
# 子类获得了父类的全部功能。Dog()里继承了run()函数，可以给自己的实例里直接用

# 子类和父类如果定义的时候都有个run()?
class Animal(object):
    def run(self):
        print('running...')

class Dog(Animal):
    def run(self):
        print('dog running...')

little_animal = Animal()
little_dog = Dog()
little_dog.run()   # >>> dog running...
# 子类的的方法如果和父类的方法重名，子类会覆盖掉父类。因为这个特性，就获得了一个继承的好处”多态”

print(isinstance(little_dog, Dog))     # >>> True
print(isinstance(little_dog, Animal))  # >>> True   # 即使dog对于超类也是True
print(isinstance(little_animal, Dog))  # >>> False  # 父类实例不属于子类

# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量
# 先再添加一个Cat子类
class Cat(Animal):
    def run(self):
        print('cat running...')

def animal_run(animal):
    animal.run()

animal_run(Animal())  # >>> running...
animal_run(Dog())     # >>> dog running...
animal_run(Cat())     # >>> cat running...

# Dog作为Animal的子类，不必对animal_run()做任何修改。
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因在于多态

# 多态的好处就是，当我们需要传入Dog、Cat 等子类时，我们只需要接收Animal类型就可以了
# 因为子类终究都是Animal类型，由于Animal类型有run()方法，因此会自动调用实际类型的run()方法，这就是多态的意思
# 总结,多态的好处就是利用与父类相同的方法名,来运行父类的方法,但是对于各子类却有不同的结果

# python动态语言特性:
# 凡是一个类含有同名方法均可以实现运行,不是必须要属于Animal的子类
class Timer():
    def run(self):
        print('Start...')

animal_run(Timer())  # >>> Start...
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子

# 总结
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不是必须的,这与静态语言有很大不同



print()
print('获取对象信息')


