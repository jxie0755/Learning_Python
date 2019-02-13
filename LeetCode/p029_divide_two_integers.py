# P029 Divide Two Integers
# Medium


# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.


# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':

        def manual_divide(mom, son):
            """Mom and Son are both non-negative integers"""
            result = 1
            while mom - son > son:
                son += son
                result += result
            return result, mom - son

        if divisor == 0:
            return None

        result = 0
        mom, son = abs(dividend), abs(divisor)
        while mom != 0 and mom >= son:
            temp_result, mom = manual_divide(mom, son)
            result += temp_result


        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            result -= result + result

        if result >= 2147483648:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result


if __name__ == '__main__':
    assert Solution().divide(10, 0) == None, "Edge1"
    assert Solution().divide(1, 3) == 0, "Edge 2"

    assert Solution().divide(10, 3) == 3, "Example 1"
    assert Solution().divide(7, -3) == -2, "Example 2"
    assert Solution().divide(1, 1) == 1, "Example 3"

    assert Solution().divide(-2147483648, -1) == 2147483647, "Edge 3"
    assert Solution().divide(2147483648, -1) == -2147483648, "Edge 3"
    assert Solution().divide(2147483649, -1) == -2147483648, "Edge 3"

    print("all passed")
