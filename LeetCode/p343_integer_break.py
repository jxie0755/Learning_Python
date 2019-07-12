# P343 Integer Break
# Medium


# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

# Note: You may assume that n is not less than 2 and not larger than 58.


class Solution:

    # the idea is to break them into k part and mathmatically they need to be as close as to each other
    # then compare all of them
    # O(N)
    def integerBreak(self, n: int) -> int:

        best_so_far = 1

        for k in range(2, n):
            base, remain = divmod(n, k)
            if remain == 0:
                prod = (n // k) ** k
            else:
                prod = (n // k) ** (k-remain)
                for _ in range(remain):
                    prod *= (n // k) + 1

            if prod > best_so_far:
                best_so_far = prod

        return best_so_far


class Solution2(object):

    # STD ans
    # Time:  O(logn), pow is O(logn).
    # Space: O(1)
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        #  Proof.
        #  1. Let n = a1 + a2 + ... + ak, product = a1 * a2 * ... * ak
        #      - For each ai >= 4, we can always maximize the product by:
        #        ai <= 2 * (ai - 2)
        #      - For each aj >= 5, we can always maximize the product by:
        #        aj <= 3 * (aj - 3)
        #
        #     Conclusion 1:
        #      - For n >= 4, the max of the product must be in the form of
        #        3^a * 2^b, s.t. 3a + 2b = n
        #
        #  2. To maximize the product = 3^a * 2^b s.t. 3a + 2b = n
        #      - For each b >= 3, we can always maximize the product by:
        #        3^a * 2^b <= 3^(a+2) * 2^(b-3) s.t. 3(a+2) + 2(b-3) = n
        #
        #     Conclusion 2:
        #      - For n >= 4, the max of the product must be in the form of
        #        3^Q * 2^R, 0 <= R < 3 s.t. 3Q + 2R = n
        #        i.e.
        #          if n = 3Q + 0,   the max of the product = 3^Q * 2^0
        #          if n = 3Q + 2,   the max of the product = 3^Q * 2^1
        #          if n = 3Q + 2*2, the max of the product = 3^Q * 2^2

        if n % 3 == 0:            #  n = 3Q + 0, the max is 3^Q * 2^0
            return 3 ** (n // 3)
        elif n % 3 == 2:          #  n = 3Q + 2, the max is 3^Q * 2^1
            return 3 ** (n // 3) * 2
        else:                     #  n = 3Q + 4, the max is 3^Q * 2^2
            return 3 ** (n // 3 - 1) * 4



if __name__ == "__main__":

    assert Solution().integerBreak(2) == 1, "Example 1, 1+1, 1*1=1"
    assert Solution().integerBreak(10) == 36, "Example 2, 3+3+4, 3*3*4=36"
    assert Solution().integerBreak(17) == 486, "Example 2, 3+3+4, 3*3*4=36"


    print("all passed")

