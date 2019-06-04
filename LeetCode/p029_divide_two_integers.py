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
    # Time:  O(logn) = O(1)
    # Space: O(1)
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


class Solution(object):
    # Same idea but use bit calculation << and >>
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result, dvd, dvs = 0, abs(dividend), abs(divisor)
        while dvd >= dvs:
            inc = dvs
            i = 0
            while dvd >= inc:
                dvd -= inc
                result += 1 << i
                inc <<= 1
                i += 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            return -result
        else:
            return result

    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


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
