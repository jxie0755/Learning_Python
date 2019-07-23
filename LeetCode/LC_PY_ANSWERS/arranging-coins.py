# Time:  O(logn)
# Space: O(1)

import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(8 * n + 1) - 1) / 2)  # sqrt is O(logn) time.


# Time:  O(logn)
# Space: O(1)
class Solution2(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if 2 * n < mid * (mid + 1):
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
