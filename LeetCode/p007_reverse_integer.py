# p007 Reverse Integer
# Easy

# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
# The 32-bit int data type can hold integer values in the range of −2,147,483,648 to 2,147,483,647.

# """
# :type x: int
# :rtype: int
# """

class Solution:
    def reverse(self, x):
        # string method, takes extra space
        if x >= 0:
            result = int(str(x)[::-1])
            return result if result <= 2147483647 else 0
        else:
            result = int('-' + str(x)[-1:0:-1])
            return result if result >= -2147483648 else 0

    def reverse2(self, x):
        # no extra space used, by using divmod method
        absX = abs(x)
        result = 0
        while absX > 0:
            result = result * 10 + absX % 10
            absX //= 10
        if x < 0:
            result = -result
        return result if 2147483647 > result > -2147483648 else 0

if __name__ == '__main__':
    assert Solution().reverse(123) == 321, 'regular'
    assert Solution().reverse(-120) == -21, 'tricky reverse'
    assert Solution().reverse(1534236469) == 0, 'large number'
    assert Solution().reverse(0) == 0, 'zero'
    print('all passed')
