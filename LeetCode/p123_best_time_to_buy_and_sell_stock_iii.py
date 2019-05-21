# P123 Best Time to Buy and Sell Stock III
# Hard

#
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).


from typing import *

class Solution:

    ### THis is a complicate method
    ### TO compare single transaction and max profit for every peak
    ### Exceeded max time limit

    def singleMaxProfit(self, prices):
        ### according to the best method, Denis modified for clearer logic
        min_price = float('inf')
        profit = 0
        i = 0
        while i != len(prices):
            current = prices[i]
            if current < min_price:
                min_price = current
            profit = max(current - min_price, profit)
            i += 1
        return profit

    def profitBreakdown(self, prices):
        if not prices:
            return 0

        profits = []
        lo = 0
        i = 1
        foundprofit = False
        while i != len(prices):
            cur = prices[i]
            prev = prices[i-1]
            if cur <= prev:
                if foundprofit:
                    profits.append(prev - prices[lo])
                lo = i
                foundprofit = False
            else:
                foundprofit = True
                if i == len(prices)-1:
                    profits.append(cur - prices[lo])

            i += 1

        return profits


    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_two_so_far = 0
        i = 0
        while i != len(prices):

            if i < len(prices) -1:
                A = self.singleMaxProfit(prices[0:i+1]) + self.singleMaxProfit(prices[i+1:])
                Later = sorted(self.profitBreakdown(prices[i+1:]))
            else:
                A = self.singleMaxProfit(prices)
                Later = sorted(self.profitBreakdown(prices))

            if len(Later) <= 1:
                max_two_so_far = max(max_two_so_far, A)
            else:
                B = Later[-1] + Later[-2]
                max_two_so_far = max(max_two_so_far, A, B)

            i += 1

        return max_two_so_far



if __name__ == '__main__':
    assert Solution().maxProfit([]) == 0, 'Edge 0'
    assert Solution().maxProfit([1]) == 0, 'Edge 1'

    assert Solution().maxProfit([3,3,5,0,0,3,1,4]) == 6, 'Example 1, two transaction'
    assert Solution().maxProfit([1,2,3,4,5]) == 4, 'Example 2, one transaction'
    assert Solution().maxProfit([7,6,4,3,1]) == 0, 'Example 3, zero transaction'

    assert Solution().maxProfit([1,11,1,2,3,2,3,4,3,4,5]) == 14, 'Additional 1'
    assert Solution().maxProfit([5,6,1,4,2,6]) == 7, 'Additional 2'

    print('all passed')
