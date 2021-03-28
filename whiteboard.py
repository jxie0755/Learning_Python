
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
LC123 Best Time to Buy and Sell Stock III
Hard


Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""


from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass


if __name__ == "__main__":
    testCase = Solution()

    assert testCase.maxProfit([]) == 0, "Edge 0"
    assert testCase.maxProfit([1]) == 0, "Edge 1"

    assert testCase.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6, "Example 1, two transaction"
    assert testCase.maxProfit([1, 2, 3, 4, 5]) == 4, "Example 2, one transaction"
    assert testCase.maxProfit([7, 6, 4, 3, 1]) == 0, "Example 3, zero transaction"

    assert testCase.maxProfit([1, 11, 1, 2, 3, 2, 3, 4, 3, 4, 5]) == 14, "Additional 1"
    assert testCase.maxProfit([5, 6, 1, 4, 2, 6]) == 7, "Additional 2"

    print("All passed")
