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


myanimal = Animal(3)
print(myanimal)






