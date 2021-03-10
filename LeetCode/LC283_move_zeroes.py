# LC283 Move Zeroes
# Easy


# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

from typing import *


class Solution:

    # Time:  O(n)
    # Space: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        if nums:
            length = len(nums)
            i = -1
            while i >= -length:
                if nums[i] == 0:
                    nums.append(nums.pop(i))
                i -= 1


class Solution(object):

    # Time:  O(n)
    # Space: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
            print(nums)


if __name__ == "__main__":
    a = []
    Solution().moveZeroes(a)
    assert a == [], "Edge 0"

    a = [0]
    Solution().moveZeroes(a)
    assert a == [0], "Edge 2"

    a = [0, 0, 0]
    Solution().moveZeroes(a)
    assert a == [0, 0, 0], "Edge 3"

    a = [1]
    Solution().moveZeroes(a)
    assert a == [1], "Edge 4"

    a = [1, 1, 1]
    Solution().moveZeroes(a)
    assert a == [1, 1, 1], "Edge 5"

    a = [1, 0]
    Solution().moveZeroes(a)
    assert a == [1, 0], "Edge 6"

    a = [0, 1, 0, 3, 12]
    Solution().moveZeroes(a)
    assert a == [1, 3, 12, 0, 0], "Example 1"

    print("All passed")
