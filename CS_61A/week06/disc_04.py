# CS61A Discussion 04 Nonlocals & Mutation


# Nonlocal
def stepper(num):
    def step():
        nonlocal num
        num = num + 1
        return num
    return step

s = stepper(3)
print(s()) # >>> 4
print(s()) # >>> 5


lamb = 'da'
def da(da):
    def lamb(lamb):
        nonlocal da
        def da(nk):
            da = nk + ['da']
            da.append(nk[0:2])
            return nk.pop()
    da(lamb)
    return da([[1], 2]) + 3

print(da(lambda da: da(lamb)))
# >>>
# 2 + 3 = 5

# Write a function that takes in a value x and updates and prints the result based on input functions

def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def f(fn):
        nonlocal n
        n = fn(n)
        print(n)
        return f
    return f
