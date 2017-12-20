# eval() function is to convert a string to a piece of codes

# Example: list.count()
a = [1,2,3,1,2,3,4,1,2,5,6,7]
b = 'count'

target = 2


# regular way
print(a.count(target))  # >>> 3

# use f string to bring variable in, but also use 'count' string to execute the count() function.
print(eval(f'{a}' + '.' + b + f'({target})'))  # >>> 3
