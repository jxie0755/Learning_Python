print('Coordinate example')
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return f'<{self.x},{self.y}>'

    def __sub__(self, other):      # this is actually from operator module!!
                                   # see other special methods in Language reference section 3.3
        return Coordinate(self.x - other.x, self.y - other.y)

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    # Add an __eq__ method that returns True if coordinates refer to same point in the plane
    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

    # Define __repr__, a special method that returns a string that looks like a valid Python expression
    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'

c = Coordinate(3,4)
print(c.x, c.y)  # >>> 3 4
origin = Coordinate(0,0)

# if using instance to call a method, then self is already the instance, so only need one paramenter
print(c.distance(origin))  # >>> 5.0

# if use a class method, then you must provide self as an parament
print(Coordinate.distance(c, origin))  # >>> 5.0

print(c)  # >>> <3,4>
print(isinstance(c, Coordinate))  # >>> True

c2 = Coordinate(1,1)
print(c-c2) # >>> <2,3>

cdash = Coordinate(3,4)
print(c == cdash)

ccopy = eval(repr(c))
print(repr(c))  # >>> Coordinate(3,4)
print(ccopy)

# create a new type as a fraction type of number
# 分子Numerator and 分母denominator
print()
print('Fraction example')
class Fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return f'{self.numer} / {self.denom}'

    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer() / self.getDenom()

oneHalf = Fraction(1,2)
twoThirds = Fraction(2,3)
threeQuarters = Fraction(3,4)
print(f'{oneHalf}, {twoThirds}')  # >>> 1 / 2, 2 / 3

print(oneHalf + twoThirds)  # >>> 7 / 6
print(oneHalf - twoThirds)  # >>> -1 / 6

print(threeQuarters.convert())  # >>> 0.75

# another example: a set of integers
# basic idea is the same as python sets (no repeat items), but to achieve by codes
# methods can be:
# insert : add an elements
# member: boolean a member's exisitence in set
# remove: remove an element, error if not present


print()
print('intSet example')
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    # Define an intersect method that returns a new intSet containing elements that appear in both sets. (交集)
    def intersect(self, other):
        intersect = intSet()
        for i in self.vals:
            if i in other.vals:
                intersect.vals.append(i)
        return intersect

    # Add the appropriate method(s) so that len(s) returns the number of elements in s
    def __len__(self):
        return len(self.vals)

emptset = intSet()
print(emptset)  # >>> {}

set1 = intSet()
set1.insert(1); set1.insert(1); set1.insert(2); set1.insert(2); set1.insert(3); set1.insert(4); set1.insert(5)
set2 = intSet()
set2.insert(2); set2.insert(4); set2.insert(4); set2.insert(4); set2.insert(6); set2.insert(8); set2.insert(8); set2.insert(8)
print(set1)  # >>> {1, 2, 3, 4, 5}

set1.insert(5)
set1.insert(6)
print(set1)  # >>> {1, 2, 3, 4, 5, 6}

print(set1.member(6))  # >>> True
print(set1.member(7))  # >>> False

set1.remove(3)
# set1.remove(8)
print(set1)  # >>> {1, 2, 4, 5, 6}

print(set1.intersect(set2))  # >>> {2, 4, 6}


# Mimic real life
print()
print('Hierarchy example')
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None  # start with no name

    # getters and setters should always be used outside of the class to access the data attributes.

    # getter
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    # setter
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=''):
        self.name = newname
    def __str__(self):
        return 'animal:' + str(self.name) + ':' + str(self.age)

myAnimal = Animal(3)
myAnimal.set_name('foobar')
print(myAnimal)

class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return 'cat:' + str(self.name) + ':' + str(self.age)

jelly = Cat(1)
jelly.set_name('JellyBelly')
print(jelly)                  # >>> cat:JellyBelly:1
print(Animal.__str__(jelly))  # >>> animal:JellyBelly:1  # still get access to Animal's method by using this way


class Rabbit(Animal):
    def speak(self):
        print('meep')
    def __str__(self):
        return 'rabbit:' + str(self.name) + ':' + str(self.age)

peter = Rabbit(5)
jelly.speak()  # >>> meow
peter.speak()  # >>> meep

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag  # call Class tag
        Rabbit.tag += 1  # change Class tag, so that each tag is unique
        # every instance created, __init__ is called, and class variable changes
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other)
    def __eq__(self, other):  # using the rid as unique identification
        parent_same = self.parent1.rid == other.parent1.rid \
                      and self.parent2.rid == other.parent2.rid
        parent_diff = self.parent1.rid == other.parent2.rid \
                      and self.parent2.rid == other.parent1.rid
        return parent_same or parent_diff
    # get_name and get_age inherit from Animal class

print()
print('new Rabbit class example')
peter = Rabbit(2); peter.set_name('Peter')
hopsy = Rabbit(3); hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
print(peter.get_rid(), hopsy.get_rid(), cotton.get_rid())  # >>> 001 002 003
print(cotton.get_parent2().get_name())  # >>> Hopsy
cotton2 = hopsy + peter
print(cotton2.get_rid(), cotton2.get_parent1().get_name(), cotton2.get_parent2().get_name())
# >>> 0004 Hopsy Peter
print(cotton == cotton2) # >>> True

print()
print('Person class')
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, 'is', diff, 'years older than', other.name)
        else:
            print(self.name, 'is', -diff, 'years younger than', other.name)
    def __str__(self):
        return 'person:'+str(self.name)+':'+str(self.age)

eric = Person('eric', 45)
john = Person('john', 55)
eric.speak()  # >>> hello
eric.age_diff(john)  # >>> eric is 10 years younger than john
john.age_diff(eric)  # >>> john is 10 years older than eric

import random
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()  # gives a float between 0 and 1
        if r < 0.25:
            print('i have homework')
        elif 0.25 <= r < 0.5:
            print('i need sleep')
        elif 0.5 <= r < 0.75:
            print('i should eat')
        else:
            print('i am watching tv')
    def __str__(self):
        return 'student:'+str(self.name)+':'+str(self.age)+':'+str(self.major)

fred = Student('Fred', 18, 'Course VI')
print(fred)  # >>> studentFred:18:Course VI
fred.speak()  # >>> random

# Python supports a limited form of multiple inheritance, demonstrated in the following code
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

# When resolving a reference to an attribute of an object that's an instance of class D
# Python first searches the object's instance variables then uses a simple left-to-right, depth first search through the class hierarchy.
# In this case that would mean searching the class C, followed the class B and its superclasses

obj = D()
print(obj.a)  # >>> 2  # __init__ goes for the last get called, which is B class
print(obj.b)  # >>> 3
print(obj.c)  # >>> 5
print(obj.d)  # >>> 6
obj.x()       # >>> A.x
obj.y()       # >>> C.y
obj.z()       # >>> D.z
