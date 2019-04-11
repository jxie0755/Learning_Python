# P047 Permutations II
# Medium



# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
from typing import *
import math

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


    def permuteUnique(self, nums):
        ### First handle index, then convert to nuns[index], if not repeating then append.
        ### This will pass but way too slow
        ### revised to use set(tuples) to removed repeats, it is faster, but still slow
        total_n = math.factorial(len(nums))
        result = []
        idxs = list(range(len(nums)))[::-1]
        for i in range(total_n):
            idxs = self.next_permute(idxs)
            result.append(tuple([nums[i] for i in idxs]))
        return [list(i) for i in set(result)]


class Solution:
    ### recursive method from leetcode P046
    ### revised the recursion rule by bypassing the repeated next_list
    def restList(self, elm, lst):
        """return a list with target element removed"""
        nextList = lst[:]
        nextList.remove(elm)
        return nextList

    def permuteUnique(self, nums: List[int]):
        length = len(nums)
        result = []

        def helper(lst, permute_list=[]):
            if len(permute_list) == length:
                result.append(permute_list)
            else:
                next_list_list = []
                for i in lst:
                    next_list = self.restList(i, lst)
                    if next_list not in next_list_list:   # 在这里去重, 只要剩下的list完全相同就不要递归了
                        next_list_list.append(next_list)
                        updated_permute_list = permute_list + [i]
                        helper(next_list, updated_permute_list)

        helper(nums)
        return result

class Solution:
    ### recursive method, single and pure recursion from leetcode P046
    ### revised the recursion rule by bypassing the repeated next_list
    def permuteUnique(self, nums: List[int]):
        length = len(nums)
        if length == 1:
            return [[nums[0]]]
        else:
            result = []
            sublist_list = []
            for i in nums:
                subist = nums[:]
                subist.remove(i)
                if subist not in sublist_list:
                    sublist_list.append(subist)
                    result += [[i] + per for per in self.permuteUnique(subist)]
            return result



if __name__ == '__main__':
    assert Solution().permuteUnique([1]) == [
        [1]
    ], "Edge 1"


    assert Solution().permuteUnique([1,2,3]) == [
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

    print('all passed')
