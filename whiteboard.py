"""
https://leetcode.com/problems/climbing-stairs/
p070 Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# 解释为什么跟fibbonaci关联: 假设有n级楼梯, 可以走到n-1级的方式数x, 可以走到n-2级的方式数y.
# 因为当走到n-1时,只剩一种走法到n,所以本质上每一种走到n-1的方法数也就是走到n的方法数.
# 而另一种方式则是走到n-2,跳过n-1直接到n,也是只有一种方法(跳两步),所以有多少走到n-2的方法就有多少种从这里跳两步到n.
# 所以结果就是 x + y, 本质上就是斐波那契数列
"""


class Solution_A:
    def climbStairs(self, n: int) -> int:
        pass


if __name__ == "__main__":
    testCase = Solution()
    assert testCase.climbStairs(1) == 1, "Edge 1"
    assert testCase.climbStairs(2) == 2, "Example 1"
    assert testCase.climbStairs(3) == 3, "Example 2"
    assert testCase.climbStairs(7) == 21, "Long"
    print("passed")
