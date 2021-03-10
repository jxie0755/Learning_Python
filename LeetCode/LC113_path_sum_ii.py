"""
https://leetcode.com/problems/path-sum-ii/
LC113 Path Sum II
Medium


Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

"""
from a0_TreeNode import *


class Solution_A:
    VALID_PATHS = []

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.validPathCollecter(root, targetSum, [])
        ans = self.VALID_PATHS.copy()
        self.VALID_PATHS.clear() # clear memory for next run
        return ans

    def validPathCollecter(self, root, target: int, path_so_far: List[int]) -> None:
        """
        Modified path collecting helper from LC112
        Add valid path to Class Attribute
        """
        if not root:
            pass

        elif not root.left and not root.right:  # isLeaf
            path_so_far = path_so_far + [root.val]
            if sum(path_so_far) == target:
                self.VALID_PATHS.append(path_so_far)

        else:
            left_path, right_path = path_so_far[:], path_so_far[:]
            left_path.append(root.val)
            right_path.append(root.val)
            self.validPathCollecter(root.left, target, left_path)
            self.validPathCollecter(root.right, target, right_path)



if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert testCase.pathSum(T0, 0) == [], "Edge 0"

    T1 = genTree([1])
    assert testCase.pathSum(T1, 1) == [
        [1]
    ], "Edge 1"

    T2 = genTree([
        5,
        4, 8,
        11, None, 13, 4,
        7, 2, None, None, None, None, 5, 1
    ])
    assert testCase.pathSum(T2, 22) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ], "Example 1"

    print("All passed")
