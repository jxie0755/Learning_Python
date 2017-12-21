# getattr(a, b) == a.b if b is an attribute of an object(anything follows a '.')

x = 'append'
y = 'remove'
z = 'insert'
u = 'count'

# List operation
lst = [1,1,2,3,4,5]
getattr(lst, x)(6)
print(lst)  # >>> [1, 1, 2, 3, 4, 5, 6]

getattr(lst, y)(6)
print(lst)  # >>> [1, 1, 2, 3, 4, 5]

getattr(lst, z)(0, 6)
print(lst)  # >>> [6, 1, 1, 2, 3, 4, 5]

print(getattr(lst, u)(1))  # >>> 2

# string operation
x = 'upper'
y = 'isdigit'
z = 'zfill'
u = 'count'

d = 'abcdefg'

print(getattr(d, x)())  # >>> 'ABCDEFG'
print(getattr(d, y)())  # >>> False
print(getattr(d, z)(10))  # >>> 000abcdefg
print(getattr(d, u)('c'))  # >>> 1

import itertools
op = 'chain'
list2d = [[1,2,3],['a','b','c'], [7], [8,9]]
print(list(getattr(itertools, op)(*list2d)))
# >>> [1, 2, 3, 'a', 'b', 'c', 7, 8, 9]
