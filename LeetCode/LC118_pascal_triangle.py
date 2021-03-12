"""
https://leetcode.com/problems/pascals-triangle/
LC118 Pascal's triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

from typing import *

class Solution_A:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Iteration method
        generate next layer based on the current last layer
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            result = [[1]]
            layer = [1, 1]
            for i in range(numRows - 1):
                result.append(layer)
                new_layer = [1]
                for j in range(len(layer) - 1):
                    new_layer.append(layer[j] + layer[j + 1])
                new_layer.append(1)
                layer = new_layer
            return result



if __name__ == "__main__":
    testCase = Solution_A()

    assert testCase.generate(0) == [
    ], "Edge 0"

    assert testCase.generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ], "Example 1"

    assert testCase.generate(1) == [
        [1]
    ], "Example 2"

    print("All passed")
