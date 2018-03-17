# P005 Smalest multiple


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from functools import reduce

if __name__ == '__main__':
    print(reduce(lambda x, y: x*y, range(1,21)))
    # >>>> 2432902008176640000
    # maximum is a very big number

# Brutal force will not work as the number is too big
# use greatest common divisor, to calculate
def smallest_multiple(n1, n2):
    """"find the positive number that can be evenly divided by numbers from range(n1, n2+1)"""

    def common_multiple(x, y):
        for i in range(min(x, y), 0, -1):
            if x % i == 0 and y % i == 0:
                return x * y // i

    return reduce(common_multiple, range(n1, n2+1))

if __name__ == '__main__':
     print(smallest_multiple(1, 20))
     # >>> 232792560
     # passed
