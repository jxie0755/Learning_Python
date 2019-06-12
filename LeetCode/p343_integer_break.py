# P343 Integer Break
# Medium


# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

# Note: You may assume that n is not less than 2 and not larger than 58.


class Solution:

    # the idea is to break them into k part and mathmatically they need to be as close as to each other
    # then compare all of them
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



if  __name__ == '__main__':
    assert Solution().integerBreak(2) == 1, 'Example 1, 1+1, 1*1=1'
    assert Solution().integerBreak(10) == 36, 'Example 2, 3+3+4, 3*3*4=36'
    assert Solution().integerBreak(17) == 486, 'Example 2, 3+3+4, 3*3*4=36'


    print('all passed')

