"""
https://leetcode.com/problems/permutations-ii/
P047 Permutations II
Medium

Given a collection of numbers that might contain duplicates, return all possible unique permutations.
"""

from itertools import permutations
from math import factorial
from typing import *


class Solution_A1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        use python's internal method, only for testing the speed
        Only permute the idx (non-repeating), as a proxy method, but check repeat after put back to elements
        It is not necessary to use proxy
        """
        result = []
        for idxs in permutations(list(range(len(nums)))):
            next_perm = [nums[i] for i in idxs]
            if next_perm not in result:
                result.append(next_perm)
        return result


class Solution_A2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        use python's internal method, only for testing the speed
        Non-proxy version of A1
        """
        result = []
        for p in permutations(nums):
            lp = list(p)
            if lp not in result:
                result.append(lp)
        return result


class Solution_B:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Use next nextPermutation from LC031, but use proxy to avoid repeating causing comparison error
        First handle index, then convert to nuns[index], if not repeating then append.

        This will pass but way too slow
        revised to use set(tuples) to removed repeats, then sort, it is faster, but still slow
        """
        total_n = factorial(len(nums))
        result = []
        idxs = list(range(len(nums)))

        for _ in range(total_n):
            each_perm = [nums[i] for i in idxs]
            if each_perm not in result:
                result.append(each_perm)
            self.nextPermutation(idxs)

        return result

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Helper function from LC031
        """

        if not nums:
            return None

        # 从后往前找到第一次出现下降趋势那个元素
        first_idx = len(nums) - 2
        second_idx = len(nums) - 1

        # 先定位first_idx
        while first_idx >= 0 and nums[first_idx] >= nums[first_idx + 1]:
            first_idx -= 1

        if first_idx == -1:  # 如果完美倒序上升,则已经逆序排好,直接反转即可
            nums[:] = nums[:][::-1]  # nums.reverse()
        else:
            # 定位second_idx
            # 由于尾部已经是逆序排好, 所以从尾部开始倒退,第一个>first_element的元素就是second_element
            while nums[second_idx] <= nums[first_idx]:
                second_idx -= 1

            # complete the swap
            nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]
            # reverse element after first_idx
            nums[first_idx + 1:] = nums[first_idx + 1:][::-1]



class Solution_C1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        recursive method modified from leetcode P046 Version C
        revised the recursion rule by bypassing the repeated next_list
        """

        def permuteUniHelper(lst: List[int], permute_list: List[int] = []) -> None:
            """Helper from LC046 Version C"""

            if len(lst) == 0:  # all elements got picked
                result.append(permute_list)
            else:
                sub_list_check = []  # create a next_list_list
                for i in range(len(lst)):
                    sub_list = lst[:]  # it will be the sub-list after the pop
                    picked = sub_list.pop(i)

                    # must check on sorted to avoid same sub_list in different sequence!
                    sub_list_sorted = sorted(sub_list)

                    # Modification: Recursively removing repeating sub_list through each pick
                    if sub_list_sorted not in sub_list_check:
                        sub_list_check.append(sub_list_sorted)
                        updated_permute_list = permute_list + [picked]
                        permuteUniHelper(sub_list, updated_permute_list)

        result = []
        permuteUniHelper(nums)
        return result


class Solution_C2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Version C1 modified
        Sort nums first to avoid sort sub_list check for repeating

        So far, this is the best solution
        """

        def permuteUniHelper(lst: List[int], permute_list: List[int] = []) -> None:
            """Helper from LC046 Version C"""

            if len(lst) == 0:
                result.append(permute_list)
            else:
                sub_list_check = []  # create a next_list_list
                for i in range(len(lst)):
                    sub_list = lst[:]  # it will be the sub-list after the pop
                    picked = sub_list.pop(i)

                    if sub_list not in sub_list_check:
                        sub_list_check.append(sub_list)
                        updated_permute_list = permute_list + [picked]
                        permuteUniHelper(sub_list, updated_permute_list)

        nums = sorted(nums)  # sort first to avoid repeating issue
        result = []
        permuteUniHelper(nums)
        return result



class Solution_D:
    def permuteUnique(self, nums: List[int]):
        """
        Pure recursive method, single and pure recursion modified from leetcode P046 version D
        Revised the recursion rule by bypassing the repeated next_list

        Must sort sub_list for checking repeat, unlike version C
        The sort nums can not be separated from main function, like the way version C uses helper
        """

        length = len(nums)
        if length == 1:
            return [nums]
        else:
            result = []
            sub_list_check = []  # add an intermediate step to prevent repeats
            for i in range(len(nums)):
                sub_list = nums[:]
                picked = sub_list.pop(i)

                # must check on sorted to avoid same sub_list in different sequence!
                sub_list_sorted = sorted(sub_list)

                # Recursively removing repeating sub_list through each pick
                if sub_list_sorted not in sub_list_check:
                    sub_list_check.append(sub_list_sorted)
                    result += [[picked] + per for per in self.permuteUnique(sub_list)]
            return result



if __name__ == "__main__":
    testCase = Solution_C2()
    assert testCase.permuteUnique([1]) == [
        [1]
    ], "Edge 1"

    assert sorted(testCase.permuteUnique([1, 2, 3])) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ], "Example 1"

    assert sorted(testCase.permuteUnique([3, 2, 1])) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ], "Example 1 addtional"

    assert sorted(testCase.permuteUnique([1, 1, 2])) == [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ], "Example 2"

    assert sorted(testCase.permuteUnique([2, 1, 1])) == [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ], "Example 2 additional"


    assert sorted(testCase.permuteUnique([3, 3, 0, 3])) == [
        [0, 3, 3, 3],
        [3, 0, 3, 3],
        [3, 3, 0, 3],
        [3, 3, 3, 0]
    ], "Additional 1"

    print("All passed")
