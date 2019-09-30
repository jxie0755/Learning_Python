"""
https://leetcode.com/problems/permutation-sequence/
P060 Permutation Sequence
Medium

The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
"""


import timeit
from typing import *
import math


class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        """
        Helper from Leetcode P031
        O(N), directly find next different permutations
        """
        length = len(nums)
        cur_i = None

        for i in range(-2, -length - 1, -1):
            if nums[i] < nums[i + 1]:
                cur_i = i
                break

        if not cur_i:
            nums[:] = nums[::-1]  # 直接结束,因为本身是倒着排序的,返回正排序即可
        else:
            for rev_i in range(-1, cur_i, -1):
                if nums[rev_i] > nums[cur_i]:
                    nums[cur_i], nums[rev_i] = nums[rev_i], nums[cur_i]  # switch
                    nums[cur_i + 1:] = nums[cur_i + 1:][::-1]
                    break
        return nums

    def prevPermutation(self, nums: List[int]) -> List[int]:
        """
        Helper developped from Leetcode P031
        O(N), directly find next different permutations
        """
        length = len(nums)
        cur_i = None

        for i in range(-2, -length - 1, -1):
            if nums[i] > nums[i + 1]:
                cur_i = i
                break

        if not cur_i:
            nums[:] = nums[::-1]  # 直接结束,因为本身是倒着排序的,返回正排序即可
        else:
            for rev_i in range(-1, cur_i, -1):
                if nums[rev_i] < nums[cur_i]:
                    nums[cur_i], nums[rev_i] = nums[rev_i], nums[cur_i]  # switch
                    nums[cur_i + 1:] = nums[cur_i + 1:][::-1]
                    break
        return nums


    def getPermutation_A1(self, n: int, k: int) -> str:
        """
        Version A
        Direct permutate to k, failed as exceed time limit
        """
        lst = list(range(1, n + 1))
        for i in range(k - 1):
            lst = self.nextPermutation(lst)
        return "".join([str(i) for i in lst])

    # This is basically the same as next permuation, with further implementation
    # Optimization method is used to minimize the number of iteration on nextPermuete

    def getPermutation_A2(self, n: int, k: int) -> str:
        """
        Version A2
        Simple optimization to just to one-round of permuation if k is bigger than total p.
        Also skip nn permutations, if k > nn! where nn < n
        Failed as exceed time limit
        """
        # Create a dict to calculation all number of permutation for n in 1 to 9.
        p_dict = {i: math.factorial(i) for i in range(1, 10)}
        total_p = p_dict[n]

        if k == 1 or n == 1:
            lst = list(range(1, n + 1))
            return "".join([str(i) for i in lst])

        elif k > total_p:  # 避免k太大   # question noted that k will not be > n! So this is unecessary
            return self.getPermutation_A2(n, k % total_p)  # 取余数

        for i in range(n, 0, -1):
            p = p_dict[i]
            if k >= p:  # 检查是否k大于x级的排列数, 如果是, 则直接把后x部分直接逆序
                # 例如n=4有24种排列方式,而n=3只有6中,所以如果k=10的话:
                # 直接就从1432开始往后找10-6=4个next permuate就完成了
                lst = list(range(1, n - i + 1)) + list(range(n - i + 1, n + 1))[::-1]
                if k > p:
                    new_k = k - p
                    for i in range(new_k):
                        lst = self.nextPermutation(lst)
                return "".join([str(i) for i in lst])

    def getPermutation_A3(self, n: int, k: int) -> str:
        """
        Induce prevPermute to optimize
        Still fail in time limit!
        """
        total_p = math.factorial(n)
        if k == 1 or n == 1:
            lst = list(range(1, n + 1))
            return "".join([str(i) for i in lst])
        else:
            if total_p - k < k:
                lst = list(range(1, n + 1))[::-1]
                rev_k = total_p - k
                for i in range(rev_k):
                    lst = self.prevPermutation(lst)
            else:
                lst = list(range(1, n + 1))
                for i in range(k - 1):
                    lst = self.nextPermutation(lst)
            return "".join([str(i) for i in lst])


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Helper from Leetcode P46 version D
        Get all permuation in a list, recursive method, single and pure recursion
        """
        length = len(nums)
        if length == 1:
            return [nums]
        else:
            result = []
            for i in nums:
                subList = nums[:]
                subList.remove(i)
                result += [[i] + per for per in self.permute(subList)]
            return result

    def getPermutation(self, n: int, k: int) -> str:
        """
        Version B
        Directly pick kth permuation
        Faster but still failed, and high Space Complexity
        """
        lst = list(range(1, n + 1))
        if k == 1 or n == 1:
            return "".join([str(i) for i in lst])
        else:
            return "".join(str(i) for i in self.permute(lst)[k - 1])


class Solution(object):
    def getPermutation(self, n: int, k: int) -> str:
        """
        Version C1
        Direct generation, digit by digit
        这里利用的是每一位数字, 都会因为后面位数的总排列数为循环发生变化, 从小到大发展
        """
        fact_dict = {i: math.factorial(i) for i in range(n)} # 注意这里i从0开始到n-1, 因为不算第一位, 只计算从第二位开始有多少种排列方式
        seq, k, fact = "", k - 1, fact_dict[n-1]  # k = k-1 因为一开始算一个,所以要去掉
        perm = list(range(1, n + 1))

        for i in reversed(range(n)):
            fact = fact_dict[i]
            curr = perm[k // fact]
            seq += str(curr)
            perm.remove(curr)  # 这一步很关键, 去掉已经排出来的数字, 因为此后的迭代这个数字不参与其中
            k %= fact
        return seq


class Solution(object):

    def getPermutation(self, n: int, k: int) -> str:
        """
        Version C2
        Direct generation, digit by digit
        recursive method
        """

        def helper(nums: List[int], k: int) -> str:
            """
            A helper function for recursion
            """
            length = len(nums)
            if length == 1:
                return str(nums[0])
            else:
                fact = fact_dict[length - 1]
                digit = nums[k // fact]
                nums.remove(digit)
                return str(digit) + helper(nums, k % fact)

        fact_dict = {i: math.factorial(i) for i in range(n)}
        lst = list(range(1, n + 1))
        return helper(lst, k - 1)  # k - 1原理同上


if __name__ == "__main__":
    assert Solution().getPermutation(4, 1) == "1234", "Edge 1"
    assert Solution().getPermutation(3, 3) == "213", "Example 1"
    assert Solution().getPermutation(4, 9) == "2314", "Example 2"
    assert Solution().getPermutation(8, 29805) == "68327415", "Long 1"
    assert Solution().getPermutation(9, 62716) == "265183794", "Long 2"
    print("all passed")

    # print("test timeit")
    # print(timeit.repeat("Solution().getPermutation_0(8, 6000)", setup="from __main__ import Solution", repeat=3, number=500))
    # >>> [3.045518253785702, 3.04060806065978, 3.0435408311783467]
    # print(timeit.repeat("Solution().getPermutation(8, 6000)", setup="from __main__ import Solution", repeat=3, number=500))
    # >>> [0.48771537433245093, 0.48776606102485154, 0.48719471292885963]
    # 当k刚好略大于上一级n的时候, 会快很多, 但是其他情况下这样只能略微提速
    # print("timeit ended")
