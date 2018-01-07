# p007 Reverse Integer 
# Easy

# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
# The 32-bit int data type can hold integer values in the range of −2,147,483,648 to 2,147,483,647.

class Solution(object):
    def reverse(self, x):  # beats 3.88%
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            result = int(str(x)[::-1])
            return result if result <= 2147483647 else 0
        elif x < 0:
            result = int('-' + str(x)[-1:0:-1])
            return result if result >= -2147483648 else 0


assert Solution().reverse(123) == 321
assert Solution().reverse(-120) == -21
assert Solution().reverse(1534236469) == 0
print('done')
