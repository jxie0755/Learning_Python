"""
Dynamic Programming Summary
动态规划
Multiple sources
"""

from typing import *

# https://www.bilibili.com/video/av47420469/
print("From https://www.bilibili.com/video/av47420469/")
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
            return float("inf")  # so that this is not possible be selected by min()

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
                temp.append(float("inf"))
        num.append(min(temp) + 1)

    ans = num[-1]
    return ans if ans != float("inf") else None


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

"""https://zhuanlan.zhihu.com/p/31628866"""
# Q1 上楼梯
print("\nQ1: 上楼梯")

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
print("\nQ2: 国王和金矿")
# 有一个国家发现了5座金矿，每座金矿的黄金储量不同，需要参与挖掘的工人数也不同pair(man, gold)。
# 参与挖矿工人的总数是10人。
# 每座金矿要么全挖，要么不挖，不能派出一半人挖取一半金矿。
# 要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取哪几座金矿？
# 也就是如何合理分配有限的劳动力, 来实现最大化


# 暴力法, 寻找所有C(A,k)组合, k in range(1, len(A)), 在所有组合中, sum(man) <= 10中找最大的sum, 得到金矿pair
# 方法略


# 动态规划
# 第一解,根据所需人数来遍历到达目标人数, 假设只有1个人, 找到最优解, 然后再加一个人, 再获得新的最优解
A = [[5, 400], [5, 500], [3, 200], [4, 300], [3, 350]]
def golddig_by_man(lst, man_total):
    """
    lst: A list of gold, formed with pars of total gold value and man count needed
    man_n: total man count limit
    """

    def sum_gold(goldmine_lst):
        return sum(k[1] for k in goldmine_lst)

    # 开始规划, 若是只有man_n - 1个人怎么办?
    gold = [[[0, 0]]]  # represents whhich gold mine to dig if there is idx number of man, starting from [0,0] (zero man, zero gold)

    for total_man in range(1, man_total + 1): # iterate man_total from 1 to man_total
        temp = []

        for gm in lst: # check each gold mine avaible
            gm_man_need = gm[0]
            man_extra = total_man - gm_man_need

            # 第一条件, 如果要找i个人最佳,必须保证,当前的检查的金矿需要的人数k[0]不能超过当前拥有的人数i
            if man_extra >= 0:
                prev = gold[man_extra] # 多出来那部分人的最优解从之前的最优解中找

                # 第二条件: 必须保证这个金矿(需要x人) 没有在此前的(i-x)那个最佳选法之中
                if gm not in prev:
                    temp.append(gold[man_extra] + [gm])

        if temp: # 如果有金矿能满足上两个条件, 则在备选中选一个最大金总和的选法
            gold.append(max(temp, key=sum_gold))
        else: # 如果不满足, 说明多出来的一个人, 没有更好的安放方式, 所以它的最佳就是total-1一样, 浪费了一个人
            gold.append(gold[-1])

    return gold[-1][1:] # 返回第man_total个最佳, 不需要包括[0,0]

print("\n金矿第一解:")
print(golddig_by_man(A, 10))
# >>> [[5, 500], [5, 400]]



# 第二解, 根据金矿数目来遍历而到达当前金矿获得最优解
A = [[5, 400], [5, 500], [3, 200], [4, 300], [3, 350]]
def golddig_by_man(lst, man_total):
    """
    lst: A list of gold, formed with pars of total gold value and man count needed
    man_n: total man count limit
    """

    def sum_gold(goldmine_lst):
        return sum(k[1] for k in goldmine_lst)

    gold = []
    for gm in lst:  # 从1个金矿到n个金矿(n为lst全部金矿)
        temp = [[[0,0]]]  # temp最终变成一个len(man_total)+1的长度, 通过index指示几个人时,i个
        man_need, val = gm[0], gm[1]
        for k in range(1, man_total+1): # 打表, 记录i个金矿时,如果有k个人应该选哪个金矿
            if not gold: # 第一行
                if k < man_need: # 如果人不够挖矿
                    temp.append([[0,0]])
                else:
                    temp.append([gm])
            else:
                option1 = gold[-1][k] # 上一行k个人, 也就是放弃此矿
                option2 = gold[-1][k-man_need] + [gm] if k-man_need >= 0 else [[0,0]]  # 上一行k-man_need个人 + 此矿, 选最优解
                temp.append(max([option1, option2], key=sum_gold))
        gold.append(temp)

    # To see the full table:
    # for line in gold:
    #     print(line)
    return gold[-1][-1]


# 扩展问题, 此上二法复杂度为O(m*n), m=金矿数, n=人数
# 若n比较大, 导致m*n大于2^m, 则不如用递归来的容易!

print("\n金矿第二解:")
print(golddig_by_man(A, 10))
