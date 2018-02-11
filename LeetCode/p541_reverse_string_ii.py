# p541 Reverse String II
# Easy

# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string.
# If there are less than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

# """
# :type s: str
# :type k: int
# :rtype: str
# """

class Solution:
    def reverseStr(self, s, k):  # O(n) method
        start = 0
        result = ''
        while start <= len(s):
            result += s[start:start + k][::-1] + s[start + k: start + 2 * k]
            start += 2 * k
        return result


if __name__ == '__main__':
    assert Solution().reverseStr('abcdefg', 2) == 'bacdfeg', 'regular'
    assert Solution().reverseStr('abcdefg', 1) == 'abcdefg', 'k=1, do nothing'
    assert Solution().reverseStr('abcdefghi', 2) == 'bacdfeghi',  'one extra'
    assert Solution().reverseStr('abcdefgh', 3) == 'cbadefhg', 'partial reverse'
    assert Solution().reverseStr('abcdefgh', 2) == 'bacdfegh', 'double length'
    assert Solution().reverseStr('abcdefg', 10) == 'gfedcba', 'k > len(s), complete reverse'
    print('all passed')

