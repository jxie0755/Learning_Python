# P264 Ugly Number II
# Medium

# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Note:
# 1 is typically treated as an ugly number.
# n does not exceed 1690.


import heapq

class Solution(object):

    # Version A, Abandoned
    # Use prime sieves to get all the prime numbers
    # Then sieve again with prime numbers > 2,3,5
    def primesunder(self, n):
        sieve = list(range(0, 1+n))

        for i in range(2,int(n**0.5)+1):
            if sieve[i]: # 注意这里可以省很多计算时间
                for k in range(i*i, len(sieve), i):
                    sieve[k] = 0

        sieve[1] = 0
        sieve[2] = 0
        sieve[3] = 0
        sieve[5] = 0
        return list(filter(lambda x:bool(x), sieve))

    def nthUglyNumber(self, n: int) -> int:

        # choose factor wisely:
        # primes must cover all the primes bigger than nth ugly number
        # And after sieving, there should be more than n items left in the sieve
        # This leads to a huge factor of sieve, caused the algorithm taking too long to calculate
        # Therefore, this is not a good way, abandon this method
        sieve_size = 1000*n
        sieve = list(range(sieve_size))
        primes = self.primesunder(sieve_size)
        # print('prime list', primes)

        for i in primes:
            if sieve[i]:
                for k in range(i, len(sieve), i):
                    sieve[k] = 0

        sieve = list(filter(lambda x:bool(x), sieve))
        # print('n is', n, 'sieve length:', len(sieve))
        # print('final sieve:', sieve)
        return sieve[n-1]


class Solution(object):
    # Self version B Dynamic programming
    # Same idea in P264, P279
    # Exceed max time limit
    def nthUglyNumber(self, n: int) -> int:
        result = [1]

        while len(result) < n:
            temp = float('inf')
            for i in result:
                for p in [2, 3, 5]:
                    sample = i * p
                    if temp > sample > result[-1]:
                        temp = sample
                        break
            result.append(temp)
        return result[-1]



##########################################################################################
class Solution(object):

    # STD ans A
    # Get all UG number within 32bit, and sorted....
    ugly = []
    a = 1
    maxx = 2**31 # 32 bit max Integer
    while a < maxx:
        b = a
        while b < maxx:
            c = b
            while c < maxx:
                ugly.append(c)
                c *= 5
            b *= 3
        a *= 2

    ugly = sorted(ugly)
    # 只生成一次list, 往后可以直接调用这个list

    def nthUglyNumber(self, n: int) -> int:
        return self.ugly[n-1]



class Solution(object):

    # STD ans B
    # generate a table
    # https://www.youtube.com/watch?v=ZG86C_U-vRg
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0

        while len(ugly) < n:
            candidates = [ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5]
            minimum = min(candidates)
            ugly.append(minimum)
            if minimum == candidates[0]:
                i2 += 1
            if minimum == candidates[1]:
                i3 += 1
            if minimum == candidates[2]:
                i5 += 1
        return ugly[-1]

class Solution(object):

    # STD ans C
    # Need to use heapq
    def nthUglyNumber(self, n: int) -> int:
        ugly_number = 0
        heap = [1]
        for _ in range(n):
            print(heap)
            ugly_number = heapq.heappop(heap)
            if ugly_number % 2 == 0:
                heapq.heappush(heap, ugly_number * 2)
            elif ugly_number % 3 == 0:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
            else:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
                heapq.heappush(heap, ugly_number * 5)

        return ugly_number



Solution().nthUglyNumber(10)

# if __name__ == '__main__':
#     assert Solution().nthUglyNumber(1) == 1, 'Edge'
#     assert Solution().nthUglyNumber(2) == 2, 'Example 1'
#     assert Solution().nthUglyNumber(6) == 6, 'Example 2'
#     assert Solution().nthUglyNumber(7) == 8, 'Example 3'
#     assert Solution().nthUglyNumber(10) == 12, 'Example 4'
#     assert Solution().nthUglyNumber(11) == 15, 'Example 5'
#
#     assert Solution().nthUglyNumber(80) == 800, 'Long 1'
#     assert Solution().nthUglyNumber(1690) == 2123366400, 'End'
#     print('all passed')
#
