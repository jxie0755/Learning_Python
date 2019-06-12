# P368 Largest Divisible Subset
# Medium

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
# Si % Sj = 0 or Sj % Si = 0.
# If there are multiple solutions, return any subset is fine.
from typing import *


class Solution:

    # 本质上这题是找出最长的subset使得他们的最大公约数在其中

    # Version A brutal force
    # Exceeded max time limit
    def combinationSolo(self, nums, k):
        if k == len(nums):
            return [nums]
        elif k == 1:
            return [[i] for i in nums]
        else:
            result = []
            next_list = nums[:]
            head = next_list.pop(0)
            result += [[head] + com for com in self.combinationSolo(next_list, k - 1)] + self.combinationSolo(nums[1:],
                                                                                                              k)
            return result

    def valid(self, combination):
        """check if this sorted combination meets the requirement"""
        if len(combination) == 1:
            return True
        for i in range(len(combination) - 1):
            small = combination[i]
            large = combination[i + 1]
            if large % small != 0:
                return False
        return True

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        N = len(nums)
        nums = sorted(nums)

        for i in range(N, 0, -1):
            all_combinations = self.combinationSolo(nums, i)
            for comb in all_combinations:
                if self.valid(comb):
                    return comb


class Solution:

    # 本质上这题是找出最长的subset使得他们的最大公约数在其中

    # Version B
    # Exclude numbers that is already checked
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums = sorted(nums)
        result = []
        while nums:
            temp = [nums.pop(0)]
            i = 0
            while i != len(nums):
                if nums[i] % temp[-1] == 0:
                    temp.append(nums.pop(i))
                else:
                    i += 1
            result.append(temp)

        return max(result, key=len)


print(Solution2().largestDivisibleSubset([1, 3, 9, 18, 54, 90, 108, 180, 360, 540, 720]))

# if __name__ == '__main__':
#     assert Solution().largestDivisibleSubset([]) == [], 'Edge 0'
#     assert Solution().largestDivisibleSubset([1, 2, 3]) == [1, 2] or [1, 3], 'Example 1'
#     assert Solution().largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8], 'Example 2'
#     assert Solution().largestDivisibleSubset([2, 4, 6, 7, 10, 14, 28]) == [2, 4, 28], 'Example 3'
#
#     assert Solution().largestDivisibleSubset([1, 3, 9, 18, 54, 90, 108, 180, 360, 540, 720]) == \
#            [1,3,9,18,90,180,360,720], \
#         'Additional 1'
#
#     print('all passed')
