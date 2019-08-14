"""
https://leetcode.com/problems/permutations-ii/
P047 Permutations II
Medium

Given a collection of numbers that might contain duplicates, return all possible unique permutations.
"""

from itertools import permutations
from math import factorial
from typing import *


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Version A
        use python's internal method, only for testing the speed
        """

        result = []
        for idxs in permutations(list(range(len(nums)))):
            next_perm = [nums[i] for i in idxs]
            if next_perm not in result:
                result.append(next_perm)
        return result


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Version B
        Use next permuteUnique
        First handle index, then convert to nuns[index], if not repeating then append.
        This will pass but way too slow
        revised to use set(tuples) to removed repeats, then sort, it is faster, but still slow
        """

        total_n = factorial(len(nums))
        result = []
        idxs = list(range(len(nums)))
        for i in range(total_n):
            next_perm = [nums[i] for i in idxs]
            result.append(tuple(next_perm))
            idxs = self.next_permute(idxs)
        return sorted([list(i) for i in set(result)])


    # You must not use Leetcode P046 Version B2, because it asks for distinct collection of numbers

    def next_permute(self, indexes: List[int]) -> List[int]:
        """
        Helper B
        Use next permutation method from leetcode p031
        calculate the next permuatation, with integers 0 to N-1 (for N elements)
        this will both modify idx_list and return the updated idx_list
        """

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

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Version C
        recursive method from leetcode P046
        revised the recursion rule by bypassing the repeated next_list
        """

        def permuteUniHelper(lst: List[int], permute_list: List[int] =[]) -> None:
            """Helper"""

            if len(permute_list) == length:
                result.append(permute_list)
            else:
                next_list_list = []
                for i in lst:
                    next_list = lst[:]
                    next_list.remove(i)
                    if next_list not in next_list_list:  # 在这里去重, 只要剩下的list完全相同就不要递归了
                        next_list_list.append(next_list)
                        updated_permute_list = permute_list + [i]
                        permuteUniHelper(next_list, updated_permute_list)

        length = len(nums)
        result = []
        permuteUniHelper(nums)
        return result


class Solution:

    def permuteUnique(self, nums: List[int]):
        """
        Version D
        Pure recursive method, single and pure recursion from leetcode P046
        Revised the recursion rule by bypassing the repeated next_list
        """

        length = len(nums)
        if length == 1:
            return [[nums[0]]]
        else:
            result = []
            sublist_checklist = []  # add an intermediate step to prevent repeats
            for i in nums:
                subist = nums[:]
                subist.remove(i)
                if subist not in sublist_checklist:  # check repeats
                    sublist_checklist.append(subist)
                    result += [[i] + per for per in self.permuteUnique(subist)]
            return result



if __name__ == "__main__":
    assert Solution().permuteUnique([1]) == [
        [1]
    ], "Edge 1"

    assert Solution().permuteUnique([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ], "Example 1"

    assert Solution().permuteUnique([1, 1, 2]) == [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ], "Example 2"

    print("all passed")
