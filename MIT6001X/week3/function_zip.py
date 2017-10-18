# zip function, connects the items, but do not return anything until use a data structure to it.
# only pair the least item numbers in all list.

L1 = [1, 28, 36, 99]
L2 = [2, 57, 9]
L3 = [3, 39, 77]

li = list(zip(L1, L2))
print(li)

di = dict(zip(L1, L2)) # must be two arguments
print(di)

tu = tuple(zip(L1, L2))
print(tu)

tu2 = tuple(zip(L1, L2, L3))
print(tu2)
