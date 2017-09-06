from sympy import Symbol, solve
x=Symbol('x')
y=Symbol('y')
print(solve([2*x-y-3, 3*x+y-7], [x,y]))

from sympy import *
x=Symbol('x')
y=Symbol('y')
print(solve([2*x-y-3, 3*x+y-7], [x,y]))

squares = []
for x in range(1,11):
    square = x**2
    squares.append(square)
    print(squares)  # 很有意思,它会依次打印一个list,每次比上一次多一个range item

current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

