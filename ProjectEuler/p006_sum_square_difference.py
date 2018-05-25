# P006 Sum square difference

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)^2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference(n1, n2):
    square_sum = sum(map(lambda x:x**2, range(n1, n2+1)))
    sum_square = sum(range(n1, n2+1)) ** 2
    return sum_square - square_sum

if __name__ == '__main__':
    assert sum_square_difference(1, 10) == 2640, 'regular'
    print(sum_square_difference(1, 100))
    # >>> 25164150
    # passed
