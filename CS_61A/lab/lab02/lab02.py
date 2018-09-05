"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Q1 Lambda the Free What Would Python Display?
# python3 ok -q lambda -u

# Q2 Higher Order Functions What Would Python Display?
# python3 ok -q hof -u

# Lambda Functions

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    def FUNC(x):
        def g(y):
            return func(x, y)
        return g
    return FUNC

    # one liner using lambda function:
    # return lambda arg1: lambda arg2: func(arg1, arg2)

