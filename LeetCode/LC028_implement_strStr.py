"""
https://leetcode.com/problems/implement-strstr/
p028 implement strStr()
Easy

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution_A:

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Simple iteration
        """

        length = len(needle)
        for index in range(len(haystack) - length + 1):
            if haystack[index:index + length] == needle:
                return index
        return -1


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.strStr("", "") == 0, "Edge 0"
    assert testCase.strStr("", "a") == -1, "Edge 00"

    assert testCase.strStr("abcdeabcde", "de") == 3, "Example 1"
    assert testCase.strStr("abcdeabcde", "zz") == -1, "Example 2"

    print("All passed")
