"""Definition of a binary tree node."""

from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val is None:
                return "N"

            s = str(T.val)
            if T.left and T.right:
                return s + "\n" + "  " * L + layer(T.left, L + 1) + "\n" + "  " * L + layer(T.right, L + 1)
            elif T.left and not T.right:
                return s + "\n" + "  " * L + layer(T.left, L + 1) + "\n" + "  " * L + "N"
            elif not T.left and T.right:
                return s + "\n" + "  " * L + "N" + "\n" + "  " * L + layer(T.right, L + 1)
            else:
                return s + "\n" + "  " * L + "N" + "\n" + "  " * L + "N"

        return layer(self)

    def __eq__(self, other):
        if not self and not other:
            return True
        elif not self or not other:
            return False
        else:
            return self.val == other.val and self.left == other.left and self.right == other.right

    # fix the unhashable issue with __eq__ method enabled
    def __hash__(self):
        return hash(id(self))


def genTree(lst: List[int], i: int = 1) -> TreeNode:
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if i <= len(lst) and lst[i - 1] is not None:
        node = TreeNode(lst[i - 1])
        node.left = genTree(lst, i * 2)
        node.right = genTree(lst, i * 2 + 1)
        return node


if __name__ == "__main__":
    print("\nEmpty Tree:")
    print(genTree([]))

    print("\nSingle node Tree:")
    print(genTree([1]))

    print("\nComplicated Tree:")
    print(genTree([1, 2, 3, None, 4, 5, None]))
