"""
Learn shallow copy and deepcopy
https://docs.python.org/3/library/copy.html
"""

import copy

# normal slice copy will be shallow copy
a = [[1,2,3], [2,3,4], [3,4,5]]
b = a[:]
c = copy.copy(a)
d = copy.deepcopy(a)

a[0].append(10)
print(a)  # >>> [[1, 2, 3, 10], [2, 3, 4], [3, 4, 5]]
print(b)  # >>> [[1, 2, 3, 10], [2, 3, 4], [3, 4, 5]]
# both a and b changed, because b is a copy of a, but a contains mutable list, which b is also refering to the same list

print(c)  # >>> [[1, 2, 3, 10], [2, 3, 4], [3, 4, 5]]
# c as a shallow copy act the same as a slice copy

print(d)  # >>> [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
# d as a deep copy, is not affected by the execution of a[0].append(10)
