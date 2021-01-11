"""
https://leetcode.com/problems/longest-common-prefix/
p014 Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.
"""

from typing import *
from collections import deque


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

class Solution_A2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Simple comparison from beginning"""

        result = ""
        if len(strs) == 0:
            return result

        for i in range(len(min(strs, key=len))):
            temp = strs[0][i]
            for j in range(1, len(strs)):
                check = strs[j][i]
                if check != temp:
                    break
            else:
                result += temp
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
    testCase = Solution_A2()
    lst = ["Denis Xie", "Dennis X", "Dendi Den", "Denn"]
    assert testCase.longestCommonPrefix(lst) == "Den", "regular test"

    lst2 = []
    assert testCase.longestCommonPrefix(lst2) == "", "empty list"

    print("All passed")
