# p053 Maximum Subarray
# Easy

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# """
# :type nums: List[int]
# :rtype: int
# """

class Solution:
    def maxSubArray(self, nums):  # O(n^2), Time Limit Exceeded, for large input size
        result = []
        for length in range(1, len(nums) + 1):
            for start in range(0, len(nums) - length + 1):
                result.append(sum(nums[start:start + length]))
        return max(result)

    # TODO Need to come up with a O(n) method


if __name__ == '__main__':
    assert Solution().maxSubArray([1, 2, 3, 4]) == 10, 'regular, all positive'
    assert Solution().maxSubArray([-1, -2, -3, -4]) == -1, 'all negative'
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, 'mixed positive and negative'
    assert Solution().maxSubArray([2, 2, 0, -1]) == 4, 'contains 0'
    print('all passed')


