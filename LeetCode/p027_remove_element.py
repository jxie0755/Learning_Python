"""
https://leetcode.com/problems/remove-element/
p027 Remove Element
Easy

Given an array and a value, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

from typing import *

class Solution(object):

    # Version A
    # Wrong, change of the Array length should be avoided
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        while n < len(nums):
            # this force to recalculate len() in O(1)
            # so that index will not out of range

            if nums[n] == val:
                nums.pop(n)  # if pop(), next element will move to the current index, no need to move n
            else:
                n += 1  # if no pop(), then move n to next index
        return len(nums)

    # Version B
    # This slower by checking val in nums everytime O(N)
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

    # Version C
    # No pop, re-arrange with two flags
    def removeElement(self, nums: List[int], val: int) -> int:
        i = n = 0
        L = len(nums)
        while n < len(nums):
            if nums[n] != val:
                nums[i] = nums[n]
                i += 1
            else:
                L -= 1
            n += 1

        return L


if __name__ == "__main__":
    nums = []
    assert Solution().removeElement(nums, 3) == 0, "Edge"
    assert nums == [], "Edge final list"

    nums = [3, 2, 2, 3]
    assert Solution().removeElement(nums, 3) == 2, "Example 1"
    assert nums == [2, 2, 2, 3], "Example 1 final list"

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert Solution().removeElement(nums, 2) == 5, "Example 2"
    assert nums == [0, 1, 3, 0, 4, 0, 4, 2], "Example 2 final list"

    print('all passed')
