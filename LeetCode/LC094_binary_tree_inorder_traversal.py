"""
P094 Binary Tree Inorder Traversal
Medium


Given a binary tree, return the inorder traversal of its nodes' values.
中序遍历就是二叉树的平面投影,从左到右
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


from typing import *
from a0_TreeNode import *


class Solution:
    # Recursive method
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution(object):
    # STD ans
    # Time:  O(n)
    # Space: O(h)
    # Stack Solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root, True))
                stack.append((root.left, False))
        return result


# Morris Traversal Solution
class Solution_B(object):
    def inorderTraversal(self, root):
        # STD Ans
        # TODO Learn algorithm
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


if __name__ == "__main__":
    testCase = Solution()

    t0 = None
    assert testCase.inorderTraversal(t0) == []

    t1 = genTree([
        1,
        None, 2,
        None, None, 3, None])
    assert testCase.inorderTraversal(t1) == [1, 3, 2]

    print("All passed")
