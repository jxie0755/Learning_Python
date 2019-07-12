# P023 Non-abundant sums


# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time

start_time = time.time()

from itertools import combinations_with_replacement as CR


def find_abundant_num(limit):
    result = []
    for num in range(1, limit + 1):
        divisor_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisor_sum += i
        if divisor_sum > num:
            result.append(num)
    return result


def all_non_sumable():
    """find all integers that can be written as the sum of two abundant numbers under 28123"""
    abundant_num_list = find_abundant_num(28123)
    sumable = set([x + y for x, y in CR(abundant_num_list, 2)])
    non_sumable = set(range(1, 28124)) - sumable
    return sum(non_sumable)


if __name__ == "__main__":
    print(all_non_sumable())
    print("--- %s seconds ---" % (time.time() - start_time))
    # >>>
