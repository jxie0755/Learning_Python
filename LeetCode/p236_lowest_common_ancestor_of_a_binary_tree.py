# P235 Lowest Common Ancestor of a Binary Tree
# Medium

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Version A, use the bianry heap method by showPerfectNodeLayers
    # This will not pass the max time limit
    def showPerfectNodeLayers(self, root):
        """
        Generate a perfect binary heap in list of nodes (Not Values)
        use None to replace empty Nodes for take index places
        """
        if not root:
            return []
        result = [root]
        layer = [root]
        while any(layer):
            new_layer = []
            for i in layer:
                if not i:
                    new_layer.append(None)
                    new_layer.append(None)
                else:
                    new_layer.append(i.left if i.left else None)
                    new_layer.append(i.right if i.right else None)
            result += new_layer
            layer = new_layer

        # add the first one to be None, to move the index starting from 1
        result = [None] + result
        return result


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        binaryheap = self.showPerfectNodeLayers(root)

        i,pi,qi = 0,0,0
        while i != len(binaryheap):
            node = binaryheap[i]
            if node is p:
                pi = i
            if node is q:
                qi = i
            i += 1

        parent_p, parent_q = [],[]
        while pi != 0:
            parent_p.append(pi)
            pi = pi // 2
        while qi != 0:
            parent_q.append(qi)
            qi = qi // 2


        while parent_p and parent_q:
            A, B = parent_p.pop(), parent_q.pop()
            if A == B:
                lca = A
            else:
                break

        return binaryheap[lca]


if __name__ == '__main__':
    A = genTree([
        3,
        5,1,
        6,2,0,8,
        None,None,7,4,
    ])
    assert Solution().lowestCommonAncestor(A, A.left, A.right) == A, 'Example 1'

    A = genTree([
        3,
        5, 1,
        6, 2, 0, 8,
        None, None, 7, 4,
    ])
    assert Solution().lowestCommonAncestor(A, A.left, A.left.right.right) == A.left, 'Example 2'

    A = genTree([
        3,
        5, 1,
        6, 2, 0, 8,
        None, None, 7, 4,
    ])
    assert Solution().lowestCommonAncestor(A, A.left.left, A.left.right.right) == A.left, 'Additional 1'

    A = genTree([
        3,
        5, 1,
        6, 2, 0, 8,
        None, None, 7, 4,
    ])
    assert Solution().lowestCommonAncestor(A, A.left.right, A.right.left) == A, 'Additional 2'

    A = genTree([
        2,
        None, 3
    ])
    assert Solution().lowestCommonAncestor(A, A, A.right) == A, 'Additional 3'

    A = genTree([
        2,
        1, None
    ])
    assert Solution().lowestCommonAncestor(A, A, A.left) == A, 'Additional 4'

    print('all passed')
