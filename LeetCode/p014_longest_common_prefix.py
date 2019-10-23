"""
https://leetcode.com/problems/longest-common-prefix/
p014 Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.
"""

from collections import deque
from typing import *


class Solution_A:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Use set to filter repeat"""

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

class Solution_B:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Use Deque
        利用deque的maxlen特性
        """

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
    testMethod = Solution_B().longestCommonPrefix
    lst = ["Denis Xie", "Dennis X", "Dendi Den", "Denn"]
    assert testMethod(lst) == "Den", "regular test"

    lst2 = []
    assert testMethod(lst2) == "", "empty list"

    print("all passed")
