# P209 Minimum Size Subarray Sum
# Medium

# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

### Subarray is not subsequence, it does not require continuality

class Solution(object):

    ### Version A, Brutal force, check every subarray from short to long
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

    ### Version B, O(N)
    ### 先得到整个list的和, 如果超过s, 则减去两端中最小的那个, 然后重复下去
    ### Case Addtional 5 可以证明这个思路是错的
    # def minSubArrayLen(self, s, nums):
    #     """
    #     :type s: int
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #
    #     L = len(nums)
    #     while len(nums) != 0:
    #         N = len(nums)
    #         numsum = sum(nums)
    #         if numsum < s:
    #             if N == L:
    #                 return 0
    #             else:
    #                 return N+1
    #         else:
    #             if N == 1:
    #                 return 1
    #             elif nums[0] > nums[-1]:
    #                 nums.pop()
    #             else:
    #                 nums.pop(0)


class Solution(object):

    ### Version C1, O(N)
    ### move index head and tail according to the sum of the subarray
    ### this wil exceed time limt....
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0

        L = len(nums)
        head, tail = 0, 0

        while head != len(nums):
            sub = nums[head:tail+1]
            sub_l = len(sub)
            sub_sum = sum(sub)

            if sub_sum >= s:
                if sub_l < L: # track minium length
                    L = sub_l

                # if sub_sum exceed, then move head to shorten, unless head hit tail
                if head < tail:
                    head += 1
                else: # if head hit tail, the length is 1, no need to proceed
                    break
            else:
                if tail < len(nums) - 1:  # move tail, so the sub gets longer, unless tail hit the end
                    tail += 1
                else: # if tail hit the end, move head towards the end to end the while loop
                    break
        return L


class Solution(object):

    ### Version C2, O(N)
    ### move index head and tail according to the sum of the subarray
    ### A different way of calculating sum, avoid sum(subarray)
    ### This passed very good
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0

        L = len(nums)
        head, tail = 0, 0
        sub_sum = nums[0]

        while head != len(nums):

            if sub_sum >= s:
                sub_l = tail - head + 1
                if sub_l < L: # track minium length
                    L = sub_l

                # if sub_sum exceed, then move head to shorten, unless head hit tail
                if head < tail:
                    sub_sum -= nums[head]
                    head += 1

                else: # if head hit tail, the length is 1, no need to proceed
                    break
            else:
                if tail < len(nums) - 1:  # move tail, so the sub gets longer, unless tail hit the end
                    tail += 1
                    sub_sum += nums[tail]
                else: # if tail hit the end, move head towards the end to end the while loop
                    break
        return L


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

    A = [1,4,4]
    assert Solution().minSubArrayLen(3, A) == 1, 'Additional 4'

    A = [4,1,1,1,4,3]
    assert Solution().minSubArrayLen(7, A) == 2, 'Additional 5'

    A = [4,4,1,1,1,5,1,1]
    assert Solution().minSubArrayLen(8, A) == 2, 'Additional 6'

    print('all passed')
