"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
P111 Minimum Depth of Binary Tree
Easy


Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

from a0_TreeNode import *


class Solution_A:
    def minDepth(self, root: TreeNode) -> int:
        """
        Similar to LC102
        levelOrderTraversal to find the depth when the first leaf is found
        """
        if not root:
            return 0

        layer = [root]
        depth = 1
        while layer:
            new_layer = []
            for node in layer:
                if self.isLeaf(node):  # modified to return
                    return depth

                # omit None by checking left tand right None
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)

            layer = new_layer
            depth += 1

        return depth

    def isLeaf(self, root: TreeNode) -> bool:
        """
        Helper
        The key is to find the first leaf
        """
        if root and not root.left and not root.right:
            return True
        return False


class Solution_STD:
    def minDepth(self, root: TreeNode) -> int:
        """
        Critcal factor is to determine a leaf
        """
        if root is None:  # end node not a leaf
            return 0
        if root.left and root.right:  # not a leaf, both side is valid node, find the min()
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:  # if at least one side is None, then go for the other side with Max()
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert testCase.minDepth(T0) == 0, "Edge 0"

    T1 = TreeNode(1)
    assert testCase.minDepth(T1) == 1, "Edge 1"

    T2 = genTree([
        3,
        9, 20,
        None, None, 15, 7
    ])
    assert testCase.minDepth(T2) == 2, "Example 1"

    T3 = genTree([
        2,
        None, 3,
        None, None, None, 4,
        None, None, None, None, None, None, None, 5,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6
    ])
    assert testCase.minDepth(T3) == 5, "Example 2"

    T4 = genTree([
        1,
        2, None
    ])
    assert testCase.minDepth(T4) == 2, "Additional 1"

    print("All passed")
