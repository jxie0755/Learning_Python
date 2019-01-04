# p121 Best Time to Buy and Sell Stock
# Easy

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.


# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit(self, prices):
        ### This method exceeded max time limit :(

        if not prices:
            return 0

        profits = []
        i = 0

        while i != len(prices):
            current = prices[i:]
            high = max(current)
            profits.append(high - current[0])
            i += 1

        answer = max(profits)
        return answer if answer > 0 else 0

    def maxProfit(self, prices):
        ### This method still exceeded max time limit :(

        profits = [0]

        # 折断法, 以list中最小值做切割
        while prices:
            low = min(prices)
            low_n = prices.index(low)
            profit = max(prices[low_n:]) - low
            profits.append(profit)
            prices = prices[:low_n]

        return max(profits)






if __name__ == '__main__':
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5, 'Smart trader'
    assert Solution().maxProfit([7,6,4,3,1]) == 0, 'No Transaction'
    assert Solution().maxProfit([100, 5, 25, 1, 20]) == 20, 'Tricky'
    print('all passed')


