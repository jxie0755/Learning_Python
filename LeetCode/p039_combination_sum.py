# P039 Cobination Sum
# Medium


# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.



class Solution:
    def combinationSum(self, candidates, target):
        ### Brutal Force O(N^2), very slow but passed
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        def process(temp):
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

        candidates = sorted(candidates)
        temp = [[i] for i in candidates]
        result = []

        while temp:
            temp = process(temp)

        return result


class Solution(object):
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):

        # Add a recursive process method to update result
        def process(candidates, start, intermediate, target):
            """
            Args:
                candidates:    ingredient numbers (sorted)
                start:         from 0, full candidates, to a shorter candidate list
                intermediate:  temp list to record current status
                target:        tartget to compose

            Returns: None, Imperfect function, just update the result
            """
            if target == 0:
                result.append(list(intermediate))  # 终止case, target降到0就完成

            while start < len(candidates) and candidates[start] <= target: # while loop 走完全部candidates
                intermediate.append(candidates[start])
                process(candidates, start, intermediate, target - candidates[start])
                intermediate.pop()
                start += 1

        result = []
        candidates = sorted(candidates)
        process(candidates, 0, [], target)

        return result


# 本质上这是一道考排列组合的题,如果能构建排列组合的话, 直接对每个组合考虑是否之和等于target就可以了
# 上解就是通过自己构建组合,并融合target条件所以直接得出答案.
# 这里利用python自带组合函数同样可以实现

from itertools import combinations_with_replacement

class Solution(object):
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        max_n = target // min(candidates)
        result = []
        for i in range(max_n, 0, -1):
            all_comb = combinations_with_replacement(candidates, i)
            for j in all_comb:
                if sum(j) == target:
                    result.append(list(j))
        return result


if __name__ == '__main__':
    assert Solution().combinationSum([], 1) == [], 'Edge 1'
    assert Solution().combinationSum([1], 1) == [[1]], 'Edge 2'
    assert Solution().combinationSum([1], 2) == [[1,1]], 'Edge 3'
    assert Solution().combinationSum([2], 1) == [], 'Edge 4'
    assert Solution().combinationSum([2], 5) == [], 'Edge 5'

    assert Solution().combinationSum([2,3,6,7], 7) == [[2, 2, 3], [7]], 'Example 1'
    assert Solution().combinationSum([2,3,5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]], 'Example 2'

    assert Solution().combinationSum([2,4], 10) == [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 4, 4]], 'Extra 1'

    print('all passed')
