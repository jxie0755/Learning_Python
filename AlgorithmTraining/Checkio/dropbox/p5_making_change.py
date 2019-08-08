"""
When making purchases, Nicola would like to use the minumum number of coins possible.
For example, Outer Leftopia has coins with denomination 1, 3, and 5 shillings.

Input: Two arguments. The first argument is an int: the price of the purchase. The second is a list of ints: the denominations of available coins.
Output: int. The minimum number of coins Nicola can use to make the purchase. If the price cannot be made with the available denominations, return None.
"""

import itertools

# Brutal force
def checkio(price, coins):
    # 为每个面值得到coin数目范围
    drange = list(map(lambda x: price // x, coins))

    # 将范围内所有面值的价值总结成一个matrix
    rangelist = [[coins[x] * i for i in range(drange[x] + 1)] for x in range(len(drange))]

    # 利用笛卡尔乘积将所有能够加起来等于price的组合挑选出来
    candidates = []
    for i in itertools.product(*rangelist):
        if sum(i) == price:
            candidates.append(i)

    # 为每个candidate得到每个硬币需要的个数, 然后计算总和
    result = []
    for i in candidates:
        temp = 0
        for j in range(len(coins)):
            temp += i[j] // coins[j]
        result.append(temp)

    if len(result) > 0:
        return min(result)


# Idea from Leetcode P279
# Dynamic Programing and memorization
def checkio(price, coins):

    num = [0]
    # num represents number of coins needed for a value ( value = numbers of coins, idex of num is the value)
    # for example [0,3,5]  means, need 0 coins for 0, need 3 coins for value 1, and need 5 coins for value 2
    #              0 1 2
    while len(num) <= price:
        temp = []
        for i in coins:
            if i <= len(num):
                temp.append(num[-i])  # -i就是表示刚好差i面值的那个price的最优值
            else:
                temp.append(float("inf"))

        if temp:
            num.append(min(temp) + 1)

    ans = num[-1]
    return ans if ans != float("inf") else None


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert not checkio(3, [4, 5]), "Edge 1"
    assert not checkio(15, [6, 7]), "Edge 2"

    assert checkio(8, [1, 3, 5]) == 2, "Example 1, 3+5"
    assert checkio(12, [1, 4, 5]) == 3, "Example 2, 4+4+4"
    assert checkio(123456, [1, 6, 7, 456, 678]) == 187, "Big number, 4+4+4"
    print("Done")

