"""
https://leetcode.com/problems/group-anagrams/
LC049 Group Anagrams
Medium

Given an array of strings, group anagrams together.

Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""

from typing import *


class Solution_A:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use hashmap to store each group under a sorted set of letters (tuple) as the key.
        """

        if not strs:
            return [[]]

        hmp = {}
        for word in strs:
            sorted_anagram_key = tuple(sorted(list(word)))
            if sorted_anagram_key not in hmp:
                hmp[sorted_anagram_key] = [word]
            else:
                hmp[sorted_anagram_key].append(word)
        return list(hmp.values())


if __name__ == "__main__":
    testCase = Solution_A()

    edge_1 = []
    assert testCase.groupAnagrams(edge_1) == [
        []
    ], "edge 0"

    edge_2 = ["a"]
    assert testCase.groupAnagrams(edge_2) == [
        ["a"]
    ], "edge 1"

    sample_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert testCase.groupAnagrams(sample_1) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"]
    ], "Example 1"

    print("All passed")
