# p026 Remove duplicates from sorted array
# Easy

# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 意思是不能再造一个新list,而是在原list上改动

class Solution(object):
    def removeDuplicates(self, nums):  # beats 83.31%
        """
        :type nums: List[int]
        :rtype: int
        """
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
        return index, nums

nums = [1,1,2,2,3]
print(Solution().removeDuplicates(nums))  # >>> (3, [1, 2, 3, 2, 3])


