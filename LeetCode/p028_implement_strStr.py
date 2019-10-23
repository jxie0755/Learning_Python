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
        index = 0
        while index <= len(haystack) - length:
            if haystack[index:index + length] == needle:
                return index
            index += 1
        return -1


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.strStr("", "a") == -1, "Edge 0"
    assert testCase.strStr("", "") == 0, "Edge 1"

    assert testCase.strStr("abcdeabcde", "de") == 3, "Example 1"
    assert testCase.strStr("abcdeabcde", "zz") == -1, "Example 2"

    print("all passed")
