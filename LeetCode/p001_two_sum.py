# p001 Two Sum
# Easy

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):  # beats 55.36%
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

if __name__ == '__main__':
    assert Solution().twoSum([11, 2, 7, 15], 9) == [1,2],  'regular'
    assert Solution().twoSum([3, 3], 6) == [0,1],  'two identical'
    assert Solution().twoSum([-1, -2, -3, -4, -5], -8) == [2, 4],  'negative int'
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2],  'struggle with 1/2 target'
