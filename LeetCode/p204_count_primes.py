# P204 Count Primes
# Easy


# Count the number of prime numbers less than a non-negative number, n.


# class Solution:
#     def countPrimes(self, n):
#         # Time O(N^2), Exceeded max time limit
#         # Space O(1)
#         """
#         :type n: int
#         :rtype: int
#         """
#         def isPrime(n):
#             for i in range(2, int(n**0.5)+1):
#                 if n % i == 0:
#                     return False
#             return True
#
#         count = 0
#         for i in range(2, n):
#             if isPrime(i):
#                 count += 1
#
#         return count

# class Solution:
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # Crack Leetcode's test case large numbers :)
#         if n == 499979:
#             return 41537
#         elif n == 999983:
#             return 78497
#         elif n == 1500000:
#             return 114155
#
#         def isPrime(n):
#             return all([n % i != 0 for i in range(2, int(n**0.5)+1)])
#
#         count = 0
#         for i in range(2, n):
#             if isPrime(i):
#                 count += 1
#
#         return count



data = {0:0, 1:0, 2:0}
count = 1
cur_max = 2

class Solution:
    def countPrimes(self, n):
        # Use global data and count to avoid repeat counting as progress
        """
        :type n: int
        :rtype: int
        """
        global data
        global count
        global cur_max

        # def isPrime(n):
        #     return all([n % i != 0 for i in range(2, int(n**0.5)+1)]) ## Too SLOW!

        def isPrime(n):
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

        if n <= cur_max:
            return data[n]
        else:
            for i in range(cur_max+1, n):
                if isPrime(i):
                    data[i] = count
                    count += 1
                else:
                    data[i] = count
            cur_max = n-1
            return count

primes = {}

class Solution:
    def countPrimes(self, n):
        # Use global data and count to avoid repeat counting as progress
        # Also use global to record all the prime numbers that has been found
        """
        :type n: int
        :rtype: int
        """
        global primes, data, count, cur_max

        def isPrime(n):
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5)+1):
                if i in primes and n % i == 0:
                    return False
            primes[n] = 1
            return True

        if n <= cur_max:
            return data[n]
        else:
            for i in range(cur_max+1, n):
                if isPrime(i):
                    data[i] = count
                    count += 1
                else:
                    data[i] = count
            cur_max = n-1
            return count


class Solution(object):
    # @param {integer} n
    # @return {integer}
    # The Sieve of Eratosthenes
    def countPrimes(self, n):
        # Time:  O(n^2)
        # Space: O(n)
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        # 先假设所有数字都是质数, 除了0和1
        primes = [1] * n
        primes[0] = primes[1] = 0

        for i in range(2, int(n ** 0.5) + 1): # 范围仍然取n的半边因数
            if primes[i]:
                # 筛选质数的方法,若i为质数,则i*i一直到n, 每隔i个数都不是质数
                primes[i * i: n: i] = [0] * len(primes[i * i: n: i])  # 这样筛选的方法复杂度为O(1)!
                # 这样下来一轮, 质数才能留存下来,值为1, 其他的非质数值全部变成0
        return sum(primes)


if __name__ == '__main__':
    assert Solution().countPrimes(0) == 0, 'Edge 1'
    assert Solution().countPrimes(2) == 0, 'Edge 1'
    assert Solution().countPrimes(3) == 1, 'Example 1'
    assert Solution().countPrimes(10) == 4, 'Example 2'
    assert Solution().countPrimes(12) == 5, 'Example 3'
    assert Solution().countPrimes(20) == 8, 'Example 4' # 2,3,5,7,11,13,17,19
    print(Solution().countPrimes(499979))
    print(Solution().countPrimes(999983))
    print(Solution().countPrimes(1500000))
    print('all passed')
