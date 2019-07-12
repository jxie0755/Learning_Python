# P313 Super Ugly Number
# Medium

# Write a program to find the nth super ugly number.
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.



# Note:
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

from typing import *

class Solution:

    # Version A 动态规划
    # 做一个堆栈把1-nth全部计算, 每次都把栈中每个值依次乘以primes里, 如果对于最后一个值就保留, 小于就留下
    # Exceed max time limit...
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        result = [1]
        while len(result) < n:
            temp = float("inf")
            for i in result:
                for p in primes:
                    sample = i * p
                    if temp > sample > result[-1]:
                        temp = sample
                        break
            result.append(temp)
        print(result)
        return result[-1]


class Solution(object):

    # Version B, idea borrowed from Leetcode P264 STD ans B
    # Table method
    # Passed but slow
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        pN = len(primes)
        e_stack = [0] * pN

        while len(ugly) < n:
            candidates = [ugly[e_stack[i]] * primes[i] for i in range(pN)]
            minimum = min(candidates)
            ugly.append(minimum)

            for k in range(pN):
                if candidates[k] == minimum:
                    e_stack[k] += 1

        return ugly[-1]


class Solution(object):

    # STD ans
    # Time:  O(n * k)
    # Space: O(n + k)
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [0] * n
        uglies[0] = 1
        ugly_by_prime = list(primes)
        idx = [0] * len(primes)

        for i in range(1, n):
            uglies[i] = min(ugly_by_prime)
            # print(uglies, "uglies[i]", uglies[i])
            for k in range(len(primes)):
                # print("k", k, "ugly_by_prime[k]", ugly_by_prime[k])
                if uglies[i] == ugly_by_prime[k]:
                    idx[k] += 1
                    ugly_by_prime[k] = primes[k] * uglies[idx[k]]

        return uglies[-1]


import heapq
class Solution(object):

    # Heap solution. (620ms)
    # Time:  O(n * k)
    # Space: O(n + k)
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []

        uglies = [0] * n
        uglies[0] = 1

        idx = [0] * len(primes)
        ugly_by_last_prime =[0] * n


        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))

        for i in range(1, n):
            uglies[i], k = heapq.heappop(heap)
            ugly_by_last_prime[i] = k
            idx[k] += 1
            while ugly_by_last_prime[idx[k]] > k:
                idx[k] += 1
            heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))

        return uglies[-1]



if __name__ == "__main__":
    assert Solution().nthSuperUglyNumber(12, [2,7,13,19]) == 32, "Example 1"
    assert Solution().nthSuperUglyNumber(800, [37,43,59,61,67,71,79,83,89,97,101,103,113,127,131,157,163,167,173,179,191,193,197,199,211,229,233,239,251,257]) == 411811, "Long"

    print("all passed")
