# https://stackoverflow.com/questions/47722712/use-map-for-functions-that-does-not-return-a-value

# map() returns a map object that is iterable

# This won't work if the function is used for side-effect (other than return a value)
result = []
a = [1,2,3,4,5,6,7]
def f(x):
    result.append(x**2)
map(f, a)  # this function only returns an iterable object that does nothing
print(result)  # >>> []

list(map(f, a))  # list() consumes the iterator of map object
print(result)  # >>> [1, 4, 9, 16, 25, 36, 49]



# Examine the effect one by one
result = []
b = [1,2,3,4,5,6,7]
mapobj = map(f, a)  # this function only returns an iterable object that does nothing
print(mapobj)  # >>> <map object at 0x103d5f390>

next(mapobj)
print(result)  # >>> [1]

next(mapobj)
print(result)  # >>> [1, 4]

next(mapobj)
print(result)  # >>> [1, 4, 9]