"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
LC117 Populating Next Right Pointers in Each Node II
Medium

Different from LC106: You are given a non-perfect binary tree.

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
            return self.val == other.val and \
                   self.left == other.left and \
                   self.right == other.right and \
                   self.next == other.next
        elif not self and not other:
            return True
        else:
            return False


class Solution_A:
    def connect(self, root: Node) -> Node:
        """
        Combine levelOrderTraversal idea from LC102
        """
        if root:
            current = [root]

            while current:
                # modification: link next to right side
                for lidx in range(len(current) - 1):
                    current[lidx].next = current[lidx + 1]

                new_layer = []
                for node in current:
                    # since it is not perfect bianry tree, checking left and right will be separated
                    if node.left:
                        new_layer.append(node.left)
                    if node.right:
                        new_layer.append(node.right)

                current = new_layer
        return root


if __name__ == "__main__":
    testCase = Solution_A()

    A = Node(1,
             Node(2,
                  Node(4, None, None, None),
                  Node(5, None, None, None),
                  None),
             Node(3,
                  None,
                  Node(7, None, None, None),
                  None),
             None)

    B = Node(1,
             Node(2,
                  Node(4, None, None, None),
                  Node(5, None, None, None),
                  None),
             Node(3,
                  None,
                  Node(7, None, None, None),
                  None),
             None)


    B.left.next = B.right
    B.left.left.next = B.left.right
    B.left.right.next = B.right.right

    assert testCase.connect(A) == B, "Example 1"
    print("All passed")
