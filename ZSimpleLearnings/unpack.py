# Unpack can be used to assign multiple value to multiple variables in one line.

# number of variables must equal to number of generated values!!
a, b = 2, 3  
a, b = [2, 3]
a, b = (2, 3)
a, b = {2, 3}
a, b = {2:'x', 3:'y'}  # go with keys
# all above: a=2, b=3

# can be used in iterators 
x, y, z = range(3)
print(x, y, z)  # >>> 0 1 2

# can also be used in functions that generate more than one values
x, y = divmod(5, 2)
print(x, y)  # >>> 2, 1

# multiple unpack
for x, y in [(1,2), (2,3), (3,4)]:
    print(x, y)
    
# keys and values are unpack of dict
d ={'a': 1, 'b': 2}
for k, v in d.items():
    print(k,v)

dd = [('a', 1, 'x'), ('b', 2, 'y'), ('c', 3, 'z')]
for k, v, c in dd:
    print(k)
# >>>
# a
# b
# c

# must match k, v, c (3 items) to the same number of elements in sub-tuples (3 items).
