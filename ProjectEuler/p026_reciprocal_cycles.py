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
getcontext().prec = 99

def longest_reciprocal(n):
    """return the pattern and length of pattern for 1/x
    for x in the range(2, n)"""

    # get a list of the decimal part of each 1/x, in string.
    str_dict = {}
    for i in range(2, n):
        float_num = Decimal(1) / Decimal(i)
        str_dict[i] = str(float_num)[2:]

    # remove the non-reciprocals
    k_to_remove = [k for k, v in str_dict.items() if len(v) < 99]
    for i in k_to_remove:
        del str_dict[i]

    for k,v in str_dict.items():
        print(k,v)







if __name__ == '__main__':
    longest_reciprocal(10)