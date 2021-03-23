"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
LC122 Best time to buy and sell stock II
Easy


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

from typing import *

class Solution_A:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Compare the two adjacent value and capture the profit if later is higher
        """
        if len(prices) <= 1:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            prev = prices[i - 1]
            cur = prices[i]
            if prev < cur:
                profit += cur - prev
        return profit


if __name__ == "__main__":
    testCase = Solution_A()

    assert testCase.maxProfit([0]) == 0, "Edge 0"
    assert testCase.maxProfit([1]) == 0, "Edge 1"
    assert testCase.maxProfit([1, 1, 1]) == 0, "Edge 2"

    assert testCase.maxProfit([7, 1, 5, 3, 6, 4]) == 7, "Example 1"
    # Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    # Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

    assert testCase.maxProfit([1, 2, 3, 4, 5]) == 4, "Example 2"
    # Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    # Note that you cannot buy on day 1, buy on day 2 and sell them later
    # as you are engaging multiple transactions at the same time. You must sell before buying again.

    assert testCase.maxProfit([7, 6, 4, 3, 1]) == 0, "Example 3"
    # In this case, no transaction is done, i.e.max profit = 0.

    assert testCase.maxProfit([1, 2, 2, 2, 3, 3, 2, 2]) == 2, "Additional 1"
    # flat peak

    assert testCase.maxProfit([2, 1, 4]) == 3, "Additional 2"

    print("All passed")
