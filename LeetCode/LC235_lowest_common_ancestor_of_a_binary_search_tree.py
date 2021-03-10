# LC235 Lowest Common Ancestor of a Binary Search Tree
# Easy


# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.


from a0_TreeNode import *


class Solution(object):

    # Version A1
    # use a helper function to recursive check
    # first get the range of the root (min and max)
    # if p"s val and q"s val within the range, check the left and right until neither's range covers
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        pv, qv = sorted(p.val, q.val)
        minn = maxx = root
        while minn.left:
            minn = minn.left
        while maxx.right:
            maxx = maxx.right

        result = []

        def helper(root, A, B):
            rv = root.val
            if A <= pv <= qv <= B:
                result.append(root)
                if root.left:
                    helper(root.left, A, rv - 1)
                if root.right:
                    helper(root.right, rv + 1, B)

        helper(root, minn.val, maxx.val)
        return result[-1]

    # Version A2
    # Non-recursive version
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        pv, qv = sorted(p.val, q.val)
        minn = maxx = root
        while minn.left:
            minn = minn.left
        while maxx.right:
            maxx = maxx.right
        minv, maxv = minn.val, maxx.val

        while minv <= pv <= qv <= maxv:
            rv = root.val
            if minv <= pv <= qv <= rv - 1:
                root = root.left
            elif rv + 1 <= pv <= qv <= maxv:
                root = root.right
            else:
                return root


class Solution(object):
    # STD ans
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
            # Keep searching since root is outside of [s, b].
            root = root.left if s <= root.val else root.right
        # s <= root.val <= b.
        return root


if __name__ == "__main__":
    A = genTree([
        6,
        2, 8,
        0, 4, 7, 9,
        None, None, 3, 5
    ])
    assert Solution().lowestCommonAncestor(A, A.left, A.right) == A, "Example 1"

    A = genTree([
        6,
        2, 8,
        0, 4, 7, 9,
        None, None, 3, 5
    ])
    assert Solution().lowestCommonAncestor(A, A.left, A.left.right) == A.left, "Example 2"

    A = genTree([
        6,
        2, 8,
        0, 4, 7, 9,
        None, None, 3, 5
    ])
    assert Solution().lowestCommonAncestor(A, A.left.left, A.left.right.left) == A.left, "Additional 1"

    A = genTree([
        2,
        None, 3
    ])
    assert Solution().lowestCommonAncestor(A, A, A.right) == A, "Additional 2"

    A = genTree([
        2,
        1, None
    ])
    assert Solution().lowestCommonAncestor(A, A, A.left) == A, "Additional 3"

    print("All passed")
