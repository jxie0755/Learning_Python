"""
https://leetcode.com/problems/permutations/
P046 Permutations
Medium

Given a collection of distinct (数字不会重复) integers, return all possible permutations.
"""

import itertools
import math
from typing import *


class Solution:

    """
    Version A
    use python's internal method, only for testing the speed
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in itertools.permutations(nums):
            result.append(list(i))
        return result


class Solution:

    """
        Version B1
        Convert to permutation of indexes, then replace with nums[idx]
        """

    def permute(self, nums: List[int]) -> List[List[int]]:

        total_n = math.factorial(len(nums))
        result = []
        perm_idxs = list(range(len(nums)))
        for i in range(total_n):
            result.append([nums[i] for i in perm_idxs])
            perm_idxs = self.next_permute(perm_idxs)
        return result

    """
    Version B2
    Recursive method, but direct handle elements in nums
    This only works for when sample is a collection of distinct numbers
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        total_n = math.factorial(len(nums))
        result = []
        for i in range(total_n):
            result.append(nums[:])
            self.next_permute(nums)
        return result

    """
    Herlper for B1, B2
    From Leetcode p032: next permutation
    calculate the next permuatation, with integers 0 to N-1 (for N elements)
    this will both modify idx_list and return the updated idx_list
    """
    def next_permute(self, indexes: List[int]) -> List[int]:

        length = len(indexes)
        cur_i = None

        for i in range(-2, -length - 1, -1):
            if indexes[i] < indexes[i + 1]:
                cur_i = i
                break

        if not cur_i:
            indexes.reverse()
            return indexes

        else:
            for rev_i in range(-1, cur_i, -1):
                if indexes[rev_i] > indexes[cur_i]:  # tail must already be sorted!
                    indexes[cur_i], indexes[rev_i] = indexes[rev_i], indexes[cur_i]  # switch
                    indexes[cur_i + 1:] = indexes[cur_i + 1:][::-1]
                    break
            return indexes


class Solution:

    """
    Version C
    Direct Recursive method, no need for next permute
    """
    def permute(self, nums: List[int]) -> List[List[int]]:

        """Helper"""
        def helper(lst: List[int], permute_list: List[int] = []) -> None:
            if len(permute_list) == length:
                result.append(permute_list)
            else:
                for i in lst:
                    next_list = lst[:]
                    next_list.remove(i) # Copy lst then remove i 1 by 1
                    updated_permute_list = permute_list + [i]
                    helper(next_list, updated_permute_list)

        length = len(nums)
        result = []
        helper(nums)
        return result


class Solution:

    """Version D, Pure recursive method"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            result = []
            for i in nums:
                subList = nums[:]
                subList.remove(i)
                result += [[i] + per for per in self.permute(subList)]
            return result


if __name__ == "__main__":
    assert Solution().permute([1]) == [
        [1]
    ], "Edge 1"

    assert Solution().permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ], "Example 1"

    print("all passed")
