# P105 Construct Binary Tree from Preorder and Inorder Traversal
# Medium


# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.


from a0_TreeNode import *


class Solution:
    # This will pass but exceed max time limit
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)  # root在inorder中的位置

        left_found, right_found = False, False
        left_preorder, right_preorder = [], []
        left_inorder, right_inorder = [], []

        # 从preorder后面找到left和right的值
        for i in range(1, len(preorder)):
            check = preorder[i]
            if check in inorder:
                check_idx = inorder.index(check)
                if check_idx < root_idx and not left_found:  # 第一个出现的在root_idx左侧的preorder值
                    left_preorder = preorder[i:]
                    left_inorder = inorder[:root_idx]
                    left_found = True
                if check_idx > root_idx and not right_found:  # 第二个出现的在root_idx左侧的preorder值
                    right_preorder = preorder[i:]
                    right_inorder = inorder[root_idx:]
                    right_found = True
                if left_found and right_found:
                    break

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root


class Solution:
    # Same method idea as above but build a hash table to store the index of each value
    # Passed, but still very slow
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        hmp = dict()
        for idx, val in enumerate(inorder):
            hmp[val] = idx

        def helper(preorder_lst):
            if not preorder_lst:
                return None
            root_val = preorder_lst[0]
            root = TreeNode(root_val)
            root_idx = hmp[root_val]

            left_preorder, right_preorder = [], []

            # 通过对比idx过滤preorder, 得到新的left preorder和right preorder
            for i in preorder_lst:
                check_idx = hmp[i]
                if check_idx < root_idx:
                    left_preorder.append(i)
                elif check_idx > root_idx:
                    right_preorder.append(i)

            root.left = helper(left_preorder)
            root.right = helper(right_preorder)
            return root

        return helper(preorder)


class Solution(object):
    # STD ans
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, preorder, inorder, 0, 0, len(inorder))

    def buildTreeRecu(self, lookup, preorder, inorder, pre_start, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(preorder[pre_start])
        i = lookup[preorder[pre_start]]
        node.left = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1, in_start, i)
        node.right = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1 + i - in_start, i + 1, in_end)
        return node


if __name__ == "__main__":
    assert not Solution().buildTree([], []), "Edge 0"
    assert Solution().buildTree([1], [1]) == genTree([1]), "Edge 1"
    assert Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == genTree([
        3,
        9, 20,
        None, None, 15, 7
    ]), "Example 1"

    print("All passed")
