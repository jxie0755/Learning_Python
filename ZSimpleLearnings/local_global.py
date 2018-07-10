
def f(x):
    def g(y):
        # nonlocal x
        z = x + y
        return z
    return g

print(f(4)(5))  # function to call x in previous frames
# >>> 9

def f(x):
    def g(y):
        # nonlocal x
        x = 5 + y
        return x
    return g

print(f(4)(5))  # function create x in new frames
# >>> 10  # still work



def f(x):
    def g(y):
        x = x + y
        return x
    return g

# function create the same variable in previous frames and use the value in previous frames
# print(f(4)(5)) # >>> error
# UnboundLocalError: local variable 'x' referenced before assignment

def f(x):
    def g(y):
        nonlocal x   # unless nonlocal it
        x = x + y
        return x
    return g

print(f(4)(5))
# >>> 9


x = 10
def f(x):
    def g(y):
        global x   # this pull x from global
        x = x + y
        return x
    return g

print(f(4)(5))
# >>> 15
print(x)  # this will permanantly change the global value
# >>> 15
