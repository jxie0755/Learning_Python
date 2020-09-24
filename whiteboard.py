"""
https://leetcode.com/problems/combination-sum-ii/
P040 Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
    All numbers (including target) will be positive integers.
    The difference between the P039 and P040 is that the candidates can be duplicated in P040 but not in P039
    The solution set must not contain duplicate combinations.
"""

from typing import *


class Solution_C:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        本质上这是一道考排列组合的题,如果能构建排列组合的话, 直接对每个组合考虑是否之和等于target就可以了
        (可以通过python自带组合函数同样可以实现,也可以通过自建一个Combinations_with_replacements)

        但是必须要额外一些优化才能pass,并且速度一般
        """
        if not candidates:
            return []

        result = []
        for i in range(1, len(candidates) + 1):
            for comb in self.combinations(candidates, i):
                sorted_comb = sorted(comb)  # 确保排序,以防重复组出现(原combinations不需要)
                if sum(sorted_comb) == target and sorted_comb not in result:
                    result.append(sorted_comb)
        return result  # must sort at the end to pass case

    def combinations(self, candidates: List, r: int) -> List[List]:
        """
        Self verison of combination algorithm, with no repeating
        None-proxy, directly forming, Recursive
        Similar to itertools.combinations_with_replacement(iterable, r)
        """

        n = len(candidates)

        if r == 0:
            return [[]]
        elif r == n:
            return [candidates]
        elif r == 1:
            return [[i] for i in candidates]
        else:
            sub_candidates = candidates[:]
            popped = sub_candidates.pop()
            return [com + [popped] for com in self.combinations(sub_candidates, r - 1)] + self.combinations(sub_candidates, r)


if __name__ == "__main__":
    testCase = Solution-C()

    q1 = [10, 1, 2, 7, 6, 1, 5]
    assert sorted([sorted(comb) for comb in testCase.combinationSum2(q1, 8)]) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ], "Example 1"

    q2 = [2, 5, 2, 1, 2]
    assert sorted([sorted(comb) for comb in testCase.combinationSum2(q2, 5)]) == [
        [1, 2, 2],
        [5]
    ], "Example 2"

    print("all passed")

