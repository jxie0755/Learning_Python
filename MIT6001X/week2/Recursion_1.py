# iteration method
# a * b
# break down to a + a + a... as a total b number of a.
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    print(result)
    return result

mult_iter(3, 4)

