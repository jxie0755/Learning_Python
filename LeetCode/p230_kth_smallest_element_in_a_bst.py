# P230 Kth Smallest Element in a BST
# Medium


# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Version A
    # Indorder traverse to ge the sorted list, then get lst[k-1]
    # This is slow as it forces to go through all BST first
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inorderTraversal(root)[k-1]



class Solution(object):

    # Internal class of BST iterator from Leetcode P173
    class BSTIterator(object):

        # from Leetcode P173
        def __init__(self, root):
            """
            :type root: TreeNode
            """
            self.root = root
            self.que = []
            if root:
                self.que.append(root)
                self.updateQue()

        def updateQue(self):
            if self.que:
                last = self.que[-1]
                while last:
                    if last.left:
                        self.que.append(last.left)
                    last = last.left

        def next(self) -> int:
            """
            @return the next smallest number
            """

            if self.que:
                last = self.que[-1]
                next_val = last.val  # first get return vanl as a temp

                # if there is a right branch, then replace the last node with right branch
                if last.right:
                    self.que[-1] = last.right
                    self.updateQue()
                # if there is no right branch, move one level above to parent node
                else:
                    self.que.pop()

                return next_val

    # Version B
    # Borrow the idea from Leetcode P173, by using an iterator
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        iter = Solution().BSTIterator(root)
        for i in range(k):
            item = iter.next()
        return item


class Solution(object):

    # STD ans
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    # This is also using Queues for iterating, same idea of iterator
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        s, cur, rank = [], root, 0
        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right

        return float("-inf")

if __name__ == "__main__":
    A = genTree([
        3,
        1,4,
        None, 2
    ])
    assert Solution().kthSmallest(A, 1) == 1, "Example 1"

    A = genTree([
        5,
        3,6,
        2,4,None,None,
        1,
    ])
    assert Solution().kthSmallest(A, 3) == 3, "Example 2"

    print("all passed")
