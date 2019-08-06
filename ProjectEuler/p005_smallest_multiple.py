"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


# Version 1: Brutal force
from functools import reduce

def even_distribute(n1, n2):
    """"find the positive number that can be evenly divided by numbers from range(n1, n2+1)"""
    sample, maximum = 1, reduce(lambda x, y: x*y, range(n1,n2+1))
    while sample <= maximum:
        if all(sample % i == 0 for i in range(n1, n2+1)):  # list comprehension is used
            return sample
        sample += 1

# print(even_distribute(1, 20))
# >>> 232792560   # this will take too much time (~200 sec)



# Version 2: Use greatest common divisor, to calculate

def smallest_multiple(n1, n2):
    """"find the positive number that can be evenly divided by numbers from range(n1, n2+1)"""

    def lowest_common_multiple(x, y):
        for i in range(min(x, y), 0, -1):
            if x % i == 0 and y % i == 0:
                return x * y // i

    return reduce(lowest_common_multiple, range(n1, n2+1))

if __name__ == "__main__":
    assert smallest_multiple(1, 10) == 2520, "regular"
    print(smallest_multiple(1, 20))
    # >>> 232792560    # straightforward math calculation takes almost no itme.
    # passed
