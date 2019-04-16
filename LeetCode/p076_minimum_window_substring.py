# P076 Minimum Window Substring
# Hard


# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

class Solution:
    def substring_SL(self, iterable):
        result = []
        for lenth in range(1, len(iterable) + 1):
            for i in range(len(iterable) - lenth + 1):
                result.append(iterable[i:i + lenth])
        return result


    ### Brutal force
    ### maximum time limit exceeded
    def minWindow(self, s: str, t: str) -> str:
        subs = self.substring_SL(s)
        t_L = len(t)
        t_set = set(t)
        hmp = {i:t.count(i) for i in t_set}

        def isinclude(str):
            for i in t_set:
                if str.count(i) < hmp[i]:
                    return False
            return True

        for sub in subs:
            if len(sub) >= t_L:
                if isinclude(sub):
                    return sub
        return ''


    # def minWindow(self, s: str, t: str) -> str:
    #     t_set = set(t)
    #     hmp = {i:[] for i in t_set}
    #     i, L = 0, len(s)
    #     while i != L:
    #         cur = s[i]
    #         if cur in t_set:
    #             hmp[cur].append(i)
    #         i += 1
    #
    #     print(hmp)




print(Solution().minWindow("ADOBECODEBANC", "ABC"))


if __name__ == '__main__':
    assert Solution().minWindow("ABCDE", "Z") == '', "Edge 1"
    assert Solution().minWindow("A", "A") == 'A', "Edge 2"
    assert Solution().minWindow("a", "aa") == '', "Edge 3"
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == 'BANC', "Example 1"
    print('all passed')


