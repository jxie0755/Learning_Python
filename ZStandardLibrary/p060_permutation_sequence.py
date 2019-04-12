# P060 Permutation Sequence
# Medium


# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# 1. "123"
# 2. "132"
# 3. "213"
# 4. "231"
# 5. "312"
# 6. "321"

# Given n and k, return the kth permutation sequence.

# Note:
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.

import timeit
import math
class Solution:
    def nextPermutation(self, nums):
        ### O(N), directly find next different permutations
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
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

    def prevPermutation(self, nums):
        ### O(N), directly find next different permutations
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
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

    ### This is basically the same as next permuation, with further implementation
    ### Direct implementation will fail because exceeded max time limit
    ### Optimization method is used to minimize the number of iteration on nextPermuete
    p_dict = {
        i: math.factorial(i) for i in range(1,10)
    }

    def getPermutation_0(self, n, k):
        lst = list(range(1, n + 1))
        for i in range(k-1):
            lst = self.nextPermutation(lst)
        return ''.join([str(i) for i in lst])

    def getPermutation_1(self, n, k):
        total_p = self.p_dict[n]

        if k == 1 or n == 1:
            lst = list(range(1, n + 1))
            return ''.join([str(i) for i in lst])
        elif k > total_p:  # 避免k太大                    # question noted that k will not be > n!
            return self.getPermutation(n, k % total_p)   # 取余数

        for i in range(n, 0, -1):
            p = self.p_dict[i]
            if k >= p:           # 检查是否k大于x级的排列数, 如果是, 则直接把后x部分直接逆序
                                 # 例如n=4有24种排列方式,而n=3只有6中,所以如果k=10的话:
                                 # 直接就从1432开始往后找10-6个next permuate就完成了
                lst = list(range(1, n - i + 1)) + list(range(n-i+1, n + 1))[::-1]
                if k > p:
                    new_k = k - p
                    for i in range(new_k):
                        lst = self.nextPermutation(lst)
                return ''.join([str(i) for i in lst])


    def getPermutation(self, n, k):
        ### Induce prevPermute to optimize
        ### Still fail in time limit!
        total_p = math.factorial(n)
        if k == 1 or n == 1:
            lst = list(range(1, n + 1))
            return ''.join([str(i) for i in lst])
        else:
            if total_p - k < k:
                lst = list(range(1, n + 1))[::-1]
                rev_k = total_p - k
                for i in range(rev_k):
                    lst = self.prevPermutation(lst)
            else:
                lst = list(range(1, n + 1))
                for i in range(k-1):
                    lst = self.nextPermutation(lst)
            return ''.join([str(i) for i in lst])


class Solution:
    ### recursive method, single and pure recursion
    def permute(self, nums):
        length = len(nums)
        if length == 1:
            return [[nums[0]]]
        else:
            result = []
            for i in nums:
                subList = nums[:]
                subList.remove(i)
                result += [[i] + per for per in self.permute(subList)]
            return result

    def getPermutation(self, n, k):
        ### use permute method from leetcode p046
        ### Fail even faster
        lst = list(range(1, n + 1))
        if k == 1 or n == 1:
            return ''.join([str(i) for i in lst])
        else:
            return ''.join(str(i) for i in self.permute(lst)[k-1])




if __name__ == '__main__':
    assert Solution().getPermutation(1,5) == '1', 'Edge 1'
    assert Solution().getPermutation(4,1) == '1234', 'Edge 2'

    assert Solution().getPermutation(3,3) == '213', 'Example 1'
    assert Solution().getPermutation(4,9) == '2314', 'Example 2'
    print(Solution().getPermutation(8, 29805)) # >>>  68327415
    print(Solution().getPermutation(9, 62716))  # >>>  265183794
    print('all passed')

    print('test timeit')
    # print(timeit.repeat('Solution().getPermutation_0(8, 6000)', setup='from __main__ import Solution', repeat=3, number=500))
    # # >>> [3.045518253785702, 3.04060806065978, 3.0435408311783467]
    # print(timeit.repeat('Solution().getPermutation(8, 6000)', setup='from __main__ import Solution', repeat=3, number=500))
    # # >>> [0.48771537433245093, 0.48776606102485154, 0.48719471292885963]
    # # 当k刚好略大于上一级n的时候, 会快很多, 但是其他情况下这样只能略微提速
    print('timeit ended')
