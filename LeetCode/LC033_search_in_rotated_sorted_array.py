"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
P033 Search in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
"""

from typing import *

class Solution_A:
    def search(self, nums: List[int], target: int) -> int:
        """
        Recursion method, complicated binary search O(logN)
        Unecessary at all, method abandoned
        """
        L, H = 0, len(nums) - 1

        def search_helper(L: int, H: int) -> int:
            """Helper"""

            M = (L + H) // 2
            low, mid, high = nums[L], nums[M], nums[H]

            # 直接查两端, 如果满足就结束
            if nums[L] == target:
                return L
            elif nums[H] == target:
                return H

            # 如果缩到最后,长度只有2了,还是没有发现target只能return -1
            elif H - L <= 1 and nums[L] != target and nums[H] != target:
                return -1

            # 把list从中间切开,其中一半必为排序,另一半不确定是否排序
            # 如果target在排序的那一段其中,那么就接着二分法
            elif low < mid and low <= target <= mid:
                return search_helper(L, M)
            elif mid < high and mid <= target <= high:
                return search_helper(M, H)


            # 如果没有出现以上情况,那target必在没有排序的一段中 (而且只可能有一段不是排序的)
            # 而且就算不是排序的, 二分法同样可以继续
            elif low > mid:
                return search_helper(L, M)
            elif mid > low:
                return search_helper(M, H)

        # 避免nums为空
        return -1 if not nums else search_helper(L, H)

class Solution_B:
    def search(self, nums: List[int], target: int) -> int:
        """
        Regular while loop, binary search O(logN) * c
        """
        if not nums:
            return -1

        L, H = 0, len(nums) - 1
        while L <= H:
            M = (L + H) // 2
            low, mid, high = nums[L], nums[M], nums[H]
            if mid == target:
                return M
            if L == H:
                return L if low == target else -1
            if low <= target <= mid:
                H = M - 1
            elif mid <= target <= high:
                L = M + 1

            # if target not in sorted sub-array, then it must be in the unsorted sub-array
            # there could be only 1 unsorted sub-array
            elif low > mid:
                H = M - 1
            elif mid >= low:
                L = M + 1


class Solution_C:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search, with help of standard binary search for sorted array
        """

        if not nums:
            return -1

        L = 0
        H = len(nums) - 1

        while L <= H:
            M = (L + H) // 2
            low, mid, high = nums[L], nums[M], nums[H]

            if mid <= high:  # identify mid to hi is sorted
                potential_ans = self.binary_search(nums, M, H, target)
                if potential_ans != -1:   # confirm if target in the sorted array section
                    return potential_ans

                # if not, then ans must be in the other section (un-sorted, just keep breaking down)
                else:
                    H = M - 1

            else:  # identify lo to mid is sorted
                potential_ans = self.binary_search(nums, L, M, target)
                if potential_ans != -1:   # confirm if target in the sorted array section
                    return potential_ans

                # if not, then ans must be in the other section (un-sorted, just keep breaking down)
                else:
                    L = M + 1
        return -1

    def binary_search(self, nums: List[int], L: int, H: int, target: int) -> int:
        """
        helper functin for standard binary search in a sorted array at specific range
        a quick modification to definte binary search at specific range of indices
        """
        while L <= H:
            M = (L + H) // 2
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else:
                H = M - 1
        return -1


if __name__ == "__main__":
    testCase = Solution_C()
    assert testCase.search([], 1) == -1, "Edge 1"
    assert testCase.search([1], 1) == 0, "Edge 2"
    assert testCase.search([0], 1) == -1, "Edge 3"

    assert testCase.search([4, 5, 6, 7, 0, 1, 2], 0) == 4, "Example 1"
    assert testCase.search([4, 5, 6, 7, 0, 1, 2], 3) == -1, "Example 2"

    assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 3) == 0, "Additional 1"
    assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 4) == 1, "Additional 2"
    assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 8) == 5, "Additional 3"
    assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 10) == 7, "Additional 4"
    assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 1) == 8, "Additional 5"
    assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 2) == 9, "Additional 6"

    assert testCase.search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 8) == 0, "Additional 7"
    assert testCase.search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 1) == 3, "Additional 8"
    assert testCase.search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 6) == 8, "Additional 9"

    assert testCase.search([1, 3], 2) == -1, "Extra"

    print("all passed")
