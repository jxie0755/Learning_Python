# P209 Minimum Size Subarray Sum
# Medium

# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

### Subarray is not subsequence, it does not require continuality

class Solution(object):

    ### Brutal force, check every subarray from short to long
    ### O(N^2)
    ### Time limit exceeded
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        for i in range(1, N+1):
            for start in range(0, N-i+1):
                sub = nums[start:start+i]
                if sum(sub) >= s:
                    return len(sub)
        return 0


if __name__ == '__main__':
    A = []
    assert Solution().minSubArrayLen(11, A) == 0, 'Edge 0'

    A = [1, 2, 3, 4]
    assert Solution().minSubArrayLen(11, A) == 0, 'Edge 1'

    A = [2, 3, 1, 2, 4, 3]
    assert Solution().minSubArrayLen(7, A) == 2, 'Example 1'

    A = [1, 2, 3, 4, 5]
    assert Solution().minSubArrayLen(11, A) == 3, 'Additional 1'

    A = [2, 16, 14, 15]
    assert Solution().minSubArrayLen(20, A) == 2, 'Additional 2'

    A = [12,28,83,4,25,26,25,2,25,25,25,12]
    assert Solution().minSubArrayLen(213, A) == 8, 'Additional 3'

    print('all passed')
