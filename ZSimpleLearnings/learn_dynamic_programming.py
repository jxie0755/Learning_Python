# Dynamic Programming Summary
# 动态规划
# Multiple sources

from typing import *

# Q1:
print("\nQ1: 间隔最大和")
# 有n个正整数, 排成一列, 可重复, 选取一些数,两两不相邻, 但是总和最大
# 例如:
A = [1,2,3,2,1,5,7,6]
# 分解成多个小问题:
# F(A) = max(F[A:-2] + A[7], F[A:-1])

# Recursive method
def foo_recur(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return max(foo_recur(lst[:-2]) + lst[-1], foo_recur(lst[:-1]))

print(foo_recur(A))
# >>> 15

# Non-recursive method
def foo_iter(lst):
    sum_so_far = [0, lst[0]]  # 逐个记录到达list每个长度的最大可能性, 然后拓展下一个

    for i in range(1, len(lst)):
        sum_so_far.append(max(sum_so_far[-1], lst[i]+sum_so_far[-2]))
    return sum_so_far[-1]

print(foo_iter(A))
# >>> 15




# Q2:
print("\nQ2: 找零钱")
# 找零钱的问题, 总金额n, 有m种硬币面值, 各有无限多个数, 问最少需要几个硬币?

# Recursive
# 递归法是倒着处理, 把大的case变成小的case, 这样分叉太多影响速度
# 可以用memorization记录, 避免重复计算
def change_recur(target: int, coins: List[int]):
    """coins are sorted from small to large"""

    memory = {}

    def helper(target):

        if target == 0:
            return 0
        elif 0 < target < coins[0]:
            return float('inf')  # so that this is not possible be selected by min()

        elif target in memory:
            return memory[target]

        else:
            ans = min([helper(target-i) + 1 for i in coins if i <= target])
            memory[target] = ans
            return ans

    return helper(target)

# Non recursive
# 非递归法, 是从小的case积累变成大的case, 这样就有效减少了重复运算
def change_iter(price, coins):

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
                temp.append(float('inf'))
        num.append(min(temp) + 1)

    ans = num[-1]
    return ans if ans != float('inf') else None


print(change_recur(12, [1, 4, 5]))
# >>> 3 (4 * 3)

print(change_recur(55, [1, 3, 7]))
# >>> 9 (7*7 + 3*2)

print(change_recur(15, [6, 7]))
# >>> None

# big case does not work in recursion: maximum depth issue
print(change_iter(123456, [1, 6, 7, 456, 678]))
# >>> 187

# 以上两题可以总结出, 递归是把大case化成n个小case, 一直化解到最basic case, 然后再反推回来
# 而非递归方法就是, 避免拆解大case, 而是直接从最小的case开始, 一步一步推导出更大的case的最优值, 这样就避免了分叉递归的重复计算
# 所以非递归方法最常见的就是建立一个list, 记录下来1到n的所有最优解, 从而推导出n+1的最优解, 实现用一个线性推进, 结合具体判断最优解的方法复杂度,来实现低复杂度



# https://zhuanlan.zhihu.com/p/31628866
# 漫画动态递归

# Q1 上楼梯
print('\nQ1: 上楼梯')

# 有一座高度是10级台阶的楼梯，从下往上走，每跨一步只能向上1级或者2级台阶。要求用程序来求出一共有多少种走法。

# 递归法, 走到第n步的方法数等于到n-1步方法数+ 到n-2步方法数
def stair_recur(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stair_recur(n-1) + stair_recur(n-2)

print(stair_recur(10))
# >>> 89


# 非递归, 动态规划
def stair_iter(n):
    steps = [0,1,2]  # 同理, 代表了走index步的步数
    for i in range(3, n+1):
        steps.append(steps[-1]+steps[-2])
    print(steps)
    return steps[-1]
print(stair_iter(10))
# >>> 89



# Q2 国王和金矿

