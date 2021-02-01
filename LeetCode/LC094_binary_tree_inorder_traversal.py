"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
P094 Binary Tree Inorder Traversal
Medium


Given a binary tree, return the inorder traversal of its nodes' values.
中序遍历就是二叉树的平面投影,从左到右
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


from typing import *
from a0_TreeNode import *


class Solution_A:
    """
    Simple recursive method
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution_STD_A:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Stack Solution
        Space O(N), Time O(N)
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop() # Sequence guaranteed by always pop from end
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                # after poping, replace with expanded to next level by swapping
                stack.append((root.right, False))
                stack.append((root, True)) # label is_visited, to avoid repeatingly expand
                stack.append((root.left, False))
        return result


class Solution_STD_B:
    def inorderTraversal(self, root):
        """
        Morris Traversal Solution
        Space O(1), space O(N)
        """
        result, cur = [], root
        while cur:
            if cur.left is None:
                result.append(cur.val)
                cur = cur.right
            else:
                node = cur.left # if both L and R has value, always go left (label as node)

                # DO NOT use "==", this algorithm create cycling tree
                while node.right and node.right is not cur:
                    node = node.right

                if node.right is None:
                    # push cur all the way to the left, and label cur.right back to above level
                    node.right = cur # change orginal tree
                    cur = cur.left   # cur at the very left end of the right
                else:
                    result.append(cur.val)
                    node.right = None # return to the original tree
                    cur = cur.right # finished everything on the left, now move the right branch

        return result


if __name__ == "__main__":
    testCase = Solution_STD_B()

    t0 = None
    assert testCase.inorderTraversal(t0) == [], "Edge 0"

    t1 = genTree([
        1,
        None, 2,
        None, None, 3, None])
    assert testCase.inorderTraversal(t1) == [1, 3, 2], "Example 1"

    t2 = genTree([
        6,
        2, 7,
        1, 4, None,  9,
        None, None, 3, 5, None, None, 8, None
    ])
    assert testCase.inorderTraversal(t2) == [1,2,3,4,5,6,7,8,9], "Addtinal 1"

    print("All passed")
