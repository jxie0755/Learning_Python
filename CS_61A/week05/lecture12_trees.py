# CS61A Lecture 12 Trees

# Slicing
odds = [3, 5, 7, 9, 11]
print(list(range(1, 3)))
print([odds[i] for i in range(1, 3)])
print(odds[1:3])
print(odds[1:])
print(odds[:3])
print(odds[:])

# Aggregation

print(sum(odds))
print(sum({3:9, 5:25}))
print(max(range(10)))
print(max(range(10), key=lambda x: 7 - (x-2)*(x-4)))
print(all([x < 5 for x in range(5)]))
print(perfect_square = lambda x: x == round(x ** 0.5) ** 2)
print(any([perfect_square(x) for x in range(50, 60)]) # Try ,65))
