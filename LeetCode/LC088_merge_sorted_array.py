"""
https://leetcode.com/problems/merge-sorted-array/
p088 Merge Sorted Array
Easy


Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Key is to modified nums1, not returning a new list
"""

from typing import *


class Solution_A1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Insert the properly sorted element from num2 to num1, while poping the end of num1 to keep the length
        """
        merged_idx = 0
        nums2_idx = 0
        while merged_idx != m + n and nums2_idx != n:
            cur = nums1[merged_idx]
            check = nums2[nums2_idx]
            if check <= cur or merged_idx == m + nums2_idx:
                # two conditions (insertable or reaching last index of nums1)
                # After inserting from nums 2, if i touch m+j then i is at last element of nums 1
                nums1.insert(merged_idx, check)
                nums1.pop()
                nums2_idx += 1
            merged_idx += 1


class Solution_A2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Insert the properly sorted element from num2 to num1, while poping the end of num1 to keep the length
        Clearer logic with simple codes
        """
        merged_idx = 0   # start from 0, end at m+n-1
        num_inserted = 0 # how many elem from nums2 inserted to nums1
        for elem in nums2:
            while elem >= nums1[merged_idx] and merged_idx < m + num_inserted:
                merged_idx += 1
            nums1.insert(merged_idx, elem)
            num_inserted += 1
            nums1.pop()


class Solution_B1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Treated as true array, length fixed, no insert or pop implement
        Developed based on Version A1
        Move every element one index to right when insert
        """
        merged_idx = 0
        nums2_idx = 0
        while merged_idx != m + n and nums2_idx != n:
            cur = nums1[merged_idx]
            check = nums2[nums2_idx]
            if check <= cur or merged_idx == m + nums2_idx:
                for x in range(merged_idx+1, m+n): # from idx=i+1 to end, move all to right, make space for insert
                    tmp = nums1[x]
                    nums1[x] = nums1[merged_idx]
                    nums1[merged_idx] = tmp
                nums1[merged_idx] = check # insert element from nums2
                nums2_idx += 1
            merged_idx += 1


if __name__ == "__main__":
    testCase = Solution_B1()

    nums1 = [1]
    nums2 = []
    testCase.merge(nums1, 1, nums2, 0)
    assert nums1 == [1], "T1"

    nums1 = [0]
    nums2 = [1]
    testCase.merge(nums1, 0, nums2, 1)
    assert nums1 == [1], "T2"

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    testCase.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], "T3"

    nums1 = [1, 5, 7, 0, 0, 0]
    nums2 = [2, 4, 10]
    testCase.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 4, 5, 7, 10], "T4"

    nums1 = [8, 8, 8, 0, 0, 0]
    nums2 = [1, 2, 3]
    testCase.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 8, 8, 8], "T5"

    nums1 = [1, 0, 0, 0]
    nums2 = [5, 5, 5]
    testCase.merge(nums1, 1, nums2, 3)
    assert nums1 == [1, 5, 5, 5], "T6"

    nums1 = [1, 2, 4, 5, 6, 0]
    nums2 = [3]
    testCase.merge(nums1, 5, nums2, 1)
    assert nums1 == [1, 2, 3, 4, 5, 6], "T7"

    nums1 = [4, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    testCase.merge(nums1, 1, nums2, 5)
    assert nums1 == [1, 2, 3, 4, 5, 6], "T8"

    nums1 = [4, 0, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    testCase.merge(nums1, 1, nums2, 5)
    assert nums1 == [1, 2, 3, 4, 5, 6, 0], "T9"

    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    nums2 = [1, 2, 2]
    testCase.merge(nums1, 6, nums2, 3)
    assert nums1 == [-1, 0, 0, 1, 2, 2, 3, 3, 3], "T10"

    print("All passed")
