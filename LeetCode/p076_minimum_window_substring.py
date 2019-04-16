# P076 Minimum Window Substring
# Hard


# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass


if __name__ == '__main__':
    assert Solution().minWindow("ABCDE", "Z") == '', "Edge 1"
    assert Solution().minWindow("A", "A") == 'A', "Edge 2"
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == 'BANC', "Example 1"
    print('all passed')


