"""
https://leetcode.com/problems/next-permutation/
P031 Next Permutation
Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
Do not return anything, modify nums in-place instead!

The replacement must be in-place and use only constant extra memory.
Means you cannot list out all permutation and sort it, then find the next one.

Correct sequence (sorted):
 (1, 2, 3, 4)
 (1, 2, 4, 3)
 (1, 3, 2, 4)
 (1, 3, 4, 2)
 (1, 4, 2, 3)
 (1, 4, 3, 2)
 (2, 1, 3, 4)
 (2, 1, 4, 3)
 (2, 3, 1, 4)
 (2, 3, 4, 1)
 (2, 4, 1, 3)
 (2, 4, 3, 1)
 (3, 1, 2, 4)
 (3, 1, 4, 2)
 (3, 2, 1, 4)
 (3, 2, 4, 1)
 (3, 4, 1, 2)
 (3, 4, 2, 1)
 (4, 1, 2, 3)
 (4, 1, 3, 2)
 (4, 2, 1, 3)
 (4, 2, 3, 1)
 (4, 3, 1, 2)
 (4, 3, 2, 1)
 """

from itertools import permutations
from typing import *


class Solution_A:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Use itertool.permutations itearate the permutation sequence from small to large,
        and stop at the nums, then return the next one
        Exceeded max time limit
        """

        first_sample = False
        length = len(nums)

        for i in permutations(sorted(nums), length):
            check = list(i)
            if first_sample is False:
                first = check
                first_sample = True
            if check > nums:
                nums[:] = check
                first_sample = False
                break

        if first_sample:
            nums[:] = first


class Solution_B:
    def nextPermutation(self, nums: List[int]) -> None:

        if not nums:
            return None

        # 从后往前找到第一次出现下降趋势那个元素
        first_idx = len(nums) - 2
        second_idx = len(nums) - 1

        # 先定位first_idx
        while first_idx >= 0:
            if nums[first_idx] < nums[first_idx + 1]:
                break
            first_idx -= 1

        if first_idx == -1:  # 如果完美倒序上升,则已经逆序排好,直接反转即可
            nums.reverse()
        else:
            # 定位second_idx
            # 由于尾部已经是逆序排好, 所以从尾部开始倒退,第一个>first_element的元素就是second_element
            while second_idx > first_idx:
                if nums[second_idx] > nums[first_idx]:  # 定位成功后直接完成切换和尾部重新排序
                    # complete the swap
                    nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]
                    # sort all element after first_idx
                    nums[first_idx + 1:] = nums[first_idx + 1:][::-1]
                    break  # end process
                second_idx -= 1

    def prevPermutation(self, nums: List[int]) -> None:
        """
        This the the oppositve function to find previous permutation
        only need to simply modify the two places
        """


        if not nums:
            return None

        # 从后往前找到第一次出现上升趋势那个元素
        first_idx = len(nums) - 2
        second_idx = len(nums) - 1

        # 先定位first_idx
        while first_idx >= 0:
            pre = nums[first_idx]
            cur = nums[first_idx + 1]
            if pre > cur:  ############################## 反转对比符号
                break
            first_idx -= 1

        if first_idx == -1:  # 如果完美排序,直接反转即可
            nums.reverse()
        else:
            # 定位second_idx
            # 由于尾部已经是排序好, 所以从尾部开始倒退,第一个<first_element的元素就是second_element
            while second_idx > first_idx:
                if nums[second_idx] < nums[first_idx]:  ############################## 反转对比符号

                    # complete the swap
                    nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]
                    # sort all element after first_idx
                    nums[first_idx + 1:] = nums[first_idx + 1:][::-1]
                    break  # end process
                second_idx -= 1


if __name__ == "__main__":
    testCase = Solution_B()

    a = []
    testCase.nextPermutation(a)
    assert a == [], "Edge 1"
    testCase.prevPermutation(a)
    assert a == [], "Edge 1 prev"

    a = [1]
    testCase.nextPermutation(a)
    assert a == [1], "Edge 2"
    testCase.prevPermutation(a)
    assert a == [1], "Edge 2 prev"

    a = [1, 2]
    testCase.nextPermutation(a)
    assert a == [2, 1], "Edge 3"
    testCase.prevPermutation(a)
    assert a == [1, 2], "Edge 3 prev"

    a = [1, 2, 3]
    testCase.nextPermutation(a)
    assert a == [1, 3, 2], "Example 1"
    testCase.prevPermutation(a)
    assert a == [1, 2, 3], "Example 1 prev"

    a = [3, 2, 1]
    testCase.nextPermutation(a)
    assert a == [1, 2, 3], "Example 2"
    testCase.prevPermutation(a)
    assert a == [3, 2, 1], "Example 2 prev"

    a = [1, 1, 5]
    testCase.nextPermutation(a)
    assert a == [1, 5, 1], "Example 3"
    testCase.prevPermutation(a)
    assert a == [1, 1, 5], "Example 3 prev"

    a = [5, 1, 1]
    testCase.nextPermutation(a)
    assert a == [1, 1, 5], "Extra 1"
    testCase.prevPermutation(a)
    assert a == [5, 1, 1], "Extra 1 prev"

    a = [2, 2, 2]
    testCase.nextPermutation(a)
    assert a == [2, 2, 2], "Extra 2"
    testCase.prevPermutation(a)
    assert a == [2, 2, 2], "Extra 2 prev"

    a = [1, 2, 2, 2]
    testCase.nextPermutation(a)
    assert a == [2, 1, 2, 2], "Extra 3"
    testCase.prevPermutation(a)
    assert a == [1, 2, 2, 2], "Extra 3 prev"

    a = [2, 3, 1]
    testCase.nextPermutation(a)
    assert a == [3, 1, 2], "Exatra 4"
    testCase.prevPermutation(a)
    assert a == [2, 3, 1], "Exatra 4"

    print("all passed")
