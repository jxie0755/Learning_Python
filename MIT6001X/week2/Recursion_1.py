# iteration method
# a * b
# break down to a + a + a... as a total b number of a.
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_iter(3, 4))

# Recursion method
def mult_iter2(a, b):
    if b == 1:
        return a
    else:
        return a + mult_iter2(a, b-1)

print(mult_iter2(3, 4))
