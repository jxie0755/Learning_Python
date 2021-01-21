"""
https://leetcode.com/problems/subsets-ii/
P090 Subsets II
Medium


Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""


from typing import *

class Solution_A:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    assert sorted(testCase.subsetsWithDup([])) == [
        []
    ], "Edge 0"

    assert sorted(testCase.subsetsWithDup([1])) == [
        [],
        [1]
    ], "Edge 1"

    assert sorted(testCase.subsetsWithDup([1, 2])) == [
        [],
        [1],
        [1, 2],
        [2]
    ], "Example 1"

    assert sorted(testCase.subsetsWithDup([1, 2, 2])) == [
        [],
        [1],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2]
    ], "Example 2"

    assert sorted(testCase.subsetsWithDup([1, 2, 3])) == [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 3],
        [2],
        [2, 3],
        [3]
    ], "Additional 1"

    assert sorted(testCase.subsetsWithDup([1, 1, 2, 2])) == [
        [],
        [1],
        [1, 1],
        [1, 1, 2],
        [1, 1, 2, 2],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2]
    ], "Additional 2"

    print("All passed")
