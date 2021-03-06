"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
P114 Flatten Binary Tree to Linked List
Medium

Given a binary tree, flatten it to a linked list in-place.

Notes:
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""
from a0_TreeNode import *


class Solution_A:
    def flatten(self, root: TreeNode) -> None:
        """
        Use a preOrderTraversal helper to keep the TreeNode in order
        Then assign to a dumb head to the right with iteration
        """
        dumb = TreeNode(0)

        for node in self.preOrderTraversalNodes(root):
            dumb.right = node
            dumb = dumb.right
            dumb.left = None  # clear the left side

    def preOrderTraversalNodes(self, root: TreeNode) -> List[TreeNode]:
        """
        Modified preOrder traversal to get nodes instead of the values
        """
        if not root:
            return []
        return [root] + self.preOrderTraversalNodes(root.left) + self.preOrderTraversalNodes(root.right)


class Solution_STD:
    def flatten(self, root: TreeNode) -> None:
        """
        Run in-place with a helper
        """
        self.flattenRecu(root, None)

    def flattenRecu(self, root, list_head: TreeNode) -> TreeNode:
        """
        Helper function
        """
        if not root:
            return list_head

        list_head = self.flattenRecu(root.right, list_head) # -> list_head = root.right
        list_head = self.flattenRecu(root.left, list_head)  # link root.left -> root.right, return root.left
        root.right = list_head  # link root -> root.left
        root.left = None

        return root


if __name__ == "__main__":
    testCase = Solution_STD()

    T0 = None
    testCase.flatten(T0)
    assert not T0, "Edge 0"

    T1 = TreeNode(0)
    testCase.flatten(T1)
    assert T1 == T1, "Edge 1"

    T2 = TreeNode(1)
    testCase.flatten(T2)
    assert T2 == T2, "Edge 11"

    T3 = genTree([
        1,
        2, 5,
        3, 4, None, 6
    ])
    testCase.flatten(T3)
    assert T3 == genTree([
        1,
        None, 2,
        None, None, None, 3,
        None, None, None, None,None, None, None, 4,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6
    ]), "Example 1"

    T4 = genTree([
        1,
        2,3
    ])
    testCase.flatten(T4)
    assert T4 == genTree([
        1,
        None, 2,
        None, None, None, 3
    ]), "Addtional 1"

    print("All passed")
