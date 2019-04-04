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
    def next_permute(self, indexes):
        ### Use next permutation method from leetcode p031
        """calculate the next permuatation, with integers 0 to N-1 (for N elements)
        this will both modify idx_list and return the updated idx_list"""
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

    def permute(self, nums: List[int]):
        total_n = math.factorial(len(nums))
        result = []
        idxs = list(range(len(nums)))[::-1]
        for i in range(total_n):
            idxs = self.next_permute(idxs)
            result.append([nums[i] for i in idxs])
        return result





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



