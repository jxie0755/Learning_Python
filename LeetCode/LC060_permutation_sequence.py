"""
https://leetcode.com/problems/permutation-sequence/
P060 Permutation Sequence
Medium

The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
1 -> "123"
2 -> "132"
3 -> "213"
4 -> "231"
5 -> "312"
6 -> "321"

Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
"""

from typing import *
import math


class Solution_A:
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


class Solution_B:

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
        Directly pick kth permuation
        Faster but still failed, and high Space Complexity
        """
        lst = list(range(1, n + 1))
        if k == 1 or n == 1:
            return "".join([str(i) for i in lst])
        else:
            return "".join(str(i) for i in self.permute(lst)[k - 1])




class Solution_C1(object):
    """
    01 -> "1234"  --- x=1, 1! = 1, last 1 digit (4) is reversely sorted, the first 3 digit (123) is sorted
    02 -> "1243"  --- x=2, 2! = 2, last 2 digit (43) is reversely sorted, the first 2 digit (12) is sorted
    03 -> "1324"    |
    04 -> "1342"  --- when in between, the last x=2 digit rotate permute with one digit move up everytime
    05 -> "1423"    |
    06 -> "1432"  --- x=3, 3! = 6, last x digit (432) is reversely sorted, the first 1 digit (1) is sorted
    07 -> "2134"   |
    08 -> "2143"   |
    09 -> "2314"   |
    10 -> "2341"   |
    11 -> "2413"   |
    12 -> "2431"   |
    13 -> "3124"   |
    14 -> "3142"   |
    15 -> "3214" ___ when in between, the last x=3 digit rotate permute with one digit move up everytime
    16 -> "3241"   |
    17 -> "3412"   |
    18 -> "3421"   |
    19 -> "4123"   |
    20 -> "4132"   |
    21 -> "4213"   |
    22 -> "4231"   |
    23 -> "4312"   |
    24 -> blank  --- x=4, 4! = n!, end
    """

    def getPermutation(self, n: int, k: int) -> str:
        """
        Direct generation, digit by digit
        这里利用的是每一位数字, 都会因为后面位数x的总排列数(x!)为循环发生变化, 从小到大发展
        """
        result, k= "", k - 1  # k = k-1 因为一开始算一个,所以要去掉
        candidates = list(range(1, n + 1))

        for i in (range(n-1, -1, -1)): # 迭代,从n-1一直到0, 仍是n次,每次算出一位数字
            fact = math.factorial(i)    # 这个数字后面, 剩余位数的所有排列数目
            curr = candidates.pop(k // fact)  # 这一步很关键, 找出fact被循环了几次
                        # 用pop去掉已经排出来的数字, 因为此后的迭代这个数字不参与其中
            result += str(curr)
            k %= fact
        return result


class Solution_C2(object):

    def getPermutation(self, n: int, k: int) -> str:
        """
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
                fact = math.factorial(length-1)
                digit = nums.pop(k // fact)
                return str(digit) + helper(nums, k % fact)

        lst = list(range(1, n + 1))
        return helper(lst, k - 1)  # k - 1原理同上


if __name__ == "__main__":
    testCase = Solution_C1()
    assert testCase.getPermutation(4, 1) == "1234", "Edge 1"
    assert testCase.getPermutation(3, 3) == "213", "Example 1"
    assert testCase.getPermutation(4, 9) == "2314", "Example 2"
    assert testCase.getPermutation(8, 29805) == "68327415", "Long 1"
    assert testCase.getPermutation(9, 62716) == "265183794", "Long 2"
    print("All passed")

    # print("test timeit")
    # print(timeit.repeat("testCase.getPermutation_0(8, 6000)", setup="from __main__ import Solution", repeat=3, number=500))
    # >>> [3.045518253785702, 3.04060806065978, 3.0435408311783467]
    # print(timeit.repeat("testCase.getPermutation(8, 6000)", setup="from __main__ import Solution", repeat=3, number=500))
    # >>> [0.48771537433245093, 0.48776606102485154, 0.48719471292885963]
    # 当k刚好略大于上一级n的时候, 会快很多, 但是其他情况下这样只能略微提速
    # print("timeit ended")
