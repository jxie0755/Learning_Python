# P003 Longest Substring Without Repeating Characters
# Medium


# Given a string, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s):
        ### Brutal Force Time O(N^3)
        ### Get all substrings from long to short, then check each on repeating characters
        ### Fail as Maximum Time limit exceeded
        """
        :type s: str
        :rtype: int
        """
        def is_no_repeat(s):
            hastable = {}
            for i in s:
                if i not in hastable:
                    hastable[i] = 1
                else:
                    return False
            return True

        if not s:
            return 0

        for j in range(len(s), 0, -1):
            for i in range(0, len(s)-j+1):
                sample = s[i:i+j]
                if is_no_repeat(sample):
                    return len(sample)


class Solution:
    def lengthOfLongestSubstring(self, s):
        ### Brutal Force Time O(N^3)
        ### Get all substrings from long to short, then check each on repeating characters
        ### Fail as Maximum Time limit exceeded
        """
        :type s: str
        :rtype: int
        """
        def is_no_repeat(s):
            hastable = {}
            for i in s:
                if i not in hastable:
                    hastable[i] = 1
                else:
                    return False
            return True




assert Solution().lengthOfLongestSubstring("") == 0, 'Edge 1'
assert Solution().lengthOfLongestSubstring("abcabcbb") == 3, 'Example 1, "abc"'
assert Solution().lengthOfLongestSubstring("bbbbb") == 1, 'Example 1, "b"'
assert Solution().lengthOfLongestSubstring("pwwkew") == 3, 'Example 1, "wke"'
print('all passed')
