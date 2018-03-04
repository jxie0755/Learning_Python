# Lab 01: Expressions and Control Structures

# Expression and Stamentment
print('\nExpression and Staments')
print(3)
print(5)
print(True)

# Assignment Statements
print('\nAssignment statements')
a = (100 + 50) // 2
print(a)

# Boolean operator
print('\nBoolean operator')
print(5>3 and 3>5)
print(5>3 or 3<5)
print(not 5>3)

# Testing short circuiting theory
print('\nShort circuiting theory')
print(True or 1/0)  # >>> True, bypassing the evaluation of 1/0
# print(1/0 or 5/3)  # ZeroDivisionError
print(False and 1/0)  # >>> False

# Division
print('\nDivision')
print(1 / 2)
print(5 // 2)
print(5 % 2)

# Function
print('\nFunction')
def f(x):
    return x**2
print(f(5))

# Control
# if statement
print('\nif statement')
def largerthanthree(x):
    if x > 3:
        return True
    else:
        return False
print(largerthanthree(2))

# while loop
print('\nwhile loop')
def power_ten(x):
    result = 2
    while x < 10:
        result *= 2
        x += 1
    return result
print(power_ten(2))
