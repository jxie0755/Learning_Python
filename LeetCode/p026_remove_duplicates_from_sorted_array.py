# p026 Remove duplicates from sorted array
# Easy

# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 意思是不能再造一个新list,而是在原list上改动

# """
# :type nums: List[int]
# :rtype: int
# """

class Solution(object):
    def removeDuplicates(self, nums):
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
        print(nums)
        return index

if __name__ == "__main__":
    assert Solution().removeDuplicates([1,1,2,2,3]) == 3, "regular test"
    print("all passed")
