"""
There is a staircase with N steps and two platforms; one at the beginning, the other at the end of the stairs.
On each step a number is written (ranging from -100 to 100 with the exception of 0.) Zeros are written on both platforms.
You start going up the stairs from the first platform, to reach the top on the second one.
You can move either to the next step or to the next step plus one.
You must find the best path to maximize the sum of numbers on the stairs on your way up and return the final sum.

https://py.checkio.org/mission/stair-steps/
Input: Numbers on each stair as a list of integers.
Output: The final sum for the best way as an integer.
"""


def checkio(numbers):
    # 利用斐波那契数列方法,每走到n级都是从n-1级和n-2级过来的,那么只需要找走到n-1级和n-2级谁比较大就从谁那里走过来.
    # 然后依次递归到最小case

    def find_max(n):
        """

        Args:
            n: the index of numbers, (but with special cases)

        Returns: a number which is the max of possible sum

        """
        if n == -1:
            return 0  # 假设开头必须为0
        elif n == 0:
            return numbers[n]
        elif 0 < n < len(numbers):
            return max(find_max(n - 1), find_max(n - 2)) + numbers[n]
        elif n == len(numbers):
            return max(find_max(n - 1), find_max(n - 2)) + 0  # 假设结尾也必须是0

    return find_max(len(numbers))



# 其他算法
def checkio2(numbers):
    c = [0] * (len(numbers) + 1)
    c[1] = numbers[0]
    for i in range(2, len(numbers) + 1):
        c[i] = max(c[i - 1], c[i - 2]) + numbers[i - 1]

    return max(c[-1], c[-2])

# 其他算法
def checkio3(numbers):
    prevmax = curmax = 0
    for n in numbers + [0]:
        nextmax = max(curmax + n, prevmax + n)
        prevmax = curmax
        curmax = nextmax
    return curmax


if __name__ == "__main__":
    assert checkio([5, -3, -1, 2]) == 6, "1st test, (5-1+2=6)"
    assert checkio([5, 6, -10, -7, 4]) == 8, "2nd test, (5+6-7+4=8)"
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, "3rd test, (69+77+23+67+35+27+95=393)"
    assert checkio([1,-1,-10,-100,-50,-5000,-100,9999]) == 9840, "4th test, (1-10-50-100+9999=9840)"
    assert checkio([1, -1, -10, -100, -5000, -5, -100, 9999]) == 9894, "5th test, (1-1-100-5+9999=9894)"
    assert checkio([1, -1, -10, -100, -101, -101, -10, 9999]) == 9879, "6th test, (1-10-101-10+9999)"
    assert checkio([1, -1, -10, -500, -500, -500, -10, 9999]) == 9480, "7th test, (1-10-500-10+9999)"

    assert checkio([-1, -10, -100, -1000]) == -101, "-1-100"
    assert checkio([-1, -10, -100, -1000, -10000]) == -1010, "-10-1000"
    assert checkio([-1, -10, -100, -1000, -10000, -100000]) == -10101, "-1-100-10000"
    assert checkio([-1, -10, -100, -1000, -10000, -100000, -1000000]) == -101010, "-10-1000-100000"

    print("All ok")
