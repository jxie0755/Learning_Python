"""
https://leetcode.com/problems/permutations/
P046 Permutations
Medium

Given a collection of distinct (数字不会重复) integers, return all possible permutations.
"""

from typing import *
from itertools import permutations
from math import factorial


class Solution_A:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        use python's internal method, only for testing the speed
        """

        result = []
        for i in permutations(nums):
            result.append(list(i))
        return result


class Solution_B1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Version B1
        Proxy-version, convert to permutation of indexes, then replace with nums[idx]
        """

        total_n = factorial(len(nums))
        result = []
        perm_idxs = list(range(len(nums)))
        for i in range(total_n):
            next_perm = [nums[i] for i in perm_idxs]
            result.append(next_perm)
            perm_idxs = self.next_permute(perm_idxs)
        return result

    def next_permute(self, nums: List[int]) -> List[int]:
        """
        Herlper for B1, B2
        From Leetcode LC031: next permutation, modified to return a new permute list instead in-place
        calculate the next permuatation, with integers 0 to N-1 (as idx proxy)
        this will both modify idx_list and return the updated idx_list
        """

        # 从后往前找到第一次出现下降趋势那个元素
        first_idx = len(nums) - 2
        second_idx = len(nums) - 1

        # 先定位first_idx
        while first_idx >= 0 and nums[first_idx] >= nums[first_idx + 1]:
            first_idx -= 1

        if first_idx == -1:  # 如果完美倒序上升,则已经逆序排好,直接反转即可
            return nums[:][::-1]
        else:
            # 定位second_idx
            # 由于尾部已经是逆序排好, 所以从尾部开始倒退,第一个>first_element的元素就是second_element
            ans = nums[::] # duplicate nums, and swap in-lace
            while ans[second_idx] <= ans[first_idx]:
                second_idx -= 1

            # complete the swap
            ans[first_idx], ans[second_idx] = ans[second_idx], ans[first_idx]
            # reverse element after first_idx
            ans[first_idx + 1:] = ans[first_idx + 1:][::-1]
            return ans


class Solution_B2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Version B2
        Non-proxy, recursive method, but direct handle elements in nums
        This only works for when sample is a collection of distinct numbers
        """

        total_n = factorial(len(nums))
        result = []
        for i in range(total_n):
            result.append(nums[:])
            nums = self.next_permute(nums)
        return result

    def next_permute(self, nums: List[int]) -> List[int]:
        """
        Herlper for B1, B2
        From Leetcode LC031: next permutation, modified to return a new permute list instead in-place
        calculate the next permuatation, with integers 0 to N-1 (as idx proxy)
        this will both modify idx_list and return the updated idx_list
        """

        # 从后往前找到第一次出现下降趋势那个元素
        first_idx = len(nums) - 2
        second_idx = len(nums) - 1

        # 先定位first_idx
        while first_idx >= 0 and nums[first_idx] >= nums[first_idx + 1]:
            first_idx -= 1

        if first_idx == -1:  # 如果完美倒序上升,则已经逆序排好,直接反转即可
            return nums[:][::-1]
        else:
            # 定位second_idx
            # 由于尾部已经是逆序排好, 所以从尾部开始倒退,第一个>first_element的元素就是second_element
            ans = nums[::]  # duplicate nums, and swap in-lace
            while ans[second_idx] <= ans[first_idx]:
                second_idx -= 1

            # complete the swap
            ans[first_idx], ans[second_idx] = ans[second_idx], ans[first_idx]
            # reverse element after first_idx
            ans[first_idx + 1:] = ans[first_idx + 1:][::-1]
            return ans


class Solution_C:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Version C
        Direct Recursive method, no need for next permuteUnique
        """

        def permuteHelper(lst: List[int], permute_list: List[int] = []) -> None:
            """Helper C"""

            if len(lst) == 0: # end case, when all elements are picked
                result.append(permute_list)
            else:
                for i in range(len(lst)):  # pick one element, and take the rest to recursive run for another pick
                    sub_list = lst[:]  # it will be the sub-list after the pop
                    picked = sub_list.pop(i) # Copy lst then remove i 1 by 1
                    updated_permute_list = permute_list + [picked]  # sequence
                    permuteHelper(sub_list, updated_permute_list)

        result = []
        permuteHelper(nums)
        return result


class Solution_D:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Pure recursive method"""

        if len(nums) == 1:
            return [nums]
        else:
            result = []
            for i in range(len(nums)):
                sub_list = nums[:]
                picked = sub_list.pop(i)
                # sequence looks oppositve than version C because of the recursion
                result += [[picked] + per for per in self.permute(sub_list)]
            return result


if __name__ == "__main__":
    testCase = Solution_C()
    assert testCase.permute([1]) == [
        [1]
    ], "Edge 1"

    assert testCase.permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ], "Example 1"

    print("all passed")
