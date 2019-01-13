# P005 Longest Palindromic String
# Medium


# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.


class Solution:
    def longestPalindrome(self, s):
        ### Time: O(N^2) + O(1/2N) = O(N^2)
        ### Space: O(N)
        ### Maximum time limit exceeded
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(s):
            if len(s) <= 1:
                return True
            else:
                return s[0] == s[-1] and is_palindrome(s[1:-1])

        if not s:
            return ''

        length, L = len(s), len(s)

        while L != 0:
            for i in range(0, length - L + 1):
                sample = s[i:i+L]
                if is_palindrome(sample):
                    return sample
            L -= 1


class Solution:
    def longestPalindrome(self, s):
        ### Time: O(N^2) + O(1/2N) = O(N^2)
        ### Space: O(N)
        ### Maximum time limit exceeded
        """
        :type s: str
        :rtype: str
        """



assert Solution().longestPalindrome('') == '', 'Edge 1'
assert Solution().longestPalindrome('a') == 'a', 'Edge 2'
assert Solution().longestPalindrome('aaa') == 'aaa', 'Edge 3'

assert Solution().longestPalindrome('babad') == 'bab' or 'aba', 'Example 1'
assert Solution().longestPalindrome('cbbd') == 'bb', 'Example 2'

assert Solution().longestPalindrome('bababadddddddddddd') == 'dddddddddddd', 'Extra 1'
assert Solution().longestPalindrome('babababa') == 'abababa' or 'bababab', 'Extra 2'

a = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
b = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
assert Solution().longestPalindrome(a) == b

print('all passed')