# P029 Divide Two Integers
# Medium

# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Note:
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.

class Solution:

    # Version A, Integer method
    # Time:  O(logn) = O(1), Space: O(1)
    def divide(self, dividend: "int", divisor: "int") -> "int":

        def manual_divide(son, mom):
            """
            Helper function to achive log(n) division by doubling mom, before son > mom
            Mom and Son are both non-negative integers
            """
            result = 1
            while son - mom > mom:
                mom += mom
                result += result
            new_son = son - mom
            return result, new_son

        result = 0
        son, mom = abs(dividend), abs(divisor)
        while son != 0 and son >= mom:
            temp_result, son = manual_divide(son, mom)
            result += temp_result

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            result *= -1

        if result >= 2147483648:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result


class Solution(object):

    # Version B
    # Same idea but use bit calculation << and >>
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':

        positive = (dividend < 0) is (divisor < 0)  # great way to align two integer on the same sideK
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


if __name__ == "__main__":
    assert Solution().divide(1, 3) == 0, "Edge 1"

    assert Solution().divide(10, 3) == 3, "Example 1"
    assert Solution().divide(7, -3) == -2, "Example 2"
    assert Solution().divide(1, 1) == 1, "Example 3"

    assert Solution().divide(-2147483648, 1) == -2147483648, "Edge 2"
    assert Solution().divide(-2147483648, -1) == 2147483647, "Edge 3"

    print("all passed")
