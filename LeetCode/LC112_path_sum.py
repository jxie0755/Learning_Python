"""
https://leetcode.com/problems/path-sum/
P112 Path Sum
Easy

Given a binary tree and a sum,
determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
"""

from a0_TreeNode import *


class Solution_A1:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        """
        Borrow the idea of allPath, but add boolean verification when hit a leaf
        """
        return self.pathCollecter(root, target, [])

    def pathCollecter(self, root, target: int, path_so_far: List[int]) -> bool:
        if not root:
            return False

        elif not root.left and not root.right:  # isLeaf
            path_so_far = path_so_far + [root.val]
            return sum(path_so_far) == target

        else:
            left_path, right_path = path_so_far[:], path_so_far[:]
            left_path.append(root.val)
            right_path.append(root.val)
            return self.pathCollecter(root.left, target, left_path) or \
                   self.pathCollecter(root.right, target, right_path)

    # def allPath(self, root) -> List[int]:
    #     """
    #     show all the paths in a non-empty root
    #     """
    #     result = []
    #
    #     def helper(root, cur=[]):
    #         if not root:
    #             return None
    #         elif not root.left and not root.right: # isLeaf
    #             cur.append(root.val)
    #             result.append(cur)
    #         else:
    #             if root.left:
    #                 new_cur = cur[:]
    #                 new_cur.append(root.val)
    #                 helper(root.left, new_cur)
    #             if root.right:
    #                 new_cur = cur[:]
    #                 new_cur.append(root.val)
    #                 helper(root.right, new_cur)
    #
    #     helper(root)
    #     return result


class Solution_A2:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        """
        Use an internal fucntion to collect all path sums when hit a leaf
        Similar idea as A, but carry just the pathSum in recursion in stead of detailed path
        """
        return self.pathSumCollector(root, 0, target)

    def pathSumCollector(self, root: TreeNode, carryover: int, target: int) -> bool:
        """
        Internal helper to add all pathSum to a list
        """
        if not root:
            return False
        else:
            new_carryover = carryover + root.val
            if not root.left and not root.right:  # isLeaf
                return new_carryover == target  # collect path sum
            else:
                # carry the path sum so far and recursive find left and right
                return self.pathSumCollector(root.left, new_carryover, target) or \
                       self.pathSumCollector(root.right, new_carryover, target)


if __name__ == "__main__":
    testCase = Solution_A1()

    T0 = None
    assert not testCase.hasPathSum(T0, 0), "Edge 0"

    T1 = genTree([1])
    assert testCase.hasPathSum(T1, 1), "Edge 1"

    T2 = genTree([
        5,
        4, 8,
        11, None, 13, 4,
        7, 2, None, None, None, None, None, 1
    ])
    assert testCase.hasPathSum(T2, 22), "Example 1, 5+4+11+2"

    T3 = genTree([
        1,
        2, 3
    ])
    assert not testCase.hasPathSum(T3, 5), "Example 2"

    T4 = genTree([
        1,
        2, None
    ])
    assert not testCase.hasPathSum(T4, 0), "Example 3"

    print("All passed")
