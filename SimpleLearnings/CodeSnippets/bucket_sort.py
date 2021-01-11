"""
基于Leetcode P041
学习一下桶排序,和其简单实现


桶排序(Bucket sort)是一种基于计数的排序算法
工作的原理是将数据分到有限数量的桶子里，然后每个桶再分别排序（有可能再使用别的排序算法或是以递回方式继续使用桶排序进行排序）。
当要被排序的数据内的数值是均匀分配的时候，桶排序时间复杂度为Θ(n)。
桶排序不同于快速排序，并不是比较排序，不受到时间复杂度 O(nlogn) 下限的影响

桶排序，主要适用于小范围整数数据，且独立均匀分布，可以计算的数据量很大，而且符合线性期望时间。
                        * 不一定要连续,但是一定要分布均匀

"""

from typing import *


def bucket_sort_continous(nums: List[int]) -> None:
    """
    Bucket sort with any interger array (evenly distributed)
    Sort in-place, no extra space needed
    Time = O(N)
    """
    n = len(nums)
    if n > 1:
        max_v, min_v = max(nums), min(nums)
        bucket_width = (max_v - min_v) / (n - 1)  # 求出公差
        idx = 0
        while idx < n:  # while里面那句话执行的总次数最大就是nums的长度。一旦一个数字被放对位置,则不会再被移动,所以最多只能交换nums长度次数
            bucket_idx = int((nums[idx] - min_v) / bucket_width)  # 通过公差将值转换成正确的排序idx
            if 0 < bucket_idx <= n and nums[idx] != nums[bucket_idx]:  # 交换两者
                A = nums[idx]
                B = nums[bucket_idx]
                nums[bucket_idx] = A
                nums[idx] = B
            else:  # 连续性调换,直到每个排序正确为止
                idx += 1


if __name__ == "__main__":
    q0 = []
    bucket_sort_continous(q0)
    assert q0 == [], "Edge 0"

    q0 = [1]
    bucket_sort_continous(q0)
    assert q0 == [1], "Edge 1"

    q0 = [5]
    bucket_sort_continous(q0)
    assert q0 == [5], "Edge 2"

    q1 = [1, 3, 5, 7, 9]
    bucket_sort_continous(q1)
    assert q1 == [1, 3, 5, 7, 9], "Odd array 0"

    q1 = [7, 9, 1, 5, 3]
    bucket_sort_continous(q1)
    assert q1 == [1, 3, 5, 7, 9], "Odd array 1"

    q1 = [9, 7, 5, 3, 1]
    bucket_sort_continous(q1)
    assert q1 == [1, 3, 5, 7, 9], "Odd array 2"

    q1 = [5, 7, 1, 9, 3]
    bucket_sort_continous(q1)
    assert q1 == [1, 3, 5, 7, 9], "Odd array 3"

    q2 = [2, 5, 8, 11]
    bucket_sort_continous(q2)
    assert q2 == [2, 5, 8, 11], "Even array 0"

    q2 = [11, 8, 5, 2]
    bucket_sort_continous(q2)
    assert q2 == [2, 5, 8, 11], "Even array 0"

    q2 = [8, 11, 2, 5]
    bucket_sort_continous(q2)
    assert q2 == [2, 5, 8, 11], "Even array 0"

    q2 = [5, 2, 8, 11]
    bucket_sort_continous(q2)
    assert q2 == [2, 5, 8, 11], "Even array 0"

    print("bucket_sort_continous all passed")


def bucket_sort(nums: List[int]) -> None:
    """
    Bucket sort with any interger array none continous
    Sort in-place, but take extra space to generate buckets
    Time = O(N)
    """
    n = len(nums)
    if n > 1:
        max_v, min_v = max(nums), min(nums)

        buckets = [0 for _ in range(max_v - min_v + 1)]  # 通过限定buckets长度节省空间,而不是单纯用n
        for i in nums:
            buckets[i - min_v] += 1

        bucket_idx = 0
        nums_idx = 0
        while nums_idx < n:
            while buckets[bucket_idx] != 0:
                val = bucket_idx + min_v
                nums[nums_idx] = val
                nums_idx += 1
                buckets[bucket_idx] -= 1
            bucket_idx += 1


if __name__ == "__main__":
    q0 = []
    bucket_sort(q0)
    assert q0 == [], "Edge 0"

    q0 = [1]
    bucket_sort(q0)
    assert q0 == [1], "Edge 1"

    q0 = [5]
    bucket_sort(q0)
    assert q0 == [5], "Edge 2"

    q1 = [1, 3, 5, 7, 9]
    bucket_sort(q1)
    assert q1 == [1, 3, 5, 7, 9], "Odd array 0"

    q1 = [7, 9, 1, 5, 3]
    bucket_sort(q1)
    assert q1 == [1, 3, 5, 7, 9], "Odd array 1"

    q2 = [2, 5, 8, 11]
    bucket_sort(q2)
    assert q2 == [2, 5, 8, 11], "Even array 0"

    q2 = [11, 8, 5, 2]
    bucket_sort(q2)
    assert q2 == [2, 5, 8, 11], "Even array 0"

    q3 = [4, 1, 4, 1, 4]
    bucket_sort(q3)
    assert q3 == [1, 1, 4, 4, 4], "Uneven 1"

    q3 = [4, 1, 4, 1]
    bucket_sort(q3)
    assert q3 == [1, 1, 4, 4], "Uneven 2"

    q3 = [4, 1, 4, 1, 5, 1]
    bucket_sort(q3)
    assert q3 == [1, 1, 1, 4, 4, 5], "Uneven 3"

    print("bucket_sort all passed")
