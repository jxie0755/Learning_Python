"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
P107 Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
"""

from a0_TreeNode import *


class Solution_A:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        Show the tree layer by layer from top to bottom
        This will omit None nodes
        Refer to LC102
        Use the levelOrderTraversal operation but the maximum time limit is exceeded
        """
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]]

        return self.levelOrderTraversal(root)[::-1]

    def levelOrderTraversal(self, root: TreeNode) -> List[List[int]]:
        """
        Helper function from LC102
        Omit None nodes
        """
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)

                # omit None by checking left tand right None
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)

        return result

testCase = Solution_A()
A = genTree([
    0,
    2, 4,
    1, None, 3, -1,
    5, 1, None, None, 6, None, 8, None
])
testCase.levelOrderBottom(A)


class Solution_STD:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        STD ans
        Almost the same way as I tried, but it does not add None to next layer
        Use i.left and i.right to screen each node in current layer and only add the branch to next layer if the branch exist
        """
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                if node:
                    vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)

        return result[::-1]


class Solution_STD_2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        A more structed stack method accoding to STD method
        First build up the stack all the way to the bottom to get nodes at each layer
        Then extract the values of each node in every layer
        """
        if root is None:
            return []

        stack = [[root]]
        current = [root]
        while current:
            next_level = []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            stack.append(next_level)
            current = next_level

        result = []
        for i in stack[-2::-1]:
            vals = []
            for node in i:
                if node:
                    vals.append(node.val)
            result.append(vals)

        return result


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert testCase.levelOrderBottom(T0) == [], "Edge 0"

    T1 = genTree([1])
    assert testCase.levelOrderBottom(T1) == [[1]], "Edge 1"

    T2 = genTree([
        3,
        9, 20,
        None, None, 15, 7
    ])

    assert testCase.levelOrderBottom(T2) == [
        [15, 7],
        [9, 20],
        [3]
    ], "Example 1"

    T3 = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, None, 6, None, 8, None])

    assert testCase.levelOrderBottom(T3) == [
        [5, 1, 6, 8],
        [1, 3, -1],
        [2, 4],
        [0]
    ], "Additional 1"

    print("All passed")
