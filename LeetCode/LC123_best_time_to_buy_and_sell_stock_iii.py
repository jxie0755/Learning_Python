"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
LC123 Best Time to Buy and Sell Stock III
Hard


Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""


from typing import *


class Solution_A:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Use a helper to find out single transaction max profit
        Then cut the prices into two halfs and find out the best cut point
        This will exceed max time limit
        """
        profit = 0
        for i in range(len(prices)):
            A = prices[:i]
            B = prices[i:]
            profit = max(profit, self.maxProfit_Single(A) + self.maxProfit_Single(B))
        return profit

    def maxProfit_Single(self, prices: List[int]) -> int:
        """
        Helper function for single transaction max profit
        Referred from LC121
        """
        min_price = float("inf")
        profit = 0
        for i in range(len(prices)):
            current = prices[i]
            min_price = min(min_price, current)
            profit = max(profit, current - min_price)
        return profit


class Solution_STD:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Modified method, only do comparison at the peak
        almost the same way as profit breakdown to find peaks
        This will still exceed max time limit
        """
        profit = 0
        foundpeak = False
        for i in range(len(prices)):
            cur = prices[i]
            prev = prices[i - 1]
            if cur <= prev and foundpeak:
                profit = max(profit, self.MaxProfit_Single(prices[:i]) + self.MaxProfit_Single(prices[i:]))
                foundpeak = False
            elif i == len(prices) - 1:
                profit = max(profit, self.MaxProfit_Single(prices))
            elif cur > prev:
                foundpeak = True

        return profit

    def MaxProfit_Single(self, prices):
        """
        Helper function for single transaction max profit
        Referred from LC121
        """
        min_price = float("inf")
        profit = 0
        for i in range(len(prices)):
            current = prices[i]
            min_price = min(min_price, current)
            profit = max(profit, current - min_price)
        return profit


if __name__ == "__main__":
    testCase = Solution_STD()

    assert testCase.maxProfit([]) == 0, "Edge 0"
    assert testCase.maxProfit([1]) == 0, "Edge 1"

    assert testCase.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6, "Example 1, two transaction"
    assert testCase.maxProfit([1, 2, 3, 4, 5]) == 4, "Example 2, one transaction"
    assert testCase.maxProfit([7, 6, 4, 3, 1]) == 0, "Example 3, zero transaction"

    assert testCase.maxProfit([1, 11, 1, 2, 3, 2, 3, 4, 3, 4, 5]) == 14, "Additional 1"
    assert testCase.maxProfit([5, 6, 1, 4, 2, 6]) == 7, "Additional 2"

    print("All passed")
