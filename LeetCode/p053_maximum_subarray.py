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

    def maxSubArray(self, nums):  # O(n), using local and global max_value to iterate over the elements
        if all(i < 0 for i in nums):
            return max(nums)
        global_max, local_max = 0, 0
        for i in nums:
            local_max = max(0, local_max + i)
            global_max = max(global_max, local_max)
        return global_max


if __name__ == '__main__':
    assert Solution().maxSubArray([1, 2, 3, 4]) == 10, 'regular, all positives'
    assert Solution().maxSubArray([-1, -2, -3, -4]) == -1, 'all negatives'
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, 'mixed positive and negative'
    assert Solution().maxSubArray([2, 2, 0, -1]) == 4, 'contains 0'
    assert Solution().maxSubArray([-2, -1, -1, -1, -1, -1, -1, -1, 1]) == 1, 'a lot of negatives'
    assert Solution().maxSubArray([0, 0, -3, 1]) == 1, 'group of all zero'
    assert Solution().maxSubArray([1]) == 1, 'only one pos'
    assert Solution().maxSubArray([-1]) == -1, 'only one neg'
    assert Solution().maxSubArray([0]) == 0, 'only one zero'
    assert Solution().maxSubArray([0, -1, -1, 0, 0, 0, -1, -2, -3]) == 0, 'only one zero'
    assert Solution().maxSubArray([0, 0, 0, 0, 0, 0]) == 0, 'all zeros'
    print('all passed')


