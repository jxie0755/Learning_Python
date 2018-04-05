# P003 Largest prime factor


# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# Version 1 Brutal force iteration over the (sqrt + 1) of the target
from math import sqrt
import time


def largetst_prime_factor(target):
    def is_prime(n):
        return all(n % i != 0 for i in range(2, n))

    maximum_possible_factor = round(sqrt(target))
    for i in range(maximum_possible_factor, 1, -1):
        if target % i == 0 and is_prime(i):
            return i

if __name__ == '__main__':
    assert largetst_prime_factor(13195) == 29, 'regular'
    t0 = time.time()
    print(largetst_prime_factor(600851475143))
    t1 = time.time()
    print(t1 - t0)
    # >>> 6857
    # passed
