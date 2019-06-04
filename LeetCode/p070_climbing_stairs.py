# p070 Climbing Stairs
# Easy

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


    def climbStairs(selfself, n):
        # it is essentially fibonacci method:
        a, b = 0, 1
        for x in range(n+1):
            a, b = b, a + b  # 必须是同排,这样会调用上一次的a,b值,a值不会由于a=b后改变!
        return a

    # 解释为什么跟fibbonaci关联: 假设有n级楼梯, 可以走到n-1级的方式数x, 可以走到n-2级的方式数y.
    # 因为当走到n-1时,只剩一种走法到n,所以本质上每一种走到n-1的方法数也就是走到n的方法数.
    # 而另一种方式则是走到n-2,跳过n-1直接到n,也是只有一种方法(跳两步),所以有多少走到n-2的方法就有多少种从这里跳两步到n.
    # 所以结果就是 x + y, 本质上就是斐波那契数列

if __name__ == '__main__':
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(7) == 21
    print('passed')
