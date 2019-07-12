# P116 Populating Next Right Pointers in Each Node
# Medium

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# Definition for a Node.
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


# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
from typing import *

class Solution:
    def showLayers(self, root):
        if not root:
            return []
        result = [[root]]
        layer = [root]
        while layer:
            new_layer = []
            for i in layer:
                if i.left and i.right:
                    new_layer.append(i.left)
                    new_layer.append(i.right)
            result.append(new_layer)
            layer = new_layer
        return result

    def pointTo(self, node_lst):
        if len(node_lst) > 1:
            i = 1
            while i != len(node_lst):
                prev = node_lst[i-1]
                cur = node_lst[i]
                prev.next = cur
                i += 1

    def connect(self, root: Node) -> Node:
        all_layer = self.showLayers(root)
        for nodes in all_layer:
            self.pointTo(nodes)
        return root


if __name__ == "__main__":

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

    assert Solution().connect(A) == B, "Example 1"
    print("all passed")
