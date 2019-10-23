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
        """
        O(N), directly find next different permutations
        """
        length = len(nums)
        cur_i = -1

        for i in range(-2, -length - 1, -1):
            if nums[i] < nums[i + 1]:
                cur_i = i
                break

        if cur_i == -1:
            nums[:] = nums[::-1]  # 直接结束,因为本身是倒着排序的,返回正排序即可
        else:
            for rev_i in range(-1, cur_i, -1):
                if nums[rev_i] > nums[cur_i]:
                    nums[cur_i], nums[rev_i] = nums[rev_i], nums[cur_i]  # switch
                    nums[cur_i + 1:] = nums[cur_i + 1:][::-1]  # reverse the tail back to sorted
                    break

class Solution_prev:
    def prevPermutation(self, nums: List[int]) -> None:
        """
        Addtional: prevPermute, which is the reverse process
        O(N), directly find previous different permutations
        """
        length = len(nums)
        cur_i = -1

        for i in range(-2, -length - 1, -1):
            if nums[i] > nums[i + 1]:
                cur_i = i
                break

        if cur_i == -1:
            nums[:] = nums[::-1]  # 直接结束,因为本身是倒着排序的,返回正排序即可
        else:
            for rev_i in range(-1, cur_i, -1):
                if nums[rev_i] < nums[cur_i]:
                    nums[cur_i], nums[rev_i] = nums[rev_i], nums[cur_i]  # switch
                    nums[cur_i + 1:] = nums[cur_i + 1:][::-1]
                    break


if __name__ == "__main__":
    testMethod = Solution_B().nextPermutation

    a = []
    testMethod(a)
    assert a == [], "Edge 1"

    a = [1]
    testMethod(a)
    assert a == [1], "Edge 2"

    a = [1, 2]
    testMethod(a)
    assert a == [2, 1], "Edge 3"

    a = [1, 2, 3]
    testMethod(a)
    assert a == [1, 3, 2], "Example 1"

    a = [3, 2, 1]
    testMethod(a)
    assert a == [1, 2, 3], "Example 2"

    a = [1, 1, 5]
    testMethod(a)
    assert a == [1, 5, 1], "Example 3"

    a = [5, 1, 1]
    testMethod(a)
    assert a == [1, 1, 5], "Extra 1"

    a = [2, 2, 2]
    testMethod(a)
    assert a == [2, 2, 2], "Extra 2"

    a = [1, 2, 2, 2]
    testMethod(a)
    assert a == [2, 1, 2, 2], "Extra 3"

    a = [2, 3, 1]
    testMethod(a)
    assert a == [3, 1, 2], "Exatra 4"

    print("all passed")
