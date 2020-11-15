"""
https://leetcode.com/problems/length-of-last-word/
p058 Length of Last word
Easy

Given a string s consists of upper/lower-case alphabets and empty space characters " ", return the length of last word in the string.
If the last word does not exist, return 0

Note:
    A word is defined as a character sequence consists of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pass








if __name__ == "__main__":
    testCase = Solution()
    assert testCase.lengthOfLastWord("") == 0, "Edge 1"
    assert testCase.lengthOfLastWord(" ") == 0, "Edge 2"
    assert testCase.lengthOfLastWord("Hello World") == 5, "Regular"
    print("all passed")
