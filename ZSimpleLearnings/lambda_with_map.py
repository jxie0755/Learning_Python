# lambda function can take more than 1 argument.

f = lambda x,y:x*y
a = [(2,3), (3,4), (4,5)]

result = [f(x, y) for x, y in a]
print(result)  # >>> [6, 12, 20]

b = [2, 3, 4]
c = [3, 4, 5]
result = list(map(lambda x,y:x*y, b, c))
print(result) # >>> [6, 12, 20]
