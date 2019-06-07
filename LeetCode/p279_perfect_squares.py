# P279 Perfect Squares
# Medium


# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
from typing import *

class Solution(object):

    # Version A
    # Direct divmod method will not work as perfect sq numbers are not overlapping like (1,2,4,8)
    # Recursive method to get all break down
    # This will work but too slow and exceed time limit
    def SQlist(self, n):
        """find all possible square number up to n"""
        result = []
        for i in range(1, n+1):
            if i**2 <= n:
                result.append(i ** 2)
            else:
                break
        return result


    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []
        sqlist = self.SQlist(n)

        def helper(n, bl=[]):
            if sum(bl) == n:
                result.append(bl)

            elif sum(bl) < n:
                for i in sqlist:
                    new_bl = bl[:]
                    new_bl.append(i)
                    helper(n, new_bl)

        helper(n)
        return len(min(result, key=len))


class Solution(object):

    # Version B
    # Use multiply by adding element, instead of pure addition
    # create a list to indicate how many square number from 1 to n
    # This is EVEN SLOWER!
    def SQlist(self, n):
        """find all possible square number up to n"""
        result = []
        for i in range(1, n + 1):
            if i ** 2 <= n:
                result.append(i ** 2)
            else:
                break
        return result

    def summ(self, sqlist, multlist):
        """
        calculate the sum of sqlist by
        sum(sqlist[i]*explist[i])
        must len(sqlist) == len(multlist)
        """
        i = 0
        ans = 0
        while i != len(sqlist):
            ans += sqlist[i] * multlist[i]
            i += 1
        return ans

class Solution:
    def numSquares(self, n: int) -> int:
        result = []

        # Two list will be equal length
        sqlist = self.SQlist(n)
        multlist = [0] * len(sqlist)
        N = len(sqlist)
        def helper(n, ml):
            current_sum = self.summ(sqlist, ml)
            if current_sum == n:
                result.append(sum(ml))

            elif current_sum < n:
                for i in range(N):
                    new_ml = ml[:]
                    new_ml[i] += 1
                    helper(n, new_ml)

        helper(n, multlist)
        return min(result)




class Solution(object):

    # Version C, Similar to Version A but with optimiazation (trimming)
    def SQlist(self, n):
        """find all possible square number up to n"""
        result = []
        for i in range(int(n**0.5), 0, -1):
                result.append(i ** 2)
        return result

    def numSquares(self, n: int) -> int or float:
        result = [float('inf')]
        sqlist = self.SQlist(n)

        def helper(n, sum_so_far=0, length_so_far=0):
            print(sum_so_far, length_so_far)
            if sum_so_far == n:
                result.append(length_so_far)

            # Only proceed tree recursive if current bl beats smallest length so far
            elif sum_so_far < n and length_so_far < min(4, result[-1]): # 利用4平方和原理, 最大不超过4
                for i in sqlist:
                    new_sum = sum_so_far + i
                    new_length = length_so_far + 1
                    helper(n, new_sum, new_length)

        helper(n)
        return result[-1]


class Solution(object):

    # STD and
    # dynamic + memorization
    # 根据硬币组合的动态规划思路, 但是建立一张表, index表示n, index位置的值表示n的最优解
    # 动态规划时,通过反向跳跃-i^2来找到 n - squarenumber, 很有特色
    # 从n=1一直计算到target n, 同时建立一个memorization, 这样递归分叉时可以避免重复计算, 精妙!
    def numSquares(self, n: int) -> int:
        num = [0]

        while len(num) <= n:
            temp = []
            for i in range(1, int(len(num) ** 0.5 + 1)):
                temp.append(num[-i*i])
            num.append(min(temp) + 1)

        return num[n]

class Solution(object):

    # Version D, Improved recursion with memorization
    # This will run very quickly, but reach to maximum depth of recursion
    def SQlist(self, n):
        """find all possible square number up to n"""
        result = []
        for i in range(1, int(n**0.5)+1):
                result.append(i ** 2)
        return result

    def numSquares(self, n: int) -> int or float:

        sqlist = self.SQlist(n)
        hashmap = {}  # memorization

        def helper(n):

            if n == 0: # base case
                return 0

            elif n in hashmap: # 如果之前算过, 就直接从字典调用
                return hashmap[n]

            else:
                temp = []
                for i in sqlist:
                    if i <= n:
                        temp.append(helper(n-i))
                hashmap[n] = min(temp) + 1  # 返回之前记录结果
                return min(temp) + 1

        return helper(n)

class Solution(object):

    # Version D2, Improved recursion with memorization and depth control
    # This is much faster but still fail the max time limit
    def SQlist(self, n):
        """find all possible square number up to n"""
        result = []
        for i in range(1, int(n**0.5)+1):
                result.append(i ** 2)
        return result

    def numSquares(self, n: int) -> int or float:

        sqlist = self.SQlist(n)
        hashmap = {}  # memorization

        def helper(n, depth=0):
            if n == 0: # base case
                return 0

            elif n in hashmap and depth < 4: # 如果之前算过, 就直接从字典调用
                return hashmap[n]

            elif depth < 4:
                temp = []
                for i in sqlist:
                    if i <= n:
                        new_depth = depth + 1
                        temp.append(helper(n-i, new_depth))

                temp_n = min(temp) + 1
                if temp_n != float('inf'):  # 字典只记录真实值
                    hashmap[n] = temp_n  # 返回之前记录结果
                return temp_n
            else:
                return float('inf')  # 由于只走4层深度, 所以超过四层按无穷大来算,避免被min计算进去

        ans = helper(n)
        return ans


if __name__ == '__main__':
    assert Solution().numSquares(1) == 1, 'Edge, just 1'
    assert Solution().numSquares(7) == 4, ' Example 1:  4+1+1+1'
    assert Solution().numSquares(12) == 3, 'Example 2:  4+4+4'
    assert Solution().numSquares(13) == 2, 'Example 3:  4+9'
    assert Solution().numSquares(18) == 2, 'Example 4:  9+9'
    assert Solution().numSquares(19) == 3, 'Example 5:  9+9+1'

    assert Solution().numSquares(43) == 3, 'Example 6:  25+9+9'
    assert Solution().numSquares(67) == 3, 'Example 7:  9+9+49'
    assert Solution().numSquares(99) == 3, 'Example 8:  49+25+25'
    assert Solution().numSquares(143) == 4, 'Example 9'
    assert Solution().numSquares(488) == 2, 'Example 10'

    print('all passed')

    import time
    start_time = time.time()
    print(Solution().numSquares(7168))
    print(f"--- {time.time() - start_time}s seconds ---\n")



