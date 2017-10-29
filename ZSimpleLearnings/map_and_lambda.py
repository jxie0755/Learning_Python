# Testing multiple map()
l = [1, -1, '2', '0', 33, '-5', 9]
print(max(list(map(abs, list(map(int, l))))))

# Testing lambda
print(list(map(lambda x: x ** 2, list(map(int, l)))))

