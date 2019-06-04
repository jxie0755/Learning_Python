# p121 Best Time to Buy and Sell Stock
# Easy

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.


class Solution:
    def maxProfit(self, prices):
        # This method exceeded max time limit :(
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
        # This method still exceeded max time limit :(
        # 折断法, 以list中最小值做切割
        profits = [0]
        while prices:
            low = min(prices)
            low_n = prices.index(low)
            profit = max(prices[low_n:]) - low
            profits.append(profit)
            prices = prices[:low_n]

        return max(profits)

    def maxProfit_r(self, prices):
        # 折断法, 递归来做
        if not prices:
            return 0
        else:
            low = min(prices)
            low_n = prices.index(low)
            profit = max(prices[low_n:]) - low
            return max(profit, self.maxProfit_r(prices[:low_n]))

    def maxProfit(self, prices):
        # filter the list first, to only obtain the turn points, combine with 折断法
        # first part is O(N), Second part is also O(N), so overall O(N).
        # Accepted
        if len(prices) == 0 or len(prices) == 1:
            return 0

        turn_points = [prices[0]] # keep the head
        i = 0
        while i != len(prices) - 2:
            current, next, further = prices[i], prices[i+1], prices[i+2]
            if next == max(current, next, further) or next == min(current, next, further):
                turn_points.append(next)
            i += 1

        turn_points += [prices[-1]] # keep the tail

        # 结合折断法, 以list中最小值做切割
        profits = [0]
        while turn_points:
            low = min(turn_points)
            low_n = turn_points.index(low)
            profit = max(turn_points[low_n:]) - low
            profits.append(profit)
            turn_points = turn_points[:low_n]

        return max(profits)

    def maxProfit_best(self, prices):
        # STD ans
        # Best method evaluate on the run
        max_profit, min_price = 0, float("inf")
                                    # 无穷大
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

    def maxProfit(self, prices):
        # according to the best method, Denis modified for clearer logic
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
        # 此题本质就是迭代刷新最低价,
        # 然后得到最低价之后的(当前价-最低价)得到一个利润, 然后基于此最低价寻找更高的利润
        # 若出现新的最低价, 那么就从新的最低价开始重新寻找新的利润并与之前的最高利润做对比


if __name__ == '__main__':
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5, 'Smart trader'
    # Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

    assert Solution().maxProfit([7,6,4,3,1]) == 0, 'No Transaction'
    # In this case, no transaction is done, i.e. max profit = 0

    assert Solution().maxProfit([100, 5, 25, 1, 20]) == 20, 'Tricky'

    print('all passed')
