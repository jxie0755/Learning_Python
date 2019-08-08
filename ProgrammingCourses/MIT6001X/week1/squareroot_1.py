# using algorithm to find a square root of a target.

target = input("Please in put an integer, must >= 0:")
x = 0
while x**2 < int(target):
    x += 1
if x**2 == int(target):
    print("The square root of", int(target), "is", x)
else:
    print(int(target), "is not a perfect square")
