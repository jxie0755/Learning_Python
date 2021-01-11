# P101 Symmetric Tree
# Easy

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

from a0_TreeNode import *


class Solution:

    def showLayers(self, root):  # Omit None
        """Show the tree layer by layer from top to bottom"""
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)

        return result

    def isSymmetric(self, root: TreeNode) -> bool:
        # If wait till getting all the layers, it will be too late
        if not root:
            return True
        all_layer = self.showLayers(root)
        for i in all_layer:
            if i != i[::-1]:
                return False
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Check on the run, accepted, but too slow
        # O(N^2)
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
    def preorderTraversal(self, t):
        """return a flat list of the binary tree including None"""
        if not t:
            return [None]
        return [t.val] + self.preorderTraversal(t.left) + self.preorderTraversal(t.right)

    def preorderTraversal_mirrored(self, t):
        """return a flat list of the binary tree including None"""
        if not t:
            return [None]
        return [t.val] + self.preorderTraversal_mirrored(t.right) + self.preorderTraversal_mirrored(t.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        # Traversal with left pre and post order to generate the mirrored flat list compare if they are the same
        # O(N)
        return self.preorderTraversal(root) == self.preorderTraversal_mirrored(root)


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
            # print([i.val if i else "N" for i in stack])

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


if __name__ == "__main__":
    A0 = None
    assert Solution().isSymmetric(A0), "Edge 1"

    A00 = TreeNode(1)
    assert Solution().isSymmetric(A00), "Edge 2"

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
        0, None
    ])
    assert not Solution().isSymmetric(A3)

    print("All passed")
