# Week 1, HW 01

# Q1 A Plus Abs B
# Fill in the blanks in the following function definition for adding a to the absolute value of b, without calling abs

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs."""
    if b < 0:
        f = sub  # replace f with an alternative function
    else:
        f = add  # same as above
    return f(a, b)

if __name__=='__main__':
    print('Q1:')
    assert a_plus_abs_b(2, 3) == 5
    assert a_plus_abs_b(2, -3) == 5
    print('all passed')


# Q2: Two of Three
# Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers. Use only a single line for the body of the function.

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the positive numbers a, b, and c"""
    return a*a + b*b + c*c - min(a, b, c)**2
    return max(a*a+b*b, a*a+c*c, b*b+c*c) # alternative

if __name__=='__main__':
    print('Q2:')
    assert two_of_three(1, 2, 3) == 13
    assert two_of_three(5, 3, 1) == 34
    assert two_of_three(10, 2, 8) == 164
    assert two_of_three(5, 5, 5) == 50
    print('all passed')


# Q3: Largest Factor
# Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.

def largest_factor(n):
    """Return the largest factor of n that is smaller than n."""
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

if __name__=='__main__':
    print('Q3:')
    assert largest_factor(15) == 5  # factors are 1, 3, 5
    assert largest_factor(80) == 40  # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    assert largest_factor(13) == 1  # factor is 1 since 13 is prime
    print('all passed')


# Q4: If Function vs Statement
# Let's write a function that does the same thing as an if statement.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result

# Despite the doctests above, this function actually does not do the same thing as an if statement in all cases. To prove this fact, write functions c, t, and f such that with_if_statement returns the number 1, but with_if_function does not (it can do anything else):

def with_if_statement():
    if c():
        return t()
    else:
        return f()  # if return f(), then t() will not be examined

def with_if_function():
    return if_function(c(), t(), f())  # all c(), t(), f() will be examined before return value

# define c(), t() and f():
def c():
    return True

def t():
    return 1

def f():
    return 1/0   # the key is whether f is called or not

# test it out
if __name__ == '__main__':
    print('Q4')
    print(with_if_statement())
    # print(with_if_function())  # lead to ZeroDivisionError
    print('passed')

# The difference is not the link before c() to t() and f(), but about if python interpreter will examine the same object before output


# Q5: Hailstone
# Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

# Pick a positive integer n as the start.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Continue this process until n is 1.
# The number n will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

# This sequence of values of n is often called a Hailstone sequence, Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length."""
    count = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
            count += 1
        else:
            n = n * 3 + 1
            count += 1
    print(n)
    return count

if __name__=='__main__':
    print('Q5:')
    assert hailstone(10) == 7
    print('all passed')
