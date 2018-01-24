# p001 Two Sum
# Easy

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# type nums: List[int]
# type target: int
# rtype: List[int]
 
class Solution(object):
    def twoSum(self, nums, target):  # beats 1.25%
        half = target / 2
        if nums.count(half) == 2:
            indexHalf =nums.index(half)
            return [indexHalf, nums.index(half, indexHalf+1)]
        for i in nums:
            if i != half:
                if target - i in nums:
                    return [nums.index(i), nums.index(target - i)]

if __name__ == '__main__':
    assert Solution().twoSum([11, 2, 7, 15], 9) == [1,2],  'regular'
    assert Solution().twoSum([11, 7, 2, 15], 9) == [1,2],  'regular revert'
    assert Solution().twoSum([3, 3], 6) == [0,1],  'two identical'
    assert Solution().twoSum([-1, -2, -3, -4, -5], -8) == [2, 4],  'negative int'
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2],  'struggle with 1/2 target'
    print('test done, all passed')

if __name__ == '__main__':
    from timeit import repeat
    result = repeat('Solution().twoSum([11, 2, 7, 15], 9)',
                    setup='from __main__ import Solution',
                    repeat=3, number=1000000)
    print(round(sum(result)/len(result), 4))
