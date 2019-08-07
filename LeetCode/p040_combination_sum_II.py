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


from itertools import combinations
from typing import *

class Solution:

    """
    Version A
    brutal force, max limit time exceeded
    """
    def combinationSum2(self, candidates, target):

        result = []

        # determine maximum number of element for combination
        # and skim list down by removing elements that is larger than target
        candidates = sorted(candidates)
        temp_sum, max_n, max_length = 0, 0, 0
        for i in candidates:
            temp_sum += i
            if temp_sum <= target:
                max_n += 1
            elif i > target:
                break
            max_length += 1

        candidates = candidates[:max_length]

        while max_n != 0:
            for combine in combinations(candidates, max_n):
                good = list(combine)
                if sum(combine) == target and good not in result:
                    result.append(good)
            max_n -= 1

        return result


class Solution(object):

    """
    Version B
    Same idea with Leetcode P039 Combination Sum, but cannot repeat same elements
    Add a recursive process method to update result
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        """
        Internal Helper

        Args:
            candidates:    ingredient numbers (sorted)
            start:         from 0, full candidates, to a shorter candidate list
            intermediate:  temp list to record current status List[int]]
            target:        tartget to compose

        Returns:
            None, Imperfect function, just update the result
        """
        def process(candidates: List[int], start: int, intermediate: List[int], target: int) -> None:
            if target == 0 and intermediate not in result:  # 相对于P039 加一个去重条件
                result.append(list(intermediate))  # 终止case, target降到0就完成
                # 这里使用list其实就是复制一个itermediate, 可以用interme[:]取代

            while start < len(candidates) and candidates[start] <= target:  # while loop 走完全部candidates

                intermediate.append(candidates[start])
                process(candidates, start + 1, intermediate, target - candidates[start])
                # 这里与p039不同,需要跳过, 因为不得重复使用同一个元素
                intermediate.pop()
                start += 1

        result = []
        candidates = sorted(candidates)
        process(candidates, 0, [], target)

        return result


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    assert Solution().combinationSum2(candidates, 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], "Example 1"

    candidates = [2, 5, 2, 1, 2]
    assert Solution().combinationSum2(candidates, 5) == [[1, 2, 2], [5]], "Example 2"

    print("all passed")
