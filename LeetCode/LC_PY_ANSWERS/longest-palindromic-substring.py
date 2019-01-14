# Time:  O(n)
# Space: O(n)

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


print(Solution().longestPalindrome('cbbd'))