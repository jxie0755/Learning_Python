"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
P003 Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brutal Force Time O(N)
        Interate substrate in the level of 26 character length only (because max length is 26)

        Cannot Save time by check fixed length of 26 character, but iterate each sub from length = 1 to the max length of 26*2 + 1(space) = 53
        """
        ans = 0
        for i in range(0, len(s)):
            sub = s[i:i+53]
            for j in range(1, len(sub)+1):
                subsub = sub[0:j]
                if len(subsub) == len(set(subsub)):
                    if ans < j:
                        ans = j
                else:
                    break
        return ans


if __name__ == "__main__":
    testCase = Solution()
    assert testCase.lengthOfLongestSubstring("") == 0, "Edge 1"
    assert testCase.lengthOfLongestSubstring(" ") == 1, "Edge 2"
    assert testCase.lengthOfLongestSubstring("au") == 2, "Edge 3"
    assert testCase.lengthOfLongestSubstring("aab") == 2, "Edge 4"
    assert testCase.lengthOfLongestSubstring("dvdf") == 3, "Edge 5"

    assert testCase.lengthOfLongestSubstring("abcabcbb") == 3, "Example 1, abc"
    assert testCase.lengthOfLongestSubstring("bbbbb") == 1, "Example 2, b"
    assert testCase.lengthOfLongestSubstring("pwwkew") == 3, "Example 3, wke"
    assert testCase.lengthOfLongestSubstring("tmmzuxt") == 5, "Example 4, mzuxt"
    print("all passed")
