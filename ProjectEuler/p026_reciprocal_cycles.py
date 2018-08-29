# P026 Reciprocal cycles

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.



# Solution
# Use decimal to get the reliable float calculation and control the display to 99 place after digit
import time
from decimal import *

def longest_reciprocal(n):
    """return the pattern and length of pattern for 1/x
    for x in the range(2, n)"""

    getcontext().prec = n * 3  # !!! The key is to ensure the length of the string is long enought to show the reciprocal pattern!!

    # get a list of the decimal part of each 1/x, in string.
    str_dict = {}
    for i in range(2, n):
        float_num = Decimal(1) / Decimal(i)
        str_dict[i] = str(float_num)[2:-1]

    # remove the non-reciprocals
    k_to_remove = [k for k, v in str_dict.items() if len(v) < n * 3 - 1]
    for i in k_to_remove:
        del str_dict[i]

    result = {}
    for k,v in str_dict.items():
        result[k] = find_reciprocal_pattern(v)

    answer = max(result, key=lambda x: len(result.get(x)))
    return answer


def find_reciprocal_pattern(s):
    """give a string of numbers as the decimal part of a float
    find out the pattern of the reciprocal part
    if it is not reciprocal, return ''
    """
    limit = int(len(s) // 3)
    for start in range(limit+1):
        for end in range(start+1, start + limit):
            sample, rest = s[start:end], s[start:]
            sample_len, rest_len = len(sample), len(rest)
            repeat_n, tail = divmod(rest_len, sample_len)
            if sample * repeat_n + sample[0:tail] == rest:
                return sample
    return ''

# For a better algorithm by using the division method, please check:
# ZCodeSnippets.reciprocal_pattern.py

if __name__ == '__main__':
    print('Test enumeration method:')

    assert longest_reciprocal(10) == 7

    start_time = time.time()
    print(longest_reciprocal(1000))
    print(f"--- {time.time() - start_time}s seconds ---\n")
    # >>> 983
    # correct

    print('passed\n')




# Version 2
# Optimized algorithm by using divide calculation.

def find_reciprocal(numerator, denominator):
    """find out the pattern of the reciprocal part when numerator / denominator
    numerator: integer
    denominator: integer
    num
    return: a string of the pattern numbers
    """

    assert numerator < denominator, 'numerator must be smaller than denominator'

    decimal_part, remainder_list = '', [numerator % denominator]
    numerator *= 10 # start with numerator * 10 to avoid the first decimal point

    for i in range(denominator):
        quotient, numerator = divmod(numerator, denominator)
        if numerator == 0:
            return 'the result is not reciprocal'
        else:
            decimal_part += str(quotient)
            if numerator not in remainder_list:
                remainder_list.append(numerator)
                numerator *= 10
            else:
                start = remainder_list.index(numerator)
                pattern = decimal_part[start:]
                return pattern

def longest_reciprocal_2(n):
    result = {}
    for i in range(2, n):
        result[i] = len(find_reciprocal(1, i))
    return max(result, key=result.get)



if __name__ == '__main__':
    print('Test new algorithm:')

    assert find_reciprocal(1, 7) == '142857'   # = 0.(142857)
    assert find_reciprocal(1, 70) == '142857'  # = 0.0(142857)
    assert find_reciprocal(2, 3) == '6'        # = 0.(6)
    assert find_reciprocal(1, 12) == '3'       # = 0.08(3)

    a = find_reciprocal(1, 983)
    assert len(a) == 982

    start_time = time.time()
    print(longest_reciprocal_2(1000))
    print(f"--- {time.time() - start_time}s seconds ---\n")

    print('passed')
