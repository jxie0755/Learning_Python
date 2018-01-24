# p001 Two Sum
# Easy

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# type nums: List[int]
# type target: int
# rtype: List[int]
 
class Solution(object):
 			def twoSum(self, nums, target):  # brutal force, slowest
        for i in nums:
            index_i = nums.index(i)
            for j in nums[index_i+1:]:
                if i + j == target:
                    if i != j:
                        return [index_i, nums.index(j)]
                    else:
                        return [index_i, nums.index(i, index_i+1)]
    def twoSum2(self, nums, target):  # brutal force, check half first
        half = target / 2
        if nums.count(half) == 2:
            indexHalf =nums.index(half)
            return [indexHalf, nums.index(half, indexHalf+1)]
        for i in nums:
            if i != half:
                if target - i in nums:
                    return [nums.index(i), nums.index(target - i)]

if __name__ == '__main__':
    assert Solution().twoSum2([11, 2, 7, 15], 9) == [1,2],  'regular'
    assert Solution().twoSum2([11, 7, 2, 15], 9) == [1,2],  'regular revert'
    assert Solution().twoSum2([3, 3], 6) == [0,1],  'two identical'
    assert Solution().twoSum2([-1, -2, -3, -4, -5], -8) == [2, 4],  'negative int'
    assert Solution().twoSum2([3, 2, 4], 6) == [1, 2],  'struggle with 1/2 target'
    print('test done, all passed')
