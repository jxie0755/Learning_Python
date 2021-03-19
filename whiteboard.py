"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
LC121 Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
from typing import *


class Solution_A:
    def maxProfit(self, prices: List[int]) -> int:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    assert testCase.maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Example 1"
    # Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

    assert testCase.maxProfit([7, 6, 4, 3, 1]) == 0, "Example 2"
    # In this case, no transaction is done, i.e. max profit = 0

    assert testCase.maxProfit([100, 5, 25, 1, 20]) == 20, "Additional 1"

    print("All passed")
