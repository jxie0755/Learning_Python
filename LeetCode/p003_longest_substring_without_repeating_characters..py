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


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         ### Time O(N), Space O(N)
#         ### if a string shows repeat, then all substring that include this string will have repeat.
#         ### Use hashtable to track length of non-repeating substrings
#         ### This will fail because not able to track non-consecutive repeats !!!!
#         """
#         :type s: str
#         :rtype: int
#         """
#         found = False
#         hashtable = {}
#         i, cur_len = 0, 0
#         while i != len(s):
#             sample = s[i]
#             if sample not in hashtable:
#                 found = False
#                 hashtable[sample] = 1
#             else:
#                 found = True
#                 new_len = len(hashtable)
#                 cur_len = new_len if new_len > cur_len else cur_len
#                 hashtable = {sample: 1}
#             i += 1
#
#         return cur_len if found else len(hashtable)


class Solution:
    def lengthOfLongestSubstring(self, s):
        ### Time O(N^2), Space O(N)
        ### Use the center expansion, recursive
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            return 2 if s[0] != s[1] else 1
        else:
            length = len(s)
            mid = len(s) // 2
            hashtable = {s[mid]: 1}






Solution().lengthOfLongestSubstring("aab")
#
# assert Solution().lengthOfLongestSubstring("") == 0, 'Edge 1'
# assert Solution().lengthOfLongestSubstring(" ") == 1, 'Edge 2'
# assert Solution().lengthOfLongestSubstring("au") == 2, 'Edge 3'
# assert Solution().lengthOfLongestSubstring("aab") == 2, 'Edge 4'
# assert Solution().lengthOfLongestSubstring("dvdf") == 3, 'Edge 5'
#
# assert Solution().lengthOfLongestSubstring("abcabcbb") == 3, 'Example 1, "abc"'
# assert Solution().lengthOfLongestSubstring("bbbbb") == 1, 'Example 1, "b"'
# assert Solution().lengthOfLongestSubstring("pwwkew") == 3, 'Example 1, "wke"'
# print('all passed')
