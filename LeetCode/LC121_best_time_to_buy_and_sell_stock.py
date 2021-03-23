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
        """
        starting from each element, find the max value after the element
        the max of each (max value - element) if >0, else return 0
        Time O(N^2), exceeded max time limit
        """
        max_so_far = 0
        for i in range(len(prices)):
            max_so_far = max(max(prices[i:]) - prices[i], max_so_far)
        return max_so_far


class Solution_B1:
    def maxProfit(self, prices: List[int]) -> int:
        """
        折断法, 以list中最小值做切割
        This will pass but very slow
        """
        profits = [0]
        while prices:
            low = min(prices)
            low_idx = prices.index(low)
            profit = max(prices[low_idx:]) - low
            profits.append(profit)
            prices = prices[:low_idx]

        return max(profits)

class Solution_B2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        折断法 with recursion
        This will pass but very slow
        """
        if not prices:
            return 0
        else:
            low = min(prices)
            low_idx = prices.index(low)
            profit = max(prices[low_idx:]) - low
            return max(profit, self.maxProfit(prices[:low_idx]))

class Solution_STD:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Keep tracking minimum price and max profit
        And compare current price - minimum price with current max_profit
        """
        max_profit, min_price = 0, float("inf")
        # 无穷大

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

class Solution_STD2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Modified from STD, with better logic expression
        此题本质就是迭代刷新最低价,
        然后得到一个新的最低价之后的(当前价-最低价)得到一个利润, 然后基于此最低价寻找更高的利润
        若出现新的最低价, 那么就从新的最低价开始重新寻找新的利润并与之前的最高利润做对比
        由于价格有变化按照时间线,得到了新的最低价,此前的出现过的高价位不可能在这个最低价之后被买入,所以不必重复计算
        """
        min_price = float("inf")
        profit = 0
        for i in range(len(prices)):
            current = prices[i]
            min_price = min(min_price, current)
            profit = max(profit, current - min_price)
        return profit



if __name__ == "__main__":
    testCase = Solution_STD2()

    assert testCase.maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Example 1"
    # Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

    assert testCase.maxProfit([7, 6, 4, 3, 1]) == 0, "Example 2"
    # In this case, no transaction is done, i.e. max profit = 0

    assert testCase.maxProfit([100, 5, 25, 1, 20]) == 20, "Additional 1"

    print("All passed")

