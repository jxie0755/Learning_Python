"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
P004 Median of Two Sorted Array
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""


from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Time: O(N)
        Merge two sorted list half-way then find the median
        """
        L1, L2 = len(nums1), len(nums2)
        total_length = L1 + L2
        n = 0
        i1, i2 = 0, 0
        temp = []
        while n!= total_length//2 + 1:
            v1 = nums1[i1] if i1 < L1 else float('inf')
            v2 = nums2[i2] if i2 < L2 else float('inf')
            if v1 <= v2:
                temp.append(v1)
                i1 += 1
            else:
                temp.append(v2)
                i2 += 1
            n += 1

        if total_length % 2 == 0:
            return (temp[-1] + temp[-2]) / 2
        else:
            return temp[-1]



if __name__ == "__main__":
    testCase = Solution()
    assert testCase.findMedianSortedArrays([], [1]) == 1.0, "Edge 1"
    assert testCase.findMedianSortedArrays([1], [2]) == 1.5, "Edge 2"
    assert testCase.findMedianSortedArrays([2], []) == 2.0, "Edge 3"

    assert testCase.findMedianSortedArrays([1, 3], [2]) == 2.0, "Example 1"
    assert testCase.findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Example 2"
    assert testCase.findMedianSortedArrays([1, 2, 3, 4], [2, 3, 4, 5]) == 3.0, "Example 3"
    assert testCase.findMedianSortedArrays([3], [-2, -1]) == -1.0, "Negative"

    print("all passed")
