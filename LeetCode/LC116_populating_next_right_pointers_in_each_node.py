"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
P116 Populating Next Right Pointers in Each Node
Medium

You are given a perfect binary tree where:
1. all leaves are on the same level
2. every parent has two children.

Note:
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
"""

class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __eq__(self, other):
        if self and other:
            return self.val == other.val and self.left == other.left and self.right == other.right and self.next == other.next
        return False





class Solution_A:
    def connect(self, root: Node) -> Node:
        all_layer = self.levelOrderTraversal(root)
        for nodes in all_layer:
            self.pointTo(nodes)
        return root


    def levelOrderTraversal(self, root):
        """
        Helper
        """
        if not root:
            return []
        result = []
        current = [root]
        while current:
            new_layer = []
            for node in current:
                if node.left and node.right:
                    new_layer.append(node.left)
                    new_layer.append(node.right)
            result.append(new_layer)
            current = new_layer
        return result

    def pointTo(self, node_lst):
        """
        Helper
        """
        if len(node_lst) > 1:
            i = 1
            while i != len(node_lst):
                prev = node_lst[i - 1]
                cur = node_lst[i]
                prev.next = cur
                i += 1


if __name__ == "__main__":
    testCase = Solution_A()

    A = Node(1,
             Node(2,
                  Node(4, None, None, None),
                  Node(5, None, None, None),
                  None),
             Node(3,
                  Node(6, None, None, None),
                  Node(7, None, None, None),
                  None),
             None)

    B = Node(1,
             Node(2,
                  Node(4, None, None, None),
                  Node(5, None, None, None),
                  None),
             Node(3,
                  Node(6, None, None, None),
                  Node(7, None, None, None),
                  None),
             None)

    B.left.next = B.right
    B.left.left.next = B.left.right
    B.left.right.next = B.right.left
    B.right.left.next = B.right.right

    assert testCase.connect(A) == B, "Example 1"

    print("All passed")
