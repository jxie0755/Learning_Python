
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

# 而且只是无法访问,不代表无法更改
denis.__score = 59
print(denis.__score) # >>> 59  # 注意,这里强行添加的仍然是一个外形是private实际是public的变量
denis.print_score()  # >>> Denis Xie has a score of 99  # 这里方法调用的仍然是init方法创造的真private变量

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
# 注意,这里针对方法做例子,但是对属性的调用同样成立
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

# 介绍一些用于获取对象信息的函数与方法

# type() 可以检查类型
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
# dir() 也很有用,返回全部可调用的属性和方法, 以包含字符串的list形式返回

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用str对象的__len__()方法，
# 所以，下面的代码是等价的
print(len('ABC'))       # >>> 3
print('ABC'.__len__())  # >>> 3

# 自制__special__函数
class People():
    def __len__(self):
        return 100
    def ppl(self):
        return 'People has power'
denis = People()
print(len(denis))  # >>> 100  # 只有特殊方法才可以这样
# print(ppl(denis))  # >>> NameError: name 'ppl' is not defined

# 当然既然能列出这属性和方法，也可以相应的修改
# python准备了getattr()、setattr()、hasattr()，可以直接操作一个对象的状态
# 具体函数使用已经有基础学习过,不再赘述

# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息
# 如果可以直接写：sum = obj.x + obj.y
# 就不要写：sum = getattr(obj, 'x') + getattr(obj, 'y')



print()
print('实例属性和类属性')

# 不要把多态应用到属性上,而只是应用到方法上

class Student(object):
    name = 'Student'

s = Student()
print(s.name)  # >>> Student
print(Student.name)  # >>> Student

# 类的名字是Student,类里的属性也叫Student.这会导致黑人问号脸
s.name = 'Denis'
print(s.name)  # >>> Denis
print(Student.name)  # >>> Student
del s.name # 如果删除实例的name属性
print(s.name)  # >>> Student  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

# * 在编写程序的时候，千万不要把实例属性和类属性使用相同的名字
# * 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
# * 也就是说,不要把多态应用到属性上,而只是应用到方法上
# * 注意,这里的属性,不是指__init__()创造的属性,因为那个属于方法范畴了. 这里属性指的是直接属性.



print()
print('使用slots')

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

    def __init__(self, name):
        self.name = name
        # self.score = score  # 一旦slots限制,即使是__init__()也不能违规创建其他属性

# d = Student('Denis', 99)  # >>> AttributeError: 'Student' object has no attribute 'score'

dd = Student('Denis')
dd.age = 25
# dd.whatever = 33  # >>> 'Student' object has no attribute 'whatever'
print(dd.name)  # >>> Denis
print(dd.age)  # >>> 25

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GoodStudent(Student):
    def __init__(self, name, age):
        self.name = name
        self.age = age

cc = GoodStudent('Cindy', 26)
cc.whatever = 123123
print(cc.whatever)  # >>> 13212



print()
print('使用@Property')
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

dd = Student('Denis', 59)
dd.score = 999
print(dd.score)  # >>> 999  # score can be changed easily, not a safe way of coding


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100.')
        self._score = value

dd = Student('Denis', 59)
# dd.set_score(199)  # >>> ValueError: score must between 0 - 100.
dd.set_score(99)
print(dd.get_score())  # >>> 99


# 把一个getter方法变成属性，只需要加上@property就可以了
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
# 于是，我们就拥有一个可控的属性操作

class Student(object):
    @property  # 此处将方法score变成属性
    def score(self):
        return self._score

    @score.setter  # .setter是一个property的固定的set属性,不能乱改
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value

d = Student()
d.score = 60
print(d.score)  # >>> 60  # 这个是方法变作的属性
print(d._score)  # >>> 60  # 这个是真属性
# d.score = 9999
# print(d.score)  # >>> ValueError: score must between 0 - 100!


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

dd = Student()
dd.birth = 1986
print(dd.age)  # >> 29
# dd.age = 35  # >>> AttributeError: can't set attribute

# * @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，减少了出错的可能性
# * 主要作用还是对于属性做限制,通过设定方法,但是这个方法又被@property变成属性,这样调用方法的时候看起来就像是在调用属性



print()
print('多重继承')

class Animal(object):
    def animalrun(self):
        print('I am running...')

class Runnable():
    def run(self):
        print("I can run...")

# 多重继承,继承不止一个父类
class Dog(Animal, Runnable):
    pass

didi = Dog()
didi.animalrun()  # >>> I am running...  # Animal类的方法
didi.run()        # >>> I can run...     # Runnable类的方法
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能

# 这种多重继承的设计通常称之为MixIn:
# * MixIn的目的就是给一个类增加多个功能
# * 在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
# * 通过各种组合继承类，不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
# * 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计
# * 只允许单一继承的语言（如Java）不能使用MixIn的设计



print()
print('定制类')

# 形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的

# __str__()
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"

    __repr__ = __str__

print(Student('Denis'))  # >>> <__main__.Student object at 0x10454fe80>
# 如果想改变以上输出结果，就需要用到__str___，在类里重新定义这个方法就可以了
print(Student('Denis'))  # >>> Student name is Denis

# 但是print()管的是输出string,而不是代表物体本身的string,所以repr()仍然按以前显示
print(repr(Student('Denis')))  # >>> <__main__.Student object at 0x104550f28>
# 说明直接显示变量不归__str__管了，由__repr__管

# __iter__() 和 __next__()
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
# 直到遇到StopIteration错误时退出循环
class Fib():
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器

    def __iter__(self):
        return self  # 实例本身即是迭代对象，故而返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10000:  # 退出循环条件
            raise StopIteration()
        return self.a

print(list(Fib()))
# >>> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素
# print(Fib()[5])  # >>> TypeError: 'Fib' object does not support indexing

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

print(Fib()[8])  # >>> 34

# __getattr__()
# 还记得之前如果访问实例中的属性不存在就会抛出的no attribute错误吗
# __getattr__可以动态的返回一个属性，当要访问的属性不存在的时候，Python解释器会试图调用__getattr__(XXX)来尝试获得需要的属性
# 利用这一点，可以把一个类的所有属性和方法调用全部动态化处理
class Chain():
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
# >>> /status/user/timeline/list

# __call__()
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
# 能不能直接在实例本身上调用呢？
class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f'My name is {self.name}.')

s = Student('Denis')
s()  # >>> My name is Denis.



print()
print('使用枚举类')
# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义
JAN = 1
FEB = 2
MAR = 3
#...
NOV = 11
DEC = 12

# 好处是简单，缺点是类型是int，并且仍然是变量

# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例
# 利用enum模块
from enum import Enum

Month = Enum('Month', (
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# >>>
# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12

# 本质上还是一个mapping
print(dict(Month.__members__.items()))
# {'Jan': <Month.Jan: 1>, 'Feb': <Month.Feb: 2>, 'Mar': <Month.Mar: 3>, 'Apr': <Month.Apr: 4>, 'May': <Month.May: 5>, 'Jun': <Month.Jun: 6>, 'Jul': <Month.Jul: 7>, 'Aug': <Month.Aug: 8>, 'Sep': <Month.Sep: 9>, 'Oct': <Month.Oct: 10>, 'Nov': <Month.Nov: 11>, 'Dec': <Month.Dec: 12>}











