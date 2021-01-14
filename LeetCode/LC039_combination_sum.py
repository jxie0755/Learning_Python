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


class Solution_A:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Brutal Force O(N^2), very slow but passed
        Basically trying out every combination from 1 to target
        """

        def process(temp: List[List[int]]) -> List[List[int]]:
            """Helper"""
            new_temp = []
            i = 0
            while i < len(temp):
                if sum(temp[i]) == target:
                    result.append(temp[i])
                for j in candidates:
                    if sum(temp[i]) + j < target:
                        new_temp.append(temp[i] + [j])
                    elif sum(temp[i]) + j == target:
                        ans = sorted(temp[i] + [j])
                        if ans not in result:
                            result.append(ans)
                i += 1
            return new_temp


        if not candidates:
            return []

        temp = [[i] for i in candidates]
        result = []

        while temp:
            temp = process(temp)

        return result


class Solution_B:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        This will pass but very slowly
        An optimized A, and without sub processing methods
        """
        result = []
        available = [[[], 0] for _ in
                     range(len(candidates))]  # must remember which idx this combination is at to save repeatition

        while available:
            new_available = []

            for pair in available:
                comb = pair[0]
                idx = pair[1]

                for i in range(idx, len(candidates)):
                    cur = comb[:] + [candidates[i]]  # i.e.: [2,3] will start adding at 3 instead of 2

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


class Solution_STD:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Add a recursive process method to update result
        The best method, super fast
        """

        def process(candidates: List[int], start: int, intermediate: List[int], target: int) -> None:
            """
            Helper
            """

            if target == 0:
                result.append(list(intermediate))  # 终止case, target降到0就完成
                # 这里使用list其实就是复制一个itermediate, 可以用interme[:]取代

            while start < len(candidates) and candidates[start] <= target:  # while loop 走完全部candidates
                intermediate.append(candidates[start])
                process(candidates, start, intermediate, target - candidates[start]) # 这里很重要
                intermediate.pop()  # 这里退回相当于,即使满足条件, 也可以跳过
                start += 1

        result = []
        candidates = sorted(candidates)  # this must be sorted first, needed for algorithm
        process(candidates, 0, [], target)

        return result



class Solution_D:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Version D
        本质上这是一道考排列组合的题,如果能构建排列组合的话, 直接对每个组合考虑是否之和等于target就可以了
        (可以通过python自带组合函数同样可以实现,也可以通过自建一个Combinations_with_replacements)

        但是必须要额外一些优化才能pass,并且速度一般
        """
        if not candidates:
            return []
        max_n = target // min(candidates) # 这里是一个重要的优化步骤,通过限定一个组合中的最大length来帮助显著减少组合数
        result = []
        for i in range(1, max_n+1):
            for comb in self.combinationWR(candidates, i):
                if sum(comb) == target:
                    result.append(comb)
        return result  # must sort at the end to pass case


    def combinationWR(self, candidates: List[int], pick: int) -> List[List[int]]:
        """
        self verison of combination algorithm, with repeating
        almost the same as itertools.combinations_with_replacement
        """
        if pick == 0:
            return []

        p = 1
        ans = [[i] for i in candidates]

        while p < pick:
            new_ans = []
            for comb in ans:
                for i in candidates:
                    if i >= max(comb):  # a very critical step to remove repeating (and will sort each combinations)
                        new = comb + [i]
                        new_ans.append(new)
            ans = new_ans
            p += 1
        return ans


if __name__ == "__main__":
    testCase = Solution_D()

    # Test cases are check after sorting, to avoid sequence error
    assert sorted(testCase.combinationSum([], 1)) == [], "Edge 0"
    assert sorted(testCase.combinationSum([1], 1)) == [[1]], "Edge 1"
    assert sorted(testCase.combinationSum([1], 2)) == [[1, 1]], "Edge 2"
    assert sorted(testCase.combinationSum([2], 1)) == [], "Edge 3"
    assert sorted(testCase.combinationSum([2], 5)) == [], "Edge 4"

    assert sorted([sorted(comb) for comb in testCase.combinationSum([2, 3, 6, 7], 7)]) == [
        [2, 2, 3],
        [7]
    ], "Example 1"

    assert sorted([sorted(comb) for comb in testCase.combinationSum([2, 3, 5], 8)]) == [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ], "Example 2"

    assert sorted([sorted(comb) for comb in testCase.combinationSum([2, 4], 10)]) == [
        [2, 2, 2, 2, 2],
        [2, 2, 2, 4],
        [2, 4, 4]
    ], "Extra 1"

    assert sorted([sorted(comb) for comb in testCase.combinationSum([7, 3, 2], 18)]) == [
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 3, 3],
        [2, 2, 2, 2, 3, 7],
        [2, 2, 2, 3, 3, 3, 3],
        [2, 2, 7, 7],
        [2, 3, 3, 3, 7],
        [3, 3, 3, 3, 3, 3]
    ], "Extra 2"

    print("All passed")
