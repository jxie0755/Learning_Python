"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
LC004 Median of Two Sorted Array
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""

from typing import *


class Solution_A:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Time: O(N)
        Merge two sorted list then find the median
        Not very efficient, as we go all the way, and used a lot of space
        """

        def median(array: List[int]) -> float:
            """Helper"""
            length = len(array)
            half = length // 2
            if length == 0:
                return 0
            elif length % 2 != 0:
                return array[half]
            else:
                return (array[half - 1] + array[half]) / 2

        # Merge sort
        i, j = 0, 0
        merge = []
        while i <= len(nums1) - 1 or j <= len(nums2) - 1:
            if i == len(nums1):
                merge += nums2[j:]
                break
            elif j == len(nums2):
                merge += nums1[i:]
                break
            elif nums1[i] <= nums2[j]:
                merge.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                merge.append(nums2[j])
                j += 1

        return median(merge)

class Solution_B1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        O(1/2N)
        MergeSort like, Modified merge sort to only merge half way
        """
        L1, L2 = len(nums1), len(nums2)
        total_length = L1 + L2
        n = 0
        i1, i2 = 0, 0
        merge_list = []

        while n != total_length // 2 + 1:
            v1 = nums1[i1] if i1 < L1 else float('inf')
            v2 = nums2[i2] if i2 < L2 else float('inf')
            if v1 <= v2:
                merge_list.append(v1)
                i1 += 1
            else:
                merge_list.append(v2)
                i2 += 1
            n += 1

        if total_length % 2 == 0:
            return (merge_list[-1] + merge_list[-2]) / 2
        else:
            return merge_list[-1]


class Solution_B2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Time O(N), space O(1)
        MergeSort like, Same half way method with but only keep tracking the last two in the merge_list
        """

        L1, L2 = len(nums1), len(nums2)
        total_length = L1 + L2
        n = 0
        i1, i2 = 0, 0
        merge_list = [0, 0]

        while n != total_length // 2 + 1:

            merge_list[0] = merge_list[1] # 如果继续,第二项前移成为第一项,然后寻找新的第二项

            v1 = nums1[i1] if i1 < L1 else float('inf')
            v2 = nums2[i2] if i2 < L2 else float('inf')

            if v1 <= v2:
                merge_list[1] = v1
                i1 += 1
            else:
                merge_list[1] = v2
                i2 += 1

            n += 1

        if total_length % 2 == 0:
            return (merge_list[0] + merge_list[1]) / 2
        else:
            return merge_list[1]


if __name__ == "__main__":
    testCase = Solution_B2()
    assert testCase.findMedianSortedArrays([], [1]) == 1.0, "Edge 0"
    assert testCase.findMedianSortedArrays([2], []) == 2.0, "Edge 00"

    assert testCase.findMedianSortedArrays([1], [2]) == 1.5, "Empty 2"
    assert testCase.findMedianSortedArrays([2], []) == 2.0, "Edge 1"

    assert testCase.findMedianSortedArrays([1, 3], [2]) == 2.0, "Example 1"
    assert testCase.findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Example 2"
    assert testCase.findMedianSortedArrays([1, 2, 3, 4], [2, 3, 4, 5]) == 3.0, "Example 3"
    assert testCase.findMedianSortedArrays([3], [-2, -1]) == -1.0, "Negative"

    print("All passed")
