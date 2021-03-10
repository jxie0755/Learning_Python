# LC124 Binary Tree Maximum Path Sum
# Hard


# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

from typing import *
from a0_TreeNode import *


class Solution:

    # Self version, first find all paths leaf to leaf, from left to right
    # Then find the max value of each paths from all its subsequence, then compare between paths
    def sumMaxSubs(self, lst):
        """find the max sum from all subsequences of a list"""
        max_so_far = -float("inf")
        for lenth in range(len(lst), 0, -1):
            for i in range(len(lst) - lenth + 1):
                cur = sum(lst[i:i + lenth])
                if cur > max_so_far:
                    max_so_far = cur
        return max_so_far

    def showPerfectLayers(self, root):
        if not root:
            return []
        result = [root]
        layer = [root]
        while any(layer):
            new_layer = []
            for i in layer:
                if not i:
                    new_layer.append(None)
                    new_layer.append(None)
                else:
                    new_layer.append(i.left if i.left else None)
                    new_layer.append(i.right if i.right else None)
            result += new_layer
            layer = new_layer

        # add the first one to be None, to move the index starting from 1
        return [None] + result

    def maxPathSum(self, root: TreeNode) -> int:

        if not root.left and not root.right:
            return root.val

        nodelist = self.showPerfectLayers(root)
        right_side = []
        rr = root
        while rr:
            right_side.append(rr)
            rr = rr.right

        # print([id(i) for i in right_side])

        def helper(idx, prev_location="U", cur_path=[], end=False):
            """
            recursive go around the nodes through parent-children link
            node only going from left to right
            only from leaf to leaf

            prev_location -
            "N" : "None", starting point at the Leaf
            "U" : "Up",   Coming down from parent
            "L" : "Left"  Coming up from left child
            "R" : "Right" Coming up from rgiht child

            """

            # print("idx", idx, "prev", prev_location, "curpath", cur_path, "end", end)
            node = nodelist[idx]

            if node:
                cur_path.append(node.val)
                this_location = "L" if idx % 2 == 0 else "R"

                if node and not node.left and not node.right and end:
                    paths.append(cur_path)  # end

                elif node:
                    if idx == 1:
                        if node.right:
                            helper(idx * 2 + 1, "U", cur_path[:], True)  # go right (only from left)
                        else:
                            paths.append(cur_path)  # end

                    elif prev_location == "N":
                        if node not in right_side:
                            helper(idx // 2, this_location, cur_path[:], True)  # go up if not on the right side

                    elif prev_location == "L":
                        if node not in right_side:
                            helper(idx // 2, this_location, cur_path[:], True)  # go up if not on the right side
                        helper(idx * 2 + 1, "U", cur_path[:], True)  # go right down

                    elif prev_location == "R":
                        if node not in right_side:
                            helper(idx // 2, this_location, cur_path[:], True)  # go up if not on the right side

                    elif prev_location == "U":
                        helper(idx * 2, "U", cur_path[:], True)  # go down left
                        helper(idx * 2 + 1, "U", cur_path[:], True)  # go down right
            else:
                paths.append(cur_path)  # end

        # print(nodelist)
        paths = [[i.val for i in right_side]]
        for k in range(len(nodelist)):
            node = nodelist[k]
            if node and not node.left and not node.right:
                helper(k, "N", [], False)

        # If no nodes ont the left side from root, special cases from root to botoom is needed
        if not root.left:
            helper(1, "U", [], False)

        # find out the max path from pathsmax of all paths
        max_so_far = -float("inf")
        for path in paths:
            path_max = self.sumMaxSubs(path)
            if path_max > max_so_far:
                max_so_far = path_max
        return max_so_far


if __name__ == "__main__":
    A = TreeNode(1)
    assert Solution().maxPathSum(A) == 1, "Edge 1"

    A = genTree([
        1,
        2, 3
    ])
    assert Solution().maxPathSum(A) == 6, "Example 1, 2+1+3 = 6"

    A = genTree([
        -10,
        9, 20,
        None, None, 15, 7
    ])
    assert Solution().maxPathSum(A) == 42, "Example 2, 15+20+7 = 42"

    A = genTree([
        1,
        2, 3,
        4, 5, 6, 7,
        8, 9, 100, 11, 12, 100, 14, 15
    ])
    assert Solution().maxPathSum(A) == 217, "Additional 1, 100+5+2+1+3+6+100=217"

    A = genTree([
        -1,
        5, 6
    ])
    assert Solution().maxPathSum(A) == 10, "Additional 2, 5+-1+6=10"

    A = genTree([
        -1,
        5, -1
    ])
    assert Solution().maxPathSum(A) == 5, "Additional 3, just 5"

    A = genTree([
        -1,
        1, -1,
        1, 1, -1, -2,
        -1, -1
    ])
    assert Solution().maxPathSum(A) == 3, "Additional 4, 1+1+1=3"

    A = genTree([
        -6,
        None, 3,
        None, None, 2, None
    ])
    assert Solution().maxPathSum(A) == 5, "Additional 4, 2+3=5"

    A = genTree([
        7,
        None, 2,
        None, None, 3, -7
    ])
    assert Solution().maxPathSum(A) == 12, "Additional 4, 7+2+3=12"

    print("All passed")
