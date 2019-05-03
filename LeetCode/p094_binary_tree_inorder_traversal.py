# P094 Binary Tree Inorder Traversal
# Medium


# Given a binary tree, return the inorder traversal of its nodes' values.
# 中序遍历就是二叉树的平面投影,从左到右
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
    ### Recursive method
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root or root.val is None:
            # Must write this way to avoid val=0
            # Do not write 'not root.val'
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)




class Solution(object):
    # STD ans
    # Morris Traversal Solution
    # Time:  O(n)
    # Space: O(1)
    # TODO to learn

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



if __name__ == '__main__':
    t0 = None
    assert Solution().inorderTraversal(t0) == []

    t1 = genTree([1,None,2,None,None,3,None])
    assert Solution().inorderTraversal(t1) == [1,3,2]

    print('all passed')




