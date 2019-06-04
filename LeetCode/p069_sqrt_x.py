# p069 Sqrt(x)
# Easy

# Implement int sqrt(int x).
#  Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.


class Solution:
    # DO not use the straight high-low method, because it will return float number incorrectly to be integerized.
    # Handle the integer method from the begining
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        high, low = x, 1
        temp_result= (high + low) / 2
        while abs(temp_result** 2 - x) >= 1:
            if temp_result**2 > x:
                high = temp_result
            elif temp_result**2 < x:
                low = temp_result

            temp_result = (high + low) / 2

        temp_result = int(temp_result)
        if (temp_result+1)**2 > x:
            return temp_result
        else:
            return temp_result+1



    def mySqrt2(self, x):
        # A modified binary search:
        left, right = 1, x
        while True:
            middle = int((left + right) / 2)
            if middle * middle <= x and (middle + 1) * (middle + 1) > x:
                return middle
            elif middle * middle > x:
                right = middle
            else:
                left = middle


    def mySqrt3(self, x):
        # Cheating by use python internal function
        return int(x ** 0.5)

if __name__ == '__main__':
    assert Solution().mySqrt(0) == 0
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(36) == 6
    assert Solution().mySqrt(2147395600) == 46340
    print('all passed')
