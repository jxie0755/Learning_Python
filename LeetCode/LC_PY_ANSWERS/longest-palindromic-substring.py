# Time:  O(n)
# Space: O(n)

# Detail explanation on Manacher Algorithm:
# https://www.youtube.com/watch?v=V-sEwsca1ak
# They key is to use the symmetry of palindrome to predict next center and (expand from a new length, if partially covered)

#                       1  1 1 1 1 1 1 1
#  0 1 2 3 4 5 6 7 8 9  0  1 2 3 4 5 6 7
#  a b a x a b a x a b  y  b a x a b y b
#  1 3 1 7 1 0 1 5 1 1 11  1 1 5 9


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = '#' + '#'.join(s) + '#'

        n = len(t)
        RL = [0] * n
        ans = ""
        maxLen = 0
        maxRight = 0
        pos = 0
        for i in range(n):
            RL[i] = min(maxRight - i, RL[pos*2-i]) if i < maxRight else 1
            while i >= RL[i] and i+RL[i] < len(t) and t[i+RL[i]] == t[i-RL[i]]:
                RL[i] += 1
            if i + RL[i]-1 > maxRight:
                maxRight = i + RL[i] - 1
                pos = i
            if RL[i] > maxLen:
                maxLen = RL[i]
                ans = s[(i + 1 - maxLen)//2: (i - 1 + maxLen)//2]
        return ans
