# p680 Valid Palindrome II
# Easy

# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
# Note:
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.

# """
# :type s: str
# :rtype: bool
# """

class Solution:
    def validPalindrome(self, s):
        ### time limit exceeded
        if s == s[::-1]:
            return True
        else:
            for i in range(len(s)):
                lst = list(s)
                del lst[i]
                if lst == lst[::-1]:
                    return True
        return False

    def validPalindrome(self, s):
        ### use string slice combination, still exceed time limit
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            s_new = s[:i] + s[i + 1:]
            if s_new == s_new[::-1]:
                return True
        return False
        # 当string变得十分长,没有本质上的区别

    def validPalindrome(self, s):
        ### from two ends, check step by step
        for i in range(len(s) // 2):
            # if head != tail, check if and element needs to be removed
            if s[i] != s[len(s) - 1 - i]:
                head, tail = i, len(s) - 1 - i
                # two possibilities, remove element at head or tail, and check the rest
                return s[head:tail] == s[head:tail][::-1] or s[head + 1:tail + 1] == s[head + 1:tail + 1][::-1]
        # if nothings goes wrong, it is naturally a palindrome
        return True


if __name__ == '__main__':
    assert Solution().validPalindrome('abccba') == True, 'born to be (even)'
    assert Solution().validPalindrome('abcba') == True, 'born to be (odd)'
    assert Solution().validPalindrome('aabbcecbXbaa') == True, 'delete a letter'
    assert Solution().validPalindrome('abxcxdcba') == False, 'does not work'
    print('all passed')
