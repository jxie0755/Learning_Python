# P414 Third Maximum Number
# Easy

# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number.
# The time complexity must be in O(n).

from typing import *

import heapq


class Solution:

    # Version A, use a que to track 3 max value
    def thirdMax(self, nums: List[int]) -> int:
        que = []

        for cur in nums:
            if cur not in que:
                que.append(cur)
                que.sort()
                if len(que) > 3:
                    que.pop(0)

        return que[0] if len(que) == 3 else que[-1]

    # Vesion B, same idea, but use heapq to implement
    def thirdMax(self, nums: List[int]) -> int:
        que = []
        for cur in nums:
            if cur not in que:
                que.append(cur)
                heapq.heapify(que)
                if len(que) > 3:
                    heapq.heappop(que)

        return que[0] if len(que) == 3 else que[-1]


if __name__ == "__main__":
    assert Solution().thirdMax([3, 2, 1]) == 1, "Example 1"
    assert Solution().thirdMax([1, 2]) == 2, "Example 2"
    assert Solution().thirdMax([2, 2, 3, 1]) == 1, "Example 3"

    print("All passed")
