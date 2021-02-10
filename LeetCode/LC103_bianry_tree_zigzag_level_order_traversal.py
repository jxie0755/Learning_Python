"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
P103 Binary Tree Zigzag Level Order Traversal
Medium


Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
"""


from a0_TreeNode import *


class Solution_A:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.levelOrderTraversal_zigzag(root)


    def levelOrderTraversal_zigzag(self, root: TreeNode) -> List[List[int]]:
        """
        Helper function
        Modified from LC102, use the levelOrderTraversal (modified version) to solve the problem
        """
        if root is None:
            return []

        result, layer = [], [root]
        REV = False # label for reverse order
        while layer:
            next_layer, node_vals = [], []

            for node in layer:
                node_vals.append(node.val)

                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            layer = next_layer

            if REV:
                result.append(node_vals[::-1])
            else:
                result.append(node_vals)

            REV = not REV  # flip every turn

        return result




if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert testCase.zigzagLevelOrder(T0) == [

    ], "Edge 0"

    T1 = genTree([1])
    assert testCase.zigzagLevelOrder(T1) == [
        [1]
    ], "Edge 1"

    T2 = genTree([3, 9, 20, None, None, 15, 7])
    assert testCase.zigzagLevelOrder(T2) == [
        [3],
        [20, 9],
        [15, 7],
    ], "Example 1"

    T3 = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, None, 6, None, 8, None])

    assert testCase.zigzagLevelOrder(T3) == [
        [0],
        [4, 2],
        [1, 3, -1],
        [8, 6, 1, 5],
    ], "Additional 1"

    print("All passed")
