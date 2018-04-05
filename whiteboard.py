# Test speed

# Version 1: Brutal force
from functools import reduce
import time

def even_distribute(n1, n2):
    """"find the positive number that can be evenly divided by numbers from range(n1, n2+1)"""
    sample, maximum = 1, reduce(lambda x, y: x*y, range(n1,n2+1))
    while sample <= maximum:
        if all(sample % i == 0 for i in range(n1, n2+1)):  # list comprehension is used
            return sample
        sample += 1

t1 = time.time()
print(even_distribute(1, 20))
t2 = time.time()
print(t2 - t1)
# >>> 232792560   # this will take too much time (~200 sec)
