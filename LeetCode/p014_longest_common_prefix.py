# https://leetcode.com/problems/longest-common-prefix/
# p014 Longest Common Prefix
# Easy

from collections import deque  # 利用deque的maxlen特性
# Write a function to find the longest common prefix string amongst an array of strings.
from typing import *


class Solution:

    # Version A, Use set
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result

        for i in range(len(min(strs, key=len))):
            temp = []
            for j in range(len(strs)):
                temp.append(strs[j][i])
            if len(set(temp)) == 1:
                result += temp[0]
            else:
                break
        return result

    # Version B, Use Deque
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result
        for i in range(len(min(strs, key=len))):
            temp = list(map(lambda x: deque(x[i], 1), strs))
            if temp.count(temp[0]) == len(temp):
                result += temp[0][0]
            else:
                break
        return result


if __name__ == "__main__":
    lst = ["Denis Xie", "Dennis X", "Dendi Den", "Denn"]
    assert Solution().longestCommonPrefix(lst) == "Den", "regular test"

    lst2 = []
    assert Solution().longestCommonPrefix(lst2) == "", "empty list"

    print("all passed")
