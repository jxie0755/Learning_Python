# p088 Merge Sorted Array
# Easy



# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# Example:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]

# Key is to modified nums1, not returning a new list

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        cur = 0
        tmp_n = 0
        for j in nums2:
            while j >= nums1[cur] and cur < m + tmp_n:
                cur += 1
            nums1.insert(cur, j)
            tmp_n += 1
            nums1.pop()


if __name__ == '__main__':
    nums1 = [1]
    nums2 = []
    Solution().merge(nums1, 1, nums2, 0)
    assert nums1 == [1], 'T1'

    nums1 = [0]
    nums2 = [1]
    Solution().merge(nums1, 0, nums2, 1)
    assert nums1 == [1], 'T2'

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], 'T3'

    nums1 = [1, 5, 7, 0, 0, 0]
    nums2 = [2, 4, 10]
    Solution().merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 4, 5, 7, 10], 'T4'

    nums1 = [8, 8, 8, 0, 0, 0]
    nums2 = [1, 2, 3]
    Solution().merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 8, 8, 8], 'T5'

    nums1 = [1, 0, 0, 0]
    nums2 = [5, 5, 5]
    Solution().merge(nums1, 1, nums2, 3)
    assert nums1 == [1, 5, 5, 5], 'T6'

    nums1 = [1, 2, 4, 5, 6, 0]
    nums2 = [3]
    Solution().merge(nums1, 5, nums2, 1)
    assert nums1 == [1, 2, 3, 4, 5, 6], 'T7'

    nums1 = [4, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    Solution().merge(nums1, 1, nums2, 5)
    assert nums1 == [1, 2, 3, 4, 5, 6], 'T8'

    nums1 = [4, 0, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    Solution().merge(nums1, 1, nums2, 5)
    assert nums1 == [1, 2, 3, 4, 5, 6, 0], 'T9'

    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    nums2 = [1,2,2]
    Solution().merge(nums1, 6, nums2, 3)
    assert nums1 == [-1,0,0,1,2,2,3,3,3], 'T10'

    print('all passed')
