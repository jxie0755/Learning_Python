# P003 Longest Substring Without Repeating Characters
# Medium

# Given a string, find the length of the longest substring without repeating characters.

from typing import *

class Solution:

    # Version A, Brutal Force Time O(N^3)
    # Get all substrings from long to short, then check each on repeating characters
    # Fail as Maximum Time limit exceeded
    def lengthOfLongestSubstring(self, s: str) -> int:

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

    # Versiom B1, Time O(N^2), Space O(N)
    # Find repeating element and start again after the first repeating element
    # This wil pass, but may reach maximum recursion depth in long cases
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        else:
            hashtable = {}
            i = 0
            while i != len(s):
                if s[i] in hashtable:  # if repeat, then recursive compare to the next section, starting after the first repeating element.
                    new_start = hashtable[s[i]]+1
                    return max(i, self.lengthOfLongestSubstring(s[new_start:]))
                hashtable[s[i]] = i
                i += 1
            else:   # if no repeat, go to the end and return the full length
                return len(s)


# Idea is like:
# abcdefghXijklmXoMqrstMuvwxyz
# abcdefghXijklmX.....            Find X occured twice, then stop and recalculate after the first X
#          ijklmXoMqrstM...       Find M occured twice, then stop and recalculate after the first M
#                  qrstMuvwxyz    until it ends, and compare each secion


class Solution:

    # Version B2, Time O(N^2), Space O(N)
    # Non-recursive way to previous method
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = []

        if not s:
            return 0
        else:
            i, label = 0, 0
            hashtable = {}
            while i != len(s):
                current = s[i]
                if current not in hashtable:
                    hashtable[current] = i
                    i += 1
                    if i == len(s):  # Define an end case as no repeating found at the last element
                        result.append(i-label)
                else:
                    result.append(i-label)
                    i = hashtable[current] + 1
                    label = i
                    hashtable = {}

            return max(result)




class Solution(object):
    # STD ans
    # Time O(N), Space O(1)
    # 借字符表运算
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest


if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring("") == 0, 'Edge 1'
    assert Solution().lengthOfLongestSubstring(" ") == 1, 'Edge 2'
    assert Solution().lengthOfLongestSubstring("au") == 2, 'Edge 3'
    assert Solution().lengthOfLongestSubstring("aab") == 2, 'Edge 4'
    assert Solution().lengthOfLongestSubstring("dvdf") == 3, 'Edge 5'

    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3, 'Example 1, "abc"'
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1, 'Example 2, "b"'
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3, 'Example 3, "wke"'
    assert Solution().lengthOfLongestSubstring("tmmzuxt") == 5, 'Example 4, mzuxt'
    print('all passed')
