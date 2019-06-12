# P368 Largest Divisible Subset
# Medium

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
# Si % Sj = 0 or Sj % Si = 0.
# If there are multiple solutions, return any subset is fine.

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        pass



if not __name__ == '__main__':

    assert Solution().largestDivisibleSubset([1,2,3]) == [1,2] or [1,3], 'Example 1'
    assert Solution().largestDivisibleSubset([1,2,4,8]) == [1,2,4,8], 'Example 2'

    print('all passed')
