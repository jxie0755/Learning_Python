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


# create a new type as a fraction type of number
# 分子Numerator and 分母denominator
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


oneHalf = Fraction(1,2)
twoThirds = Fraction(2,3)
threeQuarters = Fraction(3,4)
print(f'{oneHalf}, {twoThirds}')  # >>> 1 / 2, 2 / 3

print(oneHalf + twoThirds)  # >>> 7 / 6
print(oneHalf - twoThirds)  # >>> -1 / 6








