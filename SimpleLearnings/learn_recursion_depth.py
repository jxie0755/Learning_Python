"""This is to learn the difference between a true recursion and a fake recursion"""


# Fake recursion
def recur(n):
    print(n)
    return recur(n+1)

# recur(1)
# >>>
# This will continuesly print n, all the way to 998
# Raise the error message:
# RecursionError: maximum recursion depth exceeded while calling a Python object

# This is because the recursion keep moving forward, all the way to 999 depth


# True recursion
call = 0
def fib(n):
    global call
    if n == 0:
        call += 1
        return 0
    elif n == 1:
        call += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(20))
# >>> 6765
print(call)
# >>> 10946
# Even the function has been called 10946 times, it does not reach to the maximum recursion depth
# Actually the depth is still 20.

# print(fib(500))
# >>> This will still not hit the maximum recursion depth, even thought it takes long time to execute

print(fib(1000))
# >>> RecursionError: maximum recursion depth exceeded in comparison
# This will hit the maximum recursion depth.
