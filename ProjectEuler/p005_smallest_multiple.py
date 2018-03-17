# P005 Smalest multiple


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Brutal force
from functools import reduce

def even_distribute(n1, n2):
    """"find the positive number that can be evenly divided by numbers from range(n1, n2+1)"""
    sample, maximum = 1, reduce(lambda x, y: x*y, range(n1,n2+1))
    while sample <= maximum:
        print(sample)
        if all(sample % i == 0 for i in range(n1, n2+1)):
            return sample
        sample += 1

# print(even_distribute(1, 20))
# >>> this will take too much time
