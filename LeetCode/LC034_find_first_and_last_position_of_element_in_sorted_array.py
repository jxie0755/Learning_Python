"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
P033 Find First and Last Positions of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1]
"""

from typing import *

class Solution_A:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        improved binary search
        3 binary search, find catch mid value, and Low/High of the section,
        Then according to mid value and Low/High to find head and tail by 2 additional binary search
        O(LogN), Space O(1)
        """

        L, H = 0, len(nums) - 1
        target_found = False
        # first determine if target is in nums
        # 简单的二分法, 但是搜到一个答案后, 应该直接结束 (因为答案不唯一)
        while L <= H:
            M = (L + H) // 2
            if nums[M] < target:
                L = M + 1
            elif target < nums[M]:
                H = M - 1
            else:
                target_found = True
                break

        # 找不到答案就返回[-1,-1], 只要能找到一个答案, 则必不可能为[-1,-1]
        if not target_found:
            return [-1, -1]


        head = tail = M

        # first find head
        # 这个binary search移动思路就是head不能离开target,L要逐渐摆脱非target的部分
        # 有两种方式终结while loop,第一是L已经是target了,第二是head上一位不是target
        while True:
            M = (L + head) // 2
            if nums[L] == target:  # 先检查末端是否为target如果是则不需要继续
                head = L
                break
            if nums[M] == target:  # 所以nums[M]已不可能大于target, 所以此处只可能是nums[M] == target
                # 由于先前定位了M已经是的nums[M]==target, 而array是排序的,head已无可能向后移动
                head = M  # head不离开target
                if nums[M - 1] != target:  # M上一位如果不是target即可结束, 否则继续寻找
                    break
            if nums[M] < target: # 如果中值小于目标,则直接把L移动到M之后
                L = M + 1


        # second find tail
        # 这个binary search移动思路就是tail不能离开target,H要逐渐摆脱非target的部分
        # 有两种方式终结while loop,第一是H已经是target了,第二是tail下一位不是target
        while True:
            M = (tail + H) // 2
            if nums[H] == target:  # 先检查末端是否为target如果是则不需要继续
                tail = H
                break
            if nums[M] == target:
                tail = M # tail不离开target
                if nums[M + 1] != target:  # M下一位如果不是target即可结束, 否则继续寻找
                    break
            if nums[M] > target:  # 如果中值大于目标,则直接把H移动到M之前
                H = M - 1

        return [head, tail]


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.searchRange([], 0) == [-1, -1], "Edge 0"
    assert testCase.searchRange([8], 8) == [0, 0], "Edge 1"
    assert testCase.searchRange([0], 8) == [-1, -1], "Edge 2"

    assert testCase.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4], "Example 1"
    assert testCase.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1], "Example 2"

    assert testCase.searchRange([5, 7, 7, 7, 8, 10], 8) == [4, 4], "Addtional 1"
    assert testCase.searchRange([5, 7, 7, 7, 8, 10], 7) == [1, 3], "Addtional 2"

    assert testCase.searchRange([1, 4], 4) == [1, 1], "Additional 1"
    assert testCase.searchRange([1, 3], 1) == [0, 0], "Additional 2"
    assert testCase.searchRange([-3, -2, -1], 0) == [-1, -1], "Additional 3"
    assert testCase.searchRange([0, 0, 2, 3, 4, 4, 4, 5], 5) == [7, 7], "Additional 4"
    assert testCase.searchRange([0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 8, 10, 10], 4) == [10,
                                                                                                               13], "Additional 5"
    assert testCase.searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3) == [2, 5], "Additional 6"

    print("All passed")
