# P189 Rotate Array
# Easy

# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums, k):
        # O(N) space, with O(N) time.
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        real_k = k % len(nums)
        target = nums[-real_k:] + nums[:-real_k]

        # i = 0
        # while i != len(nums):
        #     nums[i] = target[i]
        #     i += 1

        # Can be simplified as:
        nums[:] = target

    def rotate_pop(self, nums, k):
        # O(1) space, with O(N) time.
        # Somehow it is much slower
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        real_k = k % len(nums)

        i = 0
        while i != real_k:
            nums.insert(0, nums.pop())
            i += 1



if __name__ == "__main__":
    a = [1,2,3,4,5,6,7]
    Solution().rotate(a, 0)
    assert a == [1,2,3,4,5,6,7], "Edge"

    a = [1,2,3,4,5,6,7]
    Solution().rotate(a, 3)
    assert a == [5,6,7,1,2,3,4], "Example 1"

    a = [-1,-100,3,99]
    Solution().rotate(a, 2)
    assert a == [3,99,-1,-100], "Example 2"

    a = [1,2,3,4]
    Solution().rotate(a, 5)
    assert a == [4,1,2,3], "Large k"

    print("all passed")
