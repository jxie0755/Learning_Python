# Sequoia's notes - Variable practice

# Cross out the values below that cause an error when you type them into the Python interpreter.
# For values that don't cause an error:
# 1. Write what it evaluates to.
# 2. Label it an int, float, str, or bool.

print(.1)
print("one")
print("two")
# print('three")  # quote mark wrong
print(2*False)  # >>> 0
# print(int("five"))  # can't int() a pure letter string
# print(0/0)  # ZeroDivisionError
print(4/2)
print(4//2)
print(2*"hi")
# print(True + "")
print("C"+"S")
print(2**6)
print(9%7)
print("Say "Hi!"")
print("Say "Bye!"")
print("The letter "H"")
# print("The letter "H"")


# What Would python do?
print()
print(int(True))   # >>> 1
print(int(False))  # >>> 0
print(float(True))   # >>> 1.0
print(float(False))  # >>> 0.0
print(str(True))   # >>> "True"
print(str(False))  # >>> "False"
print(float(0.000))
print(bool(False))
# print(int("4.0"))  # Error
print(str(0.000))


# Variable assignment
print()
dragon = "dragon"
x = 18 % 4  # >>> 2
n, i = "kn", "ki"
knight = 5
dragons, knight, king = x*dragon, i+"ng", knight*x
print(dragons)  # >>> "dragondragon"
print(knight)  # >>> "king"
print(king)   # >>> 10

print()
square = 4
circle = 4 - (4 * (40 % 21 + 2) + 4 // 2) / 100   # >>> 3.14
square, circle, shape = square ** 2, square ** 2, square + circle
shape -= int(shape) // int(square)
print(square)  # >>> 16
print(circle)  # >>> 16
print(shape)   # >>> 7.14

print()
c = "C"
"c = "twelve""
s = "S"
c, c = s, s = c + s, s + str(True)
print(c)  # >>> "STrue"
print(s)  # >>> "STrue"
