"""
https://leetcode.com/problems/palindrome-number/
p009 Palindrome Number
Easy

Determine whether an integer is a palindrome. Do this without extra space.
Negative integer will not be a palindrome
"""

class Solution_A:

    def isPalindrome(self, x: int) -> bool:
        """String method, takes extra space"""
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]

class Solution_B:
    def isPalindrome(self, x: int) -> bool:
        """Divmod method"""
        if x < 0:
            return False
        copy, reverse = x, 0
        while copy > 0:
            reverse = reverse * 10 + copy % 10
            copy //= 10
        return reverse == x


if __name__ == "__main__":
    testCase = Solution_B()
    assert testCase.isPalindrome(21477412) == True, "Is palindrome (even)"
    assert testCase.isPalindrome(12321) == True, "Is palindrome (odd)"
    assert not testCase.isPalindrome(1477412), "Not palindrome"
    assert testCase.isPalindrome(1), "Single digit 1"
    assert testCase.isPalindrome(0), "Single digit 0"

    print("all passed")
