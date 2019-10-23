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
    testMethod = Solution_A().strStr
    assert testMethod("", "a") == -1, "Edge 0"
    assert testMethod("", "") == 0, "Edge 1"

    assert testMethod("abcdeabcde", "de") == 3, "Example 1"
    assert testMethod("abcdeabcde", "zz") == -1, "Example 2"

    print("all passed")
