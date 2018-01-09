# p026 Remove duplicates from sorted array
# Easy

# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 意思是不能再造一个新list,而是在原list上改动


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)

nums = [1,1,2]
print(Solution().removeDuplicates(nums))


