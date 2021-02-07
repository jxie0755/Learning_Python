"""
https://leetcode.com/problems/same-tree/
p100 Same Tree
Easy


Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Note:
Mirrored trees are considered not the same
Circular trees can not be tested
"""

from a0_TreeNode import *


class Solution_A:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and \
        self.isSameTree(p.left, q.left) and \
        self.isSameTree(p.right, q.right)



if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    T00 = None
    T000 = TreeNode(5)

    assert testCase.isSameTree(T0, T00) == True, "Edge 0"
    assert testCase.isSameTree(T0, T000) == False, "Edge 1"
    assert testCase.isSameTree(T00, T000) == False, "Edge 2"

    T1 = genTree([
        1,
        2, 3
    ])
    T2 = genTree([
        1,
        2, 3
    ])
    assert testCase.isSameTree(T1, T2) == True, "Example 1"

    T3 = genTree([
        1,
        2, 3,
        4, None, None, None
    ])
    T4 = genTree([
        1,
        3, 2,
        4, None, None, None
    ])
    assert testCase.isSameTree(T3, T4) == False, "Example 2"

    T5 = genTree([
        1,
        2, 3,
        None, 4, 5, None
    ])

    T6 = genTree([
        1,
        2, 3,
        None, 4, 5, None
    ])
    assert testCase.isSameTree(T5, T6) == True, "Additional 1"

    print("All passed")
