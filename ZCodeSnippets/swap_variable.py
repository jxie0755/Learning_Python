# this is the code for switching the value of two variables without creating another variable
a = 5
b = 7

a = a + b
b = a - b
a = a - b
print('a is now', a, '\nb is now', b)

a = 5
b = 7

a = a - b
b = a + b
a = b - a
print('a is now', a, '\nb is now', b)

