# p459 Repeated Substring Pattern
# Easy

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
# You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

# """
# :type s: str
# :rtype: bool
# """

class Solution:
    def repeatedSubstringPattern(self, s):
        # O(n), n as len(s)
        for i in range(1, len(s) // 2 + 1):
            if s[0:i] * (len(s) // i) == s:
                return True
        return False


if __name__ == "__main__":
    assert Solution().repeatedSubstringPattern("abab") == True
    assert Solution().repeatedSubstringPattern("abcabc") == True
    assert Solution().repeatedSubstringPattern("ababa") == False
    assert Solution().repeatedSubstringPattern("aaabbb") == False
    assert Solution().repeatedSubstringPattern("a") == False
    assert Solution().repeatedSubstringPattern("aa") == True
    assert Solution().repeatedSubstringPattern("aaa") == True
    print("all passed")
