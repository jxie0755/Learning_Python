# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0

        if len(num) == 1:
            return num[0]

        num_i, num_i_1 = max(num[1], num[0]), num[0]
        for i in xrange(2, len(num)):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(num[i] + num_i_2, num_i_1)

        return num_i

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
