# create anonymous function (with no name)

# in regular way:
def sq(x):
    return x**x
map(sq, [y for y in range(10)])
# this created a function called sq()

# in lamda way:
map(lambda x: x**x, [y for y in range(10)])
# define a function that x is the argument
# write out the function: x**x
# the parameter is to acutally be used as the argument

# practice
add = lambda x: x*2
print(list(map(add, [i for i in range(10)])))

