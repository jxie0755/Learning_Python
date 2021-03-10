# LC257 Bianry Tree Paths
# Easy


# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.


from a0_TreeNode import *


class Solution(object):

    # Version A, recursive helper to track each path
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if not root:
            return []

        paths = []

        def helper(node, path=""):
            """add a path to paths if each to a leaf"""
            if not node.left and not node.right:
                paths.append(path + str(node.val))
            if node.left:
                l_path = path + str(node.val) + "->"
                helper(node.left, l_path)
            if node.right:
                r_path = path + str(node.val) + "->"
                helper(node.right, r_path)

        helper(root)
        return paths


if __name__ == "__main__":
    assert Solution().binaryTreePaths(None) == [], "Edge 0"

    A = genTree([
        1,
        2, 3,
        None, 5
    ])
    assert Solution().binaryTreePaths(A) == ["1->2->5", "1->3"], "Example 1"

    print("All passed")
