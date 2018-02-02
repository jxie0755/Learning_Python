# p028 implement strStr()
# Easy

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# """
# :type haystack: str
# :type needle: str
# :rtype: int
# """

class Solution:
    def strStr(self, haystack, needle):
        length = len(needle)
        index = 0
        while index <= len(haystack) - length:
            if haystack[index:index+length] == needle:
                return index
            index += 1
        return -1


if __name__ == '__main__':
    assert Solution().strStr('abcdeabc', 'de') == 3
    assert Solution().strStr('abcdeabc', 'zz') == -1
    print('all passed')
