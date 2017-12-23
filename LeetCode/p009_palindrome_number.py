# Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]

print(Solution().isPalindrome(-2147447412))
