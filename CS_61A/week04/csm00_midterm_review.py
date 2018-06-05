# CSM00 Mideterm 1 Review

# Q1
apple = 4
def orange(apple):
    apple = 5
    def plum(x):
        return lambda plum: plum * 2
    return plum

print(orange(apple)("hiii")(4))
# >>> 8


# Q2
def bar(f):
    def g(x):
        return f(x-1)
    return g
f = 4
print(bar(lambda x: x + f)(2))
# >>> 5


# Q3
inception = lambda secret: lambda: secret
print(inception(5)())
# >>> 5


