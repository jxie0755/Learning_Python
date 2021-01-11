# P367 Valid Perfect Square
# Easy


# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.

class Solution:

    # Iteration of sqrt, O(Sqrt(N))
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num + 1):
            if i * i == num:
                return True
            elif i * i > num:
                break
        return False


class Solution(object):

    # STD ans
    # Time:  O(logn)
    # Space: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (right + left) // 2
            if mid >= num // mid:
                right = mid - 1
            else:
                left = mid + 1

        return left == num // left and num % left == 0


if __name__ == "__main__":
    assert Solution().isPerfectSquare(1), "Edge 1"
    assert Solution().isPerfectSquare(16), "Example 1"
    assert not Solution().isPerfectSquare(14), "Example 2"
    assert not Solution().isPerfectSquare(2147483647), "Long"
    print("All passed")
