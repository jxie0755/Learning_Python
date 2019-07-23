# P173 Binary Search Tree Iterator
# Medium

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.


# Note:
# next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class BSTIterator(object):

    # Version A
    # Use traverse list
    # This will take O(n) space, n = number of nodes instead of O(h), h = height
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.flat = self.inOrderTraverse(root)

    def inOrderTraverse(self, root):
        if not root:
            return []
        return self.inOrderTraverse(root.left) + [root.val] + self.inOrderTraverse(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.flat.pop(0)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return bool(self.flat)


class BSTIterator(object):

    # Version B, O(h) memory.
    # Use stack, track one node in each depth
    # update the queue with all left branch to the bottom
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.que = []
        if root:
            self.que.append(root)
            self.updateQue()

    # Add from Leetcode P230
    def kthSmallest(self, k):
        s = []
        rank = 0
        cur = self.root
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
        return None

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

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.que:
            return True
        else:
            return False


if __name__ == "__main__":
    b0 = None
    iterator = BSTIterator(b0)
    assert not iterator.next(), "Edge step 1"
    assert not iterator.hasNext(), "Edge step 2"

    b1 = genTree([
        7,
        3, 15,
        None, None, 9, 20
    ])
    iterator = BSTIterator(b1)

    print(iterator.kthSmallest(3))

    assert iterator.next() == 3, "Step 1"
    assert iterator.next() == 7, "Step 2"
    assert iterator.hasNext(), "Step 3"

    assert iterator.next() == 9, "Step 4"
    assert iterator.hasNext(), "Step 5"

    assert iterator.next() == 15, "Step 6"
    assert iterator.hasNext(), "Step 7"

    assert iterator.next() == 20, "Step 8"
    assert not iterator.hasNext(), "Step 9"

    print("all passed")
