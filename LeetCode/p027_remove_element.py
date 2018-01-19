# p27 Remove Element
# Easy

# Given an array and a value, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeElement(self, nums, val):  # beats 51.33%
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        while n < len(nums):  # this force to recalculate len(), so that index will not out of range
            if nums[n] == val:
                nums.pop(n)  # if pop(), next element will move to the current index, no need to move n
            else:
                n += 1  # if no pop(), then move n to next index
        return len(nums)

    def removeElement2(self, nums, val):  # beats 26.37%
        while val in nums:
            nums.remove(val)
        return len(nums)


nums = [1, 2, 3, 4, 2, 3, 4, 4, 5, 6, 1, 2, 3, 4]
val = 4
print(Solution().removeElement(nums, val))
