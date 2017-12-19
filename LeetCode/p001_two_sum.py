# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in sorted(nums):
            if target - i in nums:
                result.append(i)
                result.append(target - i)
                break
        output = []
        for j in result:
            output.append(nums.index(j))
            nums[nums.index(j)] = 'x'
        return output


a = [2, 7, 11, 15]
b = [1, 3, 3]
case = Solution()
print(case.twoSum(a, 9))
print(case.twoSum(b, 6))
