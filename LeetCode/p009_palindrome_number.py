# p009 Palindrome Number
# Easy

# Determine whether an integer is a palindrome. Do this without extra space.
# Negative integer will not be a palindrome

class Solution(object):
    def isPalindrome(self, x):  # beats 24.10%
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]

print(Solution().isPalindrome(2147447412))
print(Solution().isPalindrome(-2147447412))
