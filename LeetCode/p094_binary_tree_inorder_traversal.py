# P094 Binary Tree Inorder Traversal
# Medium


# Given a binary tree, return the inorder traversal of its nodes' values.
# Follow up: Recursive solution is trivial, could you do it iteratively?

from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if not T.val:
                return 'N'

            s = str(T.val)
            if T.left and T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + layer(T.right, L + 1)
            elif T.left and not T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + 'N'
            elif not T.left and T.right:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L + 1)
            else:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'

        return layer(self)


def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    layers = []
    i, L = 0, 1
    while i != len(lst):
        layers.append(lst[i:i + L])
        i += L
        L *= 2
    pre_root = [TreeNode(i) for i in layers[0]]
    root_to_return = pre_root[0]

    for k in range(1, len(layers)):
        cur = [TreeNode(i) for i in layers[k]]
        for j in range(len(cur)):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0:
                pre_root[rt_idx].left = cur[j]
            else:
                pre_root[rt_idx].right = cur[j]
        pre_root = cur

    return root_to_return

class Solution:
    def traverseDirected(self, t, D='L'):
        """
        Directed traverse
        must be 'L' for left or 'R' for right
        return a flat List of values
        """
        if not t or t.val is None:
                                # Must write this way to avoid val=0
                                # Do not write 'not root.val'
            return [None]
        elif D == 'L':
            return [t.val] + self.traverseDirected(t.left, 'L') + self.traverseDirected(t.right, 'L')
        elif D == 'R':
            return [t.val] + self.traverseDirected(t.right, 'R') + self.traverseDirected(t.left, 'R')

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        pass



if __name__ == '__main__':
    t1 = genTree([1,None,2,None,None,3,None])
    print(Solution().traverseDirected(t1))


