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

        """
        if len(prices) == 0:
            return 0

        i, total_profit = 1, 0
        low = prices[0]

        while i != len(prices):
            current, prev = prices[i], prices[i - 1]
            if current < prev:  # 此处如果持续下降则只更新最低点
                low = current
            elif current > prev:  # 只要开始涨就卖出, 不过也再买入来更新最低点
                low = prev
                total_profit += current - low
            i += 1

        return total_profit

    def maxProfit_best(self, prices):
        # 直接计算每一步的收益,只要是正数就要,负数就算0
        # 逻辑精简但是未必更快
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
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

    assert testCase.maxProfit([5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]) == 20, "Additional 1"
    # 平峰需要注意

    assert testCase.maxProfit([2, 1, 4]) == 3, "Additional 2"

    print("All passed")
