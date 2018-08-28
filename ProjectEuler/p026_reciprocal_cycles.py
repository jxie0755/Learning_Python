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
from decimal import *
getcontext().prec = 3000  # !!! The key is to ensure the length of the string is long enought to show the reciprocal pattern!!

def longest_reciprocal(n):
    """return the pattern and length of pattern for 1/x
    for x in the range(2, n)"""

    # get a list of the decimal part of each 1/x, in string.
    str_dict = {}
    for i in range(2, n):
        float_num = Decimal(1) / Decimal(i)
        str_dict[i] = str(float_num)[2:-1]

    # remove the non-reciprocals
    k_to_remove = [k for k, v in str_dict.items() if len(v) < 2999]
    for i in k_to_remove:
        del str_dict[i]

    result = {}
    for k,v in str_dict.items():
        result[k] = find_reciprocal_pattern(v)

    answer = max(result, key=lambda x: len(result.get(x)))
    print('Pattern is', result[answer], 'from', answer)

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


if __name__ == '__main__':
    assert longest_reciprocal(10) == 7
    longest_reciprocal(1000)
    # >>> 983
    # correct
