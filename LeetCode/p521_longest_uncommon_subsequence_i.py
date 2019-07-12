# p521 Longest Uncommon Subsequence I
# Easy

# Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings.
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings
# and this subsequence should not be any subsequence of the other strings
#
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements.
# Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
#
# The input will be two strings, and the output needs to be the length of the longest uncommon subsequence.
# If the longest uncommon subsequence doesn't exist, return -1.
# Note:
# Both strings' lengths will not exceed 100.
# Only letters from a ~ z will appear in input strings.


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


# This question is "misleading"
# if a == b, then all subsequence will be the same, so -1
# However, the longest subsequence is the string itself
# so if a != b, then the longest uncommon subsequence will be the string that has the longer length

if __name__ == "__main__":
    assert Solution().findLUSlength("abc", "abc") == -1, "two identical string"
    assert Solution().findLUSlength("aba", "cdc") == 3, "same length but different"
    assert Solution().findLUSlength("abcd", "abc") == 4, "a longer than b"
    assert Solution().findLUSlength("abc", "abcd") == 4, "b longer than a"
    print("all passed")
