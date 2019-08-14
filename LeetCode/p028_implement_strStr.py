"""
https://leetcode.com/problems/implement-strstr/
p028 implement strStr()
Easy

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        """Version A"""

        length = len(needle)
        index = 0
        while index <= len(haystack) - length:
            if haystack[index:index + length] == needle:
                return index
            index += 1
        return -1


if __name__ == "__main__":
    assert Solution().strStr("", "a") == -1, "Edge 0"
    assert Solution().strStr("", "") == 0, "Edge 1"

    assert Solution().strStr("abcdeabcde", "de") == 3, "Example 1"
    assert Solution().strStr("abcdeabcde", "zz") == -1, "Example 2"

    print("all passed")
