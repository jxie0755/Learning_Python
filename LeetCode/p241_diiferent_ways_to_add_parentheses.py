# P241 Different Ways to Add Parentheses
# Medium


# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        pass



if __name__ == '__main__':
    assert Solution().diffWaysToCompute("") == [], 'Edge 0'
    assert Solution().diffWaysToCompute("1") == [1], 'Edge 1'
    assert Solution().diffWaysToCompute("1+1") == [2], 'Edge 2'


    assert Solution().diffWaysToCompute("2-1-1") == [0, 2]
    assert Solution().diffWaysToCompute("2*3-4*5") == [-34, -14, -10, -10, 10]

    print('all passed')
