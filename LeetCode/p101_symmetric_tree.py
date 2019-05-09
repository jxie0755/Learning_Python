# P101 Symmetric Tree
# Easy

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val is None:
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
    def showlayer(self, TN):
        """return a list of list where each sub-list the layer of a tree"""
        result = [[TN.val]]

        def helper(TN):
            layer = [TN]
            while any([i for i in layer]):
                new_layer = []
                new_layer_val = []
                for i in layer:
                    if i:
                        new_layer.append(i.left)
                        new_layer_val.append(i.left.val if i.left else None)
                        new_layer.append(i.right)
                        new_layer_val.append(i.right.val if i.right else None)
                    else:
                        new_layer.append(None)
                        new_layer_val.append(None)
                        new_layer.append(None)
                        new_layer_val.append(None)

                result.append(new_layer_val)
                layer = new_layer

        helper(TN)
        return result

    def isSymmetric(self, root: TreeNode) -> bool:
        ### If wait till getting all the layers, it will be too late
        if not root:
            return True
        all_layer = self.showlayer(root)
        for i in all_layer:
            if i != i[::-1]:
                return False
        return True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        ### Check on the run, accepted, but too slow
        ### O(N^2)
        layer = [root]
        while any([i for i in layer]):
            new_layer = []
            new_layer_val = []
            for i in layer:
                if i:
                    new_layer.append(i.left)
                    new_layer_val.append(i.left.val if i.left else None)
                    new_layer.append(i.right)
                    new_layer_val.append(i.right.val if i.right else None)
                else:
                    new_layer.append(None)
                    new_layer_val.append(None)
                    new_layer.append(None)
                    new_layer_val.append(None)

            if new_layer_val != new_layer_val[::-1]:
                return False
            else:
                layer = new_layer
        return True


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



    def isSymmetric(self, root: TreeNode) -> bool:
        ### Traverse with left priority and right priority to generate the mirrored flat list compare if they are the same
        ### O(N)
        return self.traverseDirected(root, 'L') == self.traverseDirected(root, 'R')


# Iterative solution
class Solution(object):
    # STD ans
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            # 查看栈堆
            # print([i.val if i else 'N' for i in stack])

            p, q = stack.pop(), stack.pop()

            if p is None and q is None:
                continue

            if p is None or q is None or p.val != q.val:
                return False

            # 这个堆栈顺序是精髓, 可以永远维持对称组相连在一起
            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)

        return True

# Recursive solution
class Solution2(object):
    # STD ans
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True

        return self.isSymmetricRecu(root.left, root.right)

    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)


if __name__ == '__main__':
    A0 = None
    assert Solution().isSymmetric(A0), 'Edge 1'

    A00 = TreeNode(1)
    assert Solution().isSymmetric(A00), 'Edge 2'

    A1 = genTree([
        1,
        2, 2,
        3, 4, 4, 3
    ])
    assert Solution().isSymmetric(A1)

    A2 = genTree([
        1,
        2, 2,
        None, 3, None, 3
    ])
    assert not Solution().isSymmetric(A2)

    A3 = genTree([
        1,
        0,None
    ])
    assert not Solution().isSymmetric(A3)

    print('all passed')
