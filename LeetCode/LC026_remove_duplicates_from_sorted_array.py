"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
p026 Remove duplicates from sorted array
Easy

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
意思是不能再造一个新list,而是在原list上改动
"""

from typing import *


class Solution_A:

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Simple iteration with flag
        思路在于利用外部游标对应遍历时的瞬间赋值
        """
        check = float('inf')  # 设立一个核查值,检查重复

        length = 0
        new_idx = 0

        for i in range(len(nums)):
            cur = nums[i]
            if cur != check:
                nums[new_idx] = cur  # 只要不重复,就在new_idx重新赋值一次,哪怕new_idx == i
                check = cur          # 不重复的话,就更新check
                length += 1
                new_idx += 1

            # 如出现重复,则length和new_idx都不移动,check也不变,直到下次出现不重复

        return length
        # 注意, 这里不会减少array长度, 只是把不重复的元素位置提前了, 返回的是新的去重后的计算长度


if __name__ == "__main__":
    testCase = Solution_A()

    Empty = []
    assert testCase.removeDuplicates(Empty) == 0, "Empty"
    assert Empty == [], "Empty revised list"

    Q0 = [1, 1]
    assert testCase.removeDuplicates(Q0) == 1, "Edge"
    assert Q0 == [1, 1], "Edge 0 revised list"

    Q1 = [1, 1, 2, 2, 3]
    assert testCase.removeDuplicates(Q1) == 3, "Example 1"
    assert Q1 == [1, 2, 3, 2, 3], "Example 1 revised list"

    print("All passed")
