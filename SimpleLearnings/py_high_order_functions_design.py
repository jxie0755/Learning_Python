"""
Showed by designing a number of function to calculate the square root of a number
http://composingprograms.com/pages/16-higher-order-functions.html

This is a high-order function that can be used to keep updating a value until it meets the requirement
this method uses the update x by calling average(x, a/x), different than binary search method.
"""

def improve(update, close, guess=1):
    while not close(guess):     # keep trying until close returns True
        guess = update(guess)   # a method to update the value so that it can be tested by close again
    return guess                # when it is done, the final guess is the answer

def average(x, y):                         # define averaging method as a pre-processing method for update
    return (x + y)/2

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance          # define what is close enough as it will never reach to full equivalence

def sqrt(a):
    def sqrt_update(x):  # if not close enough (x*x not close to a)
        return average(x, a/x)   # this is defined because update can take 1 argument, but we need 2 here to update
    def sqrt_close(x):   # use as the close judgement
        return approx_eq(x * x, a)  # this is called to because update can take 1 argument, but we need 2 here to update
    return improve(sqrt_update, sqrt_close)

print(sqrt(5))



# Simplified version by putting approx_eq inside of sqrt_close and average inside of sqrt_update

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def sqrt(a):
    def sqrt_update(x):  # if not close enough (x*x not close to a)
        return (x + a/x)/2   # this is called because update can take 1 argument, but we need 2 here to update
    def sqrt_close(x):   # use as the close judgement
        return abs(x*x - a) < 1e-15  # this is called to because update can take 1 argument, but we need 2 here to update
    return improve(sqrt_update, sqrt_close)

print(sqrt(5))


# Compose two functions

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

# This leads to idea of lambda function, we don't need to have a name for each function when use inside of another function
# compose function will be then:

def compose1(f, g):
    return lambda x: f(g(x))

s = lambda x: x * x

print(s)
# >>> <function <lambda> at 0xf3f490>

print(s(12))
# >>> 144


# Curried Functions
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

print(curried_pow(2)(3))
# >>> equals to h(3), but x is given in curried_pow
# when h look for x, it won't find, but it will find in the last environment of curried_pow
# >>> 8


# Currying and Uncurrying with 2 arguments

def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

print(pow(2,3))  # >>> 8
pow_curried = curry2(pow)  # new curried function
print(pow_curried(2)(3))  # >>> 8  # Same as pow(2, 3)


def uncurry2(g):
    """Return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f

print(uncurry2(pow_curried)(2, 4))  # >>> 16  # Same as pow(2,4)



# The currying leads to python function decorator

# Learned in OOP where class methods can be applied by decorator
# Here it is straightly applied on normal functions

# Python provides special syntax to apply higher-order functions as part of executing a def statement, called a decorator.
# Perhaps the most common example is a trace

def trace(fn):
    def wrapped(x):
        print("-> ", fn, "(", x, ")")
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

print(triple(12))
# >>>
# ->  <function triple at 0x7f738d9b6598> ( 12 )
# 32


# Equals to:

def trace(fn):
    def wrapped(x):
        print("-> ", fn, "(", x, ")")
        return fn(x)
    return wrapped

def tripleN(x):
    return 3 * x

tripleN = trace(tripleN)

print(tripleN(12))
# >>>
# ->  <function triple at 0x7f738d9b6598> ( 12 )
# 32

# Essentially is to create a function that curry the original function inside.
