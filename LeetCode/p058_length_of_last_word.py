# p058 Length of Last word
# Easy

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0
# Note: A word is defined as a character sequence consists of non-space characters only.

# """
# :type s: str
# :rtype: int
# """

class Solution:
    def lengthOfLastWord(self, s):
        if len(s.split()) == 0:
            return 0
        return len(s.split()[-1])

    def lengthOfLastWord(self, s):
        ### without extra space for creating a list, and avoid iterate over the whole string
        cnt = 0
        for v in reversed(s):  # create reversed iterator
            if v.isspace():  # to avoid end with a ' '
                if cnt != 0:  # force to move down from the end ' ',
                    break  # but break at next ' '
            else:
                cnt += 1
        return cnt


if __name__ == '__main__':
    assert Solution().lengthOfLastWord('Hello World') == 5, 'regular'
    assert Solution().lengthOfLastWord('') == 0, 'empty'
    assert Solution().lengthOfLastWord(' ') == 0, 'empty 2'
    print('all passed')
