"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
p026 Remove duplicates from sorted array
Easy

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
意思是不能再造一个新list,而是在原list上改动
"""

from typing import *


class Solution(object):

    def removeDuplicates(self, nums: List[int]) -> int:
        """Version A"""

        if not nums:
            return 0

        index = 1  # The index where the character needs to be placed
        start = 0  # The index of repeating characters
        for i in range(1, len(nums)):
            if nums[start] != nums[i]:
                nums[index] = nums[i]
                index += 1
                start = i

        # 思路在于利用外部游标对应遍历时的瞬间赋值
        return index  # 注意, 这里不会减少array长度, 只是把不重复的元素位置提前了


if __name__ == "__main__":
    Empty = []
    assert Solution().removeDuplicates(Empty) == 0, "Empty"
    assert Empty == [], "Empty revised list"

    Q0 = [1, 1]
    assert Solution().removeDuplicates(Q0) == 1, "Edge"
    assert Q0 == [1, 1], "Edge 0 revised list"

    Q1 = [1, 1, 2, 2, 3]
    assert Solution().removeDuplicates(Q1) == 3, "Example 1"
    assert Q1 == [1, 2, 3, 2, 3], "Example 1 revised list"

    print("all passed")
