# idea generalization
# High Order Programming : HOP, map
# a unary function and a collection of suitable arguments
# simple form

# apply function to a list of argument, each in turn
map(abs, [1, -2, 3, -4])
# return iterable

L = []
for elt in map(abs, [1, -2, 3, -4]):
    L.append(elt)
print(L)




