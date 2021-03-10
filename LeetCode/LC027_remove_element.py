"""
https://leetcode.com/problems/remove-element/
LC027 Remove Element
Easy

Given an array and a value, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

from typing import *

class Solution_A:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Imperfect, Change of the Array length should be avoided
        """
        n = 0
        while n < len(nums):
            # this force to recalculate len() in O(1)
            # so that index will not out of range

            if nums[n] == val:
                nums.pop(n)  # if pop(), next element will move to the current index, no need to move n
            else:
                n += 1  # if no pop(), then move n to next index
        return len(nums)

class Solution_B:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        This slower by checking val in nums everytime O(N)
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

class Solution_C:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        No pop, re-arrange with two flags
        """
        new_idx = 0
        new_len = len(nums)

        for i in range(len(nums)):
            if nums[i] != val:
                nums[new_idx] = nums[i]
                new_idx += 1
            else:
                new_len -= 1 # directly reduce length

        return new_len


if __name__ == "__main__":
    testCase = Solution_C()

    nums = []
    assert testCase.removeElement(nums, 3) == 0, "Edge 0"
    assert nums == [], "Edge 0 final list"

    nums = [3, 2, 2, 3]
    assert testCase.removeElement(nums, 3) == 2, "Example 1"
    assert nums == [2, 2, 2, 3], "Example 1 final list"

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert testCase.removeElement(nums, 2) == 5, "Example 2"
    assert nums == [0, 1, 3, 0, 4, 0, 4, 2], "Example 2 final list"

    print("All passed")
