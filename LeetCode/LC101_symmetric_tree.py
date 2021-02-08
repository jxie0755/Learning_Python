"""
https: // leetcode.com / problems / symmetric - tree /
P101 Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

from a0_TreeNode import *


class Solution_A1:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Verify if all layers are symmetric
        """
        if not root:
            return True
        all_layer = self.showLayers(root)
        for i in all_layer:
            if i != i[::-1]:
                return False
        return True

    def showLayers(self, root) -> List[List[int]]:
        """
        Helper: show all layers in a tree
        Show the tree layer by layer from top to bottom
        """
        result, layer = [], [root]
        while layer:
            valid_node_found = False; # setup a label to identify the layer has a valid node
            next_layer, node_vals = [], []
            for node in layer:
                if not node:
                    node_vals.append(None)
                else:
                    node_vals.append(node.val)
                    valid_node_found = True # label if one valid node can be found
                    next_layer.append(node.left)
                    next_layer.append(node.right)

            if valid_node_found:
                layer = next_layer
            else:
                break

            result.append(node_vals)

        return result



class Solution_A2:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Similar idea to A1, but all-in-one without helper
        Check each layer on the run
        """
        layer = [root]
        while layer:
            next_layer = []
            node_vals = []
            valid_node_found = False;
            for node in layer:
                if not node:
                    node_vals.append(None)
                else:
                    node_vals.append(node.val)
                    valid_node_found = True  # label if one valid node can be found
                    next_layer.append(node.left)
                    next_layer.append(node.right)

            if node_vals != node_vals[::-1]:
                return False
            elif valid_node_found:
                layer = next_layer
            else:
                break
        return True



class Solution_B:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Traversal with left pre and post order to generate the mirrored flat list compare if they are the same
        O(N)
        """
        return self.preorderTraversal(root) == self.preorderTraversal_mirrored(root)

    def preorderTraversal(self, t):
        """
        return a flat list of the binary tree
        Refer to LC144, but record None nodes, to track symmetry
        """
        if not t:
            return [None]
        return [t.val] + self.preorderTraversal(t.left) + self.preorderTraversal(t.right)

    def preorderTraversal_mirrored(self, t):
        """
        return a flat list of the binary tree
        Refer to LC144, but record None nodes, to track symmetry
        Mirrored version
        """
        if not t:
            return [None]
        return [t.val] + self.preorderTraversal_mirrored(t.right) + self.preorderTraversal_mirrored(t.left)


class Solution_C:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Verify by comparing the root and the flipped root
        If a flipped tree is the same as itself, then it is symmetric
        """
        return self.isSameTree(root, self.flipTree(root))

    def flipTree(self, root: TreeNode) -> TreeNode:
        """
        A helper to generate a flipped tree
        """
        if not root:
            return None
        else:
            duplicateTree = TreeNode(root.val)
            duplicateTree.left = self.flipTree(root.right)
            duplicateTree.right = self.flipTree(root.left)
            return duplicateTree

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Helper, refer to LC100
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and \
                   self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right, q.right)



class Solution_STD1:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Iterative solution using a stack
        """
        if root is None:
            return True

        stack = [root.left, root.right]
        while stack:
            # 查看栈堆
            # print([i.val if i else "N" for i in stack])
            L, R = stack.pop(), stack.pop()

            if L is None and R is None:
                continue

            if L is None or R is None or L.val != R.val:
                return False

            # 这个堆栈顺序是精髓, 可以永远维持对称组相连在一起
            stack.append(L.left)
            stack.append(R.right) # external side

            stack.append(L.right)
            stack.append(R.left) # internal side

        return True



class Solution_STD2:
    """
    Recursive solution
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isSymmetricRecu(root.left, root.right)

    def isSymmetricRecu(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)
                                      # external side                                 # internal side



if __name__ == "__main__":
    testCase = Solution_STD2()

    T0 = None
    assert testCase.isSymmetric(T0), "Edge 0"

    T00 = TreeNode(1)
    assert testCase.isSymmetric(T00), "Edge 1"

    T1 = genTree([
        1,
        2, 2,
        3, 4, 4, 3
    ])
    assert testCase.isSymmetric(T1), "Example 1"

    T2 = genTree([
        1,
        2, 2,
        None, 3, None, 3
    ])
    assert not testCase.isSymmetric(T2), "Example 2"

    T3 = genTree([
        1,
        0, None
    ])
    assert not testCase.isSymmetric(T3), "Example 3"

    print("All passed")
