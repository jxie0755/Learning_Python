# P216 Combination Sum III
# Medium


# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

from typing import *


class Solution(object):

    # Use the combination method from Leetcode P077 and verify each one
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

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        for i in self.combinationSolo([1, 2, 3, 4, 5, 6, 7, 8, 9], k):
            if sum(i) == n:
                result.append(i)
        return result


if __name__ == "__main__":
    assert Solution().combinationSum3(3, 7) == [[1, 2, 4]], "Example 1"
    assert Solution().combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]], "Example 2"
    print("All passed")
