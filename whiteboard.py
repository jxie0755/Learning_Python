"""
https://leetcode.com/problems/permutation-sequence/
P060 Permutation Sequence
Medium

The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
"""

import math
from typing import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        pass





if __name__ == "__main__":
    testCase = Solution()
    assert testCase.getPermutation(4, 1) == "1234", "Edge 1"
    assert testCase.getPermutation(3, 3) == "213", "Example 1"
    assert testCase.getPermutation(4, 9) == "2314", "Example 2"
    assert testCase.getPermutation(8, 29805) == "68327415", "Long 1"
    assert testCase.getPermutation(9, 62716) == "265183794", "Long 2"
    print("all passed")

    # print("test timeit")
    # print(timeit.repeat("testCase.getPermutation_0(8, 6000)", setup="from __main__ import Solution", repeat=3, number=500))
    # >>> [3.045518253785702, 3.04060806065978, 3.0435408311783467]
    # print(timeit.repeat("testCase.getPermutation(8, 6000)", setup="from __main__ import Solution", repeat=3, number=500))
    # >>> [0.48771537433245093, 0.48776606102485154, 0.48719471292885963]
    # 当k刚好略大于上一级n的时候, 会快很多, 但是其他情况下这样只能略微提速
    # print("timeit ended")
