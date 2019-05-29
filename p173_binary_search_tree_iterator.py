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

    ### Version A
    ### Use traverse list
    ### This will take O(n) space, n = number of nodes instead of O(h), h = height
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

    ### Version B
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        pass

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        pass

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        pass



b1 = genTree([
        7,
        3,15,
        None, None, 9, 20
    ])
iterator = BSTIterator(b1)
print(iterator.flat)


# if __name__ == '__main__':
#     b1 = genTree([
#         7,
#         3,15,
#         None, None, 9, 20
#     ])
#     iterator = BSTIterator(b1)
#
#     assert iterator.next() == 3, 'Step 1'
#     assert iterator.next() == 7, 'Step 2'
#     assert iterator.hasNext(), 'Step 3'
#
#     assert iterator.next() == 9, 'Step 4'
#     assert iterator.hasNext(), 'Step 5'
#
#     assert iterator.next() == 15, 'Step 6'
#     assert iterator.hasNext(), 'Step 7'
#
#     assert iterator.next() == 20, 'Step 8'
#     assert not iterator.hasNext(), 'Step 9'
#
#     print('all passed')
