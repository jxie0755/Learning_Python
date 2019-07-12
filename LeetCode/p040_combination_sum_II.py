# P040 Combination Sum II
# Medium


# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.


# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

from itertools import combinations

class Solution:
    # brutal force, max limit time exceeded
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



# TODO 研究答案



if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    assert Solution().combinationSum2(candidates, target) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]


    candidates = [2, 5, 2, 1, 2]
    target = 5
    assert Solution().combinationSum2(candidates, target) == [[1, 2, 2], [5]]

    print("all passed")
