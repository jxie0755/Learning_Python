# p009 Palindrome Number
# Easy

# Determine whether an integer is a palindrome. Do this without extra space.
# Negative integer will not be a palindrome

# """
# :type x: int
# :rtype: bool
# """

class Solution(object):
    def isPalindrome(self, x):  # string method, takes extra space
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]

    def isPalindrome2(self, x):  # use divmod method, no need for extra space
        if x < 0:
            return False
        half_palindrome = 0
        while x > half_palindrome:
            half_palindrome = half_palindrome * 10 + x % 10
            x //= 10
            print(x, half_palindrome)
        return x == half_palindrome

if __name__ == '__main__':
    assert Solution().isPalindrome2(2147447412) == True, 'Is palindrome'
    assert Solution().isPalindrome2(-2147447412) == False, 'Not palindrome'
    print('all passed')
