"""
https://leetcode.com/problems/first-missing-positive/
P041 First Missing Positive
Hard

Given an unsorted integer array, find the smallest missing positive integer.

Note:
    Your algorithm should run in O(n) time and uses constant extra space.
"""

from typing import *


class Solution_A:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        O(N), space O(N) (not constant space)
        Use set to remove element, increase spped
        """
        all_possible = set(range(1, len(nums) + 2)) # range from [1 to len + 1]
        for i in nums:
            all_possible -= {i}
        return min(all_possible)


class Solution_STD:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        桶排序法
        Time: O(N)
        """

        n = len(nums)
        i = 0
        while i < n:  # while里面那句话执行的总次数最大就是nums的长度。一旦一个数字被放对位置,则不会再被移动,所以最多只能交换nums长度次数
            if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]: # 交换两者
                A = nums[i]
                B = nums[nums[i] - 1]
                nums[nums[i] - 1] = A
                nums[i] = B
            else:  # 连续性调换,直到每个排序正确为止
                i += 1

        # 第二轮排序后, 遍历找到第一个不符合者, 它的index+1即为结果,不然则是n+1在最末端
        for j in range(n):
            if nums[j] != j + 1:
                return i + 1
        return n + 1



if __name__ == "__main__":
    testCase = Solution_STD()
    assert testCase.firstMissingPositive([]) == 1, "Edge 1"
    assert testCase.firstMissingPositive([1]) == 2, "Edge 2"
    assert testCase.firstMissingPositive([2]) == 1, "Edge 3"
    assert testCase.firstMissingPositive([-1]) == 1, "Edge 4"

    assert testCase.firstMissingPositive([1, 2, 0]) == 3, "Example 1"
    assert testCase.firstMissingPositive([3, 4, -1, 1]) == 2, "Example 2"
    assert testCase.firstMissingPositive([7, 8, 9, 11, 12]) == 1, "Example 3"

    assert testCase.firstMissingPositive([2,2]) == 1, "Extra 1"

    print("all passed")
