# P098 Validate Binary Search Tree
# Medium


# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:
    # The left subtree of a node contains only nodes with keys less than the node's key.
    # The right subtree of a node contains only nodes with keys greater than the node's key.

# Both the left and right subtrees must also be binary search trees.

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

    ### Use inorderTraversal to get the list from Leetcode P094
    ### Then filter the None out from the list and check if the list is sorted
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    result.append(curr.val)
                    node.right = None
                    curr = curr.right

        return result


    def isValidBST(self, root: TreeNode) -> bool:
        flat = list(filter(lambda x:x is not None, self.inorderTraversal(root)))

        if not flat or flat[0] is None:
            return True

        for i in range(1, len(flat)):
            if flat[i] <= flat[i-1]:
                return False
        return True



if __name__ == '__main__':
    A = genTree([2,1,3])
    assert Solution().isValidBST(A), 'Example 1'

    A = genTree([
        5,
        1, 4,
        None, None, 3, 6
    ])

    assert not Solution().isValidBST(A), 'Example 2'

    A = genTree([
        5,
        1, 6,
        None, None, 3, 7
    ])
    assert not Solution().isValidBST(A), 'Additional'

    A = genTree([0, None, -1])
    assert not Solution().isValidBST(A), 'Additional'

    print('all passed')
