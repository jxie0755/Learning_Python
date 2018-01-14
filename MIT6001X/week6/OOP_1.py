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

class IntSet(object):
    def __init__(self, lst=[]):  # use default empty list incase want to create an empty set.
        self.lst = lst
        setlst = []
        for i in lst:
            if i not in setlst:
                setlst.append(i)
        self.data = setlst
    def __str__(self):
        return "{" + str(sorted(self.data))[1:-1] + "}"   # make sure it automactically sort from small to large

    def insert(self, elm):
        if elm not in self.data:
            self.data.append(elm)

    def member(self, elm):
        return elm in self.data

    def remove(self, elm):
        if elm in self.data:
            self.data.remove(elm)
        else:
            raise ValueError(f'{str(elm)} not found in set')

set1 = IntSet([1, 1, 2, 2, 3, 3, 4, 4, 4, 5])
print(set1)  # >>> {1, 2, 3, 4, 5}

set1.insert(5)
set1.insert(6)
print(set1)  # >>> {1, 2, 3, 4, 5, 6}

print(set1.member(6))  # >>> True
print(set1.member(7))  # >>> False

set1.remove(3)
# set1.remove(8)
print(set1)  # >>> {1, 2, 4, 5, 6}

set2 = IntSet()
print(set2)  # >>> {}





