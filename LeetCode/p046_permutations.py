# P046 Permutations
# Medium


# Given a collection of distinct (数字不会重复) integers, return all possible permutations.

from typing import *

import math

import itertools

class Solution:
    def permute(self, nums: List[int]):
        result = []
        for i in itertools.permutations(nums):
            result.append(list(i))
        return result

class Solution:
    def next_permute(self, idx_list):
        ### Use next permutation method from leetcode p031
        """calculate the next permuatation, with integers 0 to N-1 (for N elements)
        this will both modify idx_list and return the updated idx_list"""
        length = len(idx_list)
        cur_i = None

        for i in range(-2, -length - 1, -1):
            if idx_list[i] < idx_list[i + 1]:
                cur_i = i
                break

        if not cur_i:
            idx_list.reverse()
            return idx_list

        else:
            for rev_i in range(-1, cur_i, -1):
                if idx_list[rev_i] > idx_list[cur_i]:  # tail must already be sorted!
                    idx_list[cur_i], idx_list[rev_i] = idx_list[rev_i], idx_list[cur_i]  # switch
                    idx_list[cur_i + 1:] = idx_list[cur_i + 1:][::-1]
                    break
            return idx_list

    def permute(self, nums: List[int]):
        total_n = math.factorial(len(nums))
        result = []
        idxs = list(range(len(nums)))[::-1]
        for i in range(total_n):
            idxs = self.next_permute(idxs)
            result.append([nums[i] for i in idxs])
        return result



print(Solution().permute([1]))



if __name__ == '__main__':
    assert Solution().permute([1]) == [
        [1]
    ], "Edge 1"


    assert Solution().permute([1,2,3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ], "Example 1"

    print('all passed')



