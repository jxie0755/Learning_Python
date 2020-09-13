"""
https://leetcode.com/problems/combination-sum/
P039 Cobination Sum
Medium

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
"""

from typing import *


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        This will pass but very slowly
        """
        result = []
        available = [[[],0] for _ in range(len(candidates))]  # must remember which idx this combination is at to save repeatition


        while available:
            new_available = []

            for pair in available:
                comb = pair[0]
                idx = pair[1]

                for i in range(idx, len(candidates)):
                    cur = comb[:] + [candidates[i]]    # i.e.: [2,3] will start adding at 3 instead of 2

                    if sum(cur) < target:
                        new_available.append([cur, i])
                    elif sum(cur) == target:
                        if sorted(cur) not in result:
                            result.append(sorted(cur))
                    else:
                        pass
            available = new_available

        return result
        # Leetcode does not require sequence, but locally it is required to pass case



if __name__ == "__main__":
    testCase = Solution()

    # Test cases are check after sorting, to avoid sequence error
    assert sorted(testCase.combinationSum([], 1)) == [], "Edge 1"
    assert sorted(testCase.combinationSum([1], 1)) == [[1]], "Edge 2"
    assert sorted(testCase.combinationSum([1], 2)) == [[1, 1]], "Edge 3"
    assert sorted(testCase.combinationSum([2], 1)) == [], "Edge 4"
    assert sorted(testCase.combinationSum([2], 5)) == [], "Edge 5"

    assert sorted(testCase.combinationSum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]], "Example 1"
    assert sorted(testCase.combinationSum([2, 3, 5], 8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]], "Example 2"

    assert sorted(testCase.combinationSum([2, 4], 10)) == [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 4, 4]], "Extra 1"

    assert sorted(testCase.combinationSum([7, 3, 2], 18)) == [
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 3, 3],
        [2, 2, 2, 2, 3, 7],
        [2, 2, 2, 3, 3, 3, 3],
        [2, 2, 7, 7],
        [2, 3, 3, 3, 7],
        [3, 3, 3, 3, 3, 3]
    ], "Extra 2"


    print("all passed")
