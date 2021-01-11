# P241 Different Ways to Add Parentheses
# Medium


# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

from typing import *


# General functional functions
def calculate(A, B, op):
    """
    calculate A op B
    A and B are int
    op is operator in string
    """

    if op == "+":
        return A + B
    elif op == "-":
        return A - B
    elif op == "*":
        return A * B


def read(input):
    """
    read input and return two list:
    nums and operators
    """
    nums = []
    op = []

    temp = ""
    for i in input:
        if i.isnumeric():
            temp += i
        else:
            nums.append(int(temp))
            temp = ""
            op.append(i)

    nums.append(int(temp))  # last number

    return nums, op


class Solution:

    # Version A, Permutation method
    # Read nums and operator, and calculate all possible operator permutations
    # This could fail becaues the iteration will repeat remote parenthesis as two methods
    def diffWaysToCompute(self, input: str) -> List[int]:

        if not input:
            return []

        nums, op = read(input)

        if len(nums) == 1:
            return [nums[0]]

        result = []

        def helper(nums, op):
            """
            nums is a list of integers
            op is a list of operators
            """
            # print(nums, op)
            if len(op) == 1:
                calc_result = calculate(nums[0], nums[1], op[0])
                result.append(calc_result)
                # print(result)
            else:
                for i in range(len(op)):
                    new_nums = nums[:]
                    new_op = op[:]
                    new_nums[i] = calculate(new_nums[i], new_nums.pop(i + 1), new_op.pop(i))
                    helper(new_nums, new_op)

        helper(nums, op)
        return sorted(result)


class Solution:

    # Version B, similar idea with A but new method on adding parenthesis
    # Passed efficiently
    # 添加括号的规律:
    # 1. 有几次运算, 最终就必须有几组括号, 其实只管右半边, 也就是")"
    # 2. 直到第1个运算符后面, 最多只能有1个")", 推理: 直到第n个运算符, 最多只能有"n"个
    # 3. 添加括号后, 所有之后的运算符index发生位移
    # 4. 需要统计之前用了多少个括号(used), 才能了解根据目前第n个运算符最多需要几个, 也就是0个到n-used个
    # 5. 所以递归算法, 必须要指定插入位置, 之前有多少个")"用过了, 和还剩多少个, 因为只要任何时刻用完全部就结束了
    def diffWaysToCompute(self, input: str) -> List[int]:

        # Edge empty
        if not input:
            return []

        # Read input
        nums, op = read(input)

        # Edge single number, no operator
        if not op:
            return [nums[0]]

        all_op = []  # All possible ways to add parenthesis
        max_idx = len(op)  # record the number of parenthesis to be added

        def helper(op, idx, used, rest, count):

            if count == max_idx:  # 这里也就是到最后一个运算符, 不过剩多少, 都全加到末尾, 然后输出
                op += [")"] * rest
                all_op.append(op)
            else:
                for i in range(0, count + 1 - used):  # 注意range范围, 从0开始, 最多只能用当前位置减去此前用过的数量个')"
                    new_op = op[:idx] + [")"] * i + op[idx:]
                    helper(new_op, idx + i + 1, used + i, rest - i, count + 1)  # 递归的时候, 推进下一个idx注意位移插入了i个")"

        helper(op, 1, 0, max_idx, 1)

        # 这个就是简单的队列实现运算式, 通过遇到")"来激发运算, 用pop来保持其他顺序不变
        def calc(nums, op_p):
            i = 0
            while i != len(op_p):
                cur = op_p[i]
                if cur == ")":
                    op_p.pop(i)
                    operator = op_p.pop(i - 1)
                    nums[i - 1] = calculate(nums[i - 1], nums.pop(i), operator)
                    i -= 1  # 注意这里不但pop了")", 也pop了上一个运算符, 所以后退了两位, 天然只能前进一位,所以还需要退一位来补下一个元素的idx
                else:
                    i += 1

            return nums[0]

        result = []
        for op_p in all_op:
            result.append(calc(nums[:], op_p))

        return sorted(result)


if __name__ == "__main__":
    assert Solution().diffWaysToCompute("") == [], "Edge 0"
    assert Solution().diffWaysToCompute("1") == [1], "Edge 1"
    assert Solution().diffWaysToCompute("1+1") == [2], "Edge 2"

    assert Solution().diffWaysToCompute("2-1-1") == [0, 2], "Example 1"
    assert Solution().diffWaysToCompute("2*3-4*5") == [-34, -14, -10, -10, 10], "Example 2"

    assert Solution().diffWaysToCompute("10+11+12") == [33, 33], "Double digit"
    assert Solution().diffWaysToCompute("15*1*4") == [60, 60], "Copycat"

    print("All passed")
