# CS61a Discussion 03 Trees & Sequences


# Q1 Index
# What would python display?

a = [1, 5, 4, [2, 3], 3]
print((a[0], a[-1])) # >>> 1 3
print(len(a)) # >>> 5
print(2 in a) # >>> False
print(4 in a) # >>> True
print(a[3][0]) # >>> 2

# Q2 Slicing
# What would python display?

a = [3, 1, 4, 2, 5, 3]
print(a[1::2]) # >>> [1, 2, 3]
print(a[:]) # >>> same as a
print(a[4:2]) # >>> []
print(a[1:-2]) # [1, 4, 2]
print(a[::-1]) # >>> reversied(a)


# List comprehensions
# What would python display?

print([i + 1 for i in [1, 2, 3, 4, 5] if i % 2 == 0])
# >>> [3, 5]

print([i * i - i for i in [5, -1, 3, -1, 3] if i > 2])
# >>> [20, 6, 6]

print([[y * 2 for y in [x, x + 1]] for x in [1, 2, 3, 4]])
# >>> [[2, 4], [4, 6], [6, 8], [8, 10]]


# Trees
