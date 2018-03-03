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

# Quiz
print('\nQuiz')
print('\nQ1: what would python display')
print(True and 13)  # >>> 13
print(False or 0)   # >>> 0
print(not 10)       # >>> False
print(not None)     # >>> True

print()
# print(True and 1 / 0 and False)     # >>> ZeroDivisionError
print(True or 1 / 0 or False)       # >>> True
print(True and 0)                   # >>> 0
print(False or 1)                   # >>> 1
print(1 and 3 and 6 and 10 and 15)  # >>> 15
print(0 or False or 2 or 1 / 0)     # >>> 2

print()
print(not 0)         # >>> True
print((1+1) and 1)   # >>> 1
# print((1/0) or True)  # ZeroDivisionError  # Still have to evaluate <left> even if returning <right>
print((True or False) and False)  # >>> False

# Q2 Loops
print('\nQ2: Loops')
n = 3
while n >= 0:
    n -= 1
    print(n)
# >>>
# 2
# 1
# 0
# -1

# n = 4
# while n > 0:
#     n += 1
#     print(n)
# >>>
# 5
# 6
# 7
# ...forever continue

def go(n):
    if n % 2 != 0:
        print(n / 2)
        return
    while n > 0:
        print(n)
        n = n // 2

go(4)
# >>>
# 4
# 2
# 1

go(5)
# >>>
# 2.5

zero = 2
while zero != 0:
   zero = zero // 2
   print(zero)
# >>>
# 1
# 0

# positive = 28
# while positive:
#     print("positive?")
#     positive -= 3
# >>>
# positive? (28)
# positive? (25)
# positive? (22)
# positive? (19)
# positive? (16)
# positive? (13)
# positive? (10)
# positive? (7)
# positive? (4)
# positive? (1)
# positive? (-2)
# ...continue forever

positive = -9
negative = -12
while negative:
    if positive:
        print(negative)
    positive += 3
    negative += 3
# >>>
# -12 (p=-6, n=-9)
# -9 (p=-3, n=-6)
# -6 (p=0, n=-3)
#    (p=3, n=0)
# end

# Coding practice
print('\nCoding Practice')
print('\nQ3: Repeated')
# Implement the repeated function, which takes a one-argument function f, a positive integer n, and a parameter x. It returns the result of composing, or applying, f n times on x, i.e., f(f(...f(x)...)).
def repeated(f, n, x):
    """Returns the result of composing f n times on x."""
    "*** YOUR CODE HERE ***"

if __name__ == '__main__':
    def square(x):
        return x * x
    assert repeated(square, 2, 3) == 81, 'square(square(3)), or 3 ** 4'
    assert repeated(square, 1, 4) == 16, 'square(4)'
    assert repeated(square, 6, 2) == 18446744073709551616, 'big number'

    def opposite(b):
        return not b
    assert repeated(opposite, 4, True) == True
    assert repeated(opposite, 5, True) == False
    assert repeated(opposite, 631, 1) == False
    assert repeated(opposite, 3, 0) == True
    print('all passed')

print('\nQ4: Sum Digits')
# Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)
def sum_digits(n):
    """Sum all the digits of n."""
    "*** YOUR CODE HERE ***"

if __name__ == '__main__':
    assert sum_digits(10) == 1, '# 1 + 0 = 1'
    assert sum_digits(4224) == 12, '4 + 2 + 2 + 4 = 12'
    assert sum_digits(1234567890) == 45
    print('all passed')

print('\nQ5: Double Eights')
# Write a function that takes in a number and determines if the digits contain two adjacent 8s.
def double_eights(n):
    """Return true if n has two eights in a row."""
    "*** YOUR CODE HERE ***"

if __name__ == '__main__':
    assert double_eights(8) == False
    assert double_eights(88) == True
    assert double_eights(2882) == True
    assert double_eights(880088) == True
    assert double_eights(12345) == False
    assert double_eights(80808080) == False
    print('all passed')


# Optional Questions
print('\nOptional Questions')
