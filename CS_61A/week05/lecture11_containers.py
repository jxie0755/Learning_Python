# CS61A Lecture 11 Containers

# Lists

odds = [41, 43, 47, 49]
print(len(odds))
print(odds[1])
print(odds[0] - odds[3] + len(odds))
print(odds[odds[3]-odds[2]])

# Containers

digits = [1, 8, 2, 8]
print(1 in digits)
print('1' in digits)
print([1, 8] in digits)
print([1, 2] in [[1, 2], 3])
