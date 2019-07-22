# p027 Remove Element
# Easy

# Given an array and a value, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

from typing import *
import timeit


class Solution(object):

    # Version A
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


if __name__ == "__main__":

    nums = [3, 2, 2, 3]
    assert Solution().removeElement(nums, 3) == 2, "Example 1"
    assert nums == [2, 2], "Example 1 final list"

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert Solution().removeElement(nums, 2) == 5, "Example 2"
    assert nums == [0, 1, 3, 0, 4], "Example 2 final list"

    print('all passed')
