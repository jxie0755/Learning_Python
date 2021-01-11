# P368 Largest Divisible Subset
# Medium

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
# Si % Sj = 0 or Sj % Si = 0.
# If there are multiple solutions, return any subset is fine.

from typing import *


class Solution:

    # 本质上这题是找出最长的subset使得排序后,每隔元素都是上一个元素的整数倍

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

    # 本质上这题是找出最长的subset使得排序后,每隔元素都是上一个元素的整数倍

    # Version B
    # Exclude numbers that is already checked
    # Still exceeded max time limit
    def largestDivisibleSubset(self, nums: List[int]):
        if not nums:
            return []

        nums = sorted(nums)
        result = [[]]

        def helper(lst, start=0):
            """extend the lst into all possible subset"""
            # print("cur", lst)

            if start <= len(nums) - 1:
                for i in range(start + 1, len(nums)):
                    temp = nums[i]
                    if temp % lst[-1] == 0:
                        new_lst = lst + [temp]
                        helper(new_lst, i)
                    else:
                        helper([temp], i)
                if len(lst) > len(result[-1]):
                    result.append(lst)

        helper([nums[0]])
        return max(result, key=len)


class Solution(object):

    # STD ans, dynammic programming
    # TODO review after learning dynamic programming
    def largestDivisibleSubset(self, nums: List[int]):

        if not nums:
            return []

        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        largest_idx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[largest_idx] < dp[i]:
                largest_idx = i

        result = []
        i = largest_idx
        while i != -1:
            result.append(nums[i])
            i = prev[i]
        return result[::-1]


if __name__ == "__main__":
    assert Solution().largestDivisibleSubset([]) == [], "Edge 0"
    assert Solution().largestDivisibleSubset([1, 2, 3]) == [1, 2] or [1, 3], "Example 1"
    assert Solution().largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8], "Example 2"

    A = Solution().largestDivisibleSubset([2, 4, 6, 7, 10, 14, 28])
    assert A == [2, 4, 28] or A == [7, 14, 28], "Example 3"

    assert Solution().largestDivisibleSubset([1, 3, 9, 18, 54, 90, 108, 180, 360, 540, 720]) == \
           [1, 3, 9, 18, 90, 180, 360, 720], \
        "Additional 1"

    print("all passed")
