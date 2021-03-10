"""
https://leetcode.com/problems/unique-binary-search-trees/
LC096 Unique Binary Search Trees
Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""

from typing import *
from a0_TreeNode import *


class Solution_A1:
    def numTrees(self, n: int) -> int:
        """
        Use a helper to calculate based on actual list
        This will exceed time limit as list comprehension is time consuming
        """

        L = list(range(1, n+1))
        return self.numTreesHelper(L)


    def numTreesHelper(self, L:List[int]) -> int:
        if len(L) == 0:
            return 1
        elif len(L) == 1:
            return 1
        else:
            result = 0
            for rt in range(len(L)):
                prev = L[:rt]
                after = L[rt+1:]
                result += self.numTreesHelper(prev) * self.numTreesHelper(after)
            return result


class Solution_A2:
    def numTrees(self, n: int) -> int:
        """
        Similar idea based on A1, but just use abstract list (by length)
        No longer needs helper
        This will work but still exceed time limit
        """
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            result = 0
            for rt in range(1, n+1):
                prev = rt - 1
                after = n - rt
                result += self.numTrees(prev) * self.numTrees(after)
            return result


class Solution_A3:
    def numTrees(self, n: int) -> int:
        """
        Similar idea based on A1, but just use abstract list (by length)
        use Memorization Helper to expedite
        """
        def numTreesHelper(n: int) -> int:
            """
            Memorization helper
            """
            if n in hmp:
                return hmp[n]
            else:
                result = 0
                for rt in range(1, n + 1): # choose each point as the root
                    prev = rt - 1
                    after = n - rt
                    # the result is number of left side BST * right side BST (as combination)
                    result += numTreesHelper(prev) * numTreesHelper(after)
                hmp[n] = result
                return result

        hmp = {0: 1, 1: 1}
        return numTreesHelper(n)


class Solution_STD:
    """
    Dynamic Programming
    """
    def numTrees(self, n: int) -> int:

        # Dynamic list, idx is length of List (n)
        counts = [1, 1] # start with L=0, return 1, L=1, return 1.

        for idx_n in range(2, n + 1): # iterate from 2 to n
            count = 0
            for left in range(idx_n):
                count += counts[left] * counts[idx_n - left - 1]
                    # left side length * right side length
            counts.append(count) # progrssive extend counts to idx = n
        return counts[-1]


if __name__ == "__main__":
    testCase = Solution_A3()

    assert testCase.numTrees(3) == 5, "Example 1"
    assert testCase.numTrees(4) == 14, "Additional 1"
    assert testCase.numTrees(19) == 1767263190, "Long 1"

    print("All passed")
