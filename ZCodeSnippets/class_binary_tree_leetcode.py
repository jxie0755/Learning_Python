# This is just to summarize some useful functions learn from Leetcode Tree problems
from typing import *
# Definition for a binary tree node.
# Definition for a binary tree node.
from math import log

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val is None:
                return 'N'

            s = str(T.val)
            if T.left and T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + layer(T.right, L + 1)
            elif T.left and not T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + 'N'
            elif not T.left and T.right:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L + 1)
            else:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'

        return layer(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def isLeaf(self):
        try:
            leftval = self.left.val
        except AttributeError:
            leftval = None
        try:
            rightval = self.right.val
        except AttributeError:
            rightval = None

        return leftval and rightval

def genTree(lst, i=1):
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if lst and i <= len(lst) and lst[i-1] is not None:
        node = TreeNode(lst[i-1])
        node.left = genTree(lst, i*2)
        node.right = genTree(lst, i*2+1)
        return node


### Traversal
# Sequence of these 3 parts can be maniluated to change travel direction
# if keep the [root.val] position, and switch recurive call on left and right, can get mirrored list.
def preorderTraversal(root) -> List[int]:
    """return a pre-order flat list of the binary tree including None at the very bottom end"""
    if not root:
        return [None]  # Can use [] as an option to omit None
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)

def inorderTraversal(root: TreeNode) -> List[int]:
    """return a in-order flat list of the binary tree including None at the very bottom end"""
    if not root:
        return [None] # Can use [] as an option to omit None
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

def postorderTraversal(root: TreeNode) -> List[int]:
    """return a post-order flat list of the binary tree including None at the very bottom end"""
    if not root:
        return [None] # Can use [] as an option to omit None
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]


if __name__ == '__main__':
    A = genTree([
        1,
        2, 3,
        4, 5, 6, 7])
    print('\npre order traverse:')
    print(preorderTraversal(A))
    # >>> [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, None, None]

    print('\nin order traverse:')
    print(inorderTraversal(A))
    # >>>  [None, 4, None, 2, None, 5, None, 1, None, 6, None, 3, None, 7, None]

    print('\npost order traverse:')
    print(postorderTraversal(A))
    # >>> [None, None, 4, None, None, 5, 2, None, None, 6, None, None, 7, 3, 1]

def showLayers(root):
    """Show the tree layer by layer from top to bottom"""
    if root is None:
        return []

    result, current = [], [root]
    while current:
        next_level, vals = [], []
        for node in current:
            # if node.val is not None:    # So we add another if command to avoid None added into the list
            vals.append(node.val)  # However, this accepts None.
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level
        result.append(vals)

    return result


if __name__ == '__main__':
    A = genTree([3, None, 20, None, None, 15, 7])
    print('\nshowLayers:')
    print(showLayers(A))
    # >>> [[3], [None, 20], [None, None, 15, 7]]



def showPerfectLayers(root):
    """
    Generate a perfect binary heap in list of nodes (Not Values)
    use None to replace empty Nodes for take index places
    """
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



if __name__ == '__main__':
    A = genTree([3, None, 20, None, None, 15, 7])
    print('\nshowPerfectLayers:')
    L = showPerfectLayers(A)
    LV = []
    for i in L:
        if i:
            LV.append(i.val)
        else:
            LV.append(None)
    print(LV)


def allPathsLtoL(root: TreeNode) -> List:
    def helper(idx, prev_location='U', cur_path=[], end=False):
        """
        recursive go around the nodes through parent-children link
        node only going from left to right
        only from leaf to leaf

        prev_location -
        'N' : 'None', starting point at the Leaf
        'U' : 'Up',   Coming down from parent
        'L' : 'Left'  Coming up from left child
        'R' : 'Right' Coming up from rgiht child

        """

        # print('idx', idx, 'prev', prev_location, 'curpath', cur_path, 'end', end)
        node = nodelist[idx]

        if node:
            cur_path.append(node.val)
            this_location = 'L' if idx % 2 == 0 else 'R'

            right_side = []
            rr = root
            while rr:
                right_side.append(rr)
                rr = rr.right

            if node and not node.left and not node.right and end:
                paths.append(cur_path)  # end

            elif node:
                if idx == 1:
                    helper(idx * 2 + 1, 'U', cur_path[:], True)  # go right (only from left)

                elif prev_location == 'N':
                    if node not in right_side:
                        helper(idx // 2, this_location, cur_path[:], True)  # go up if not on the right side

                elif prev_location == 'L':
                    if node not in right_side:
                        helper(idx // 2, this_location, cur_path[:], True)  # go up if not on the right side
                    helper(idx * 2 + 1, 'U', cur_path[:], True)  # go right down

                elif prev_location == 'R':
                    if node not in right_side:
                        helper(idx // 2, this_location, cur_path[:], True)  # go up if not on the right side

                elif prev_location == 'U':
                    helper(idx * 2, 'U', cur_path[:], True)  # go down left
                    helper(idx * 2 + 1, 'U', cur_path[:], True)  # go down right
            else:
                paths.append(cur_path)  # end

    nodelist = showPerfectLayers(root)
    paths = []
    for k in range(len(nodelist)):
        node = nodelist[k]
        if node and not node.left and not node.right:
            helper(k, 'N', [], False)

    # If no nodes ont the left side from root, special cases from root to botoom is needed
    if not root.left:
        helper(1, 'U', [], False)

    return paths


if __name__ == '__main__':
    A = genTree([
        1,
        2, 3,
        4, 5, 6, 7,
    ])

    print('\nall paths leaf to leaf:')
    for i in allPathsLtoL(A):
        print(i)



def allPath(root):
    """show all the paths from root to leaf in a non-empty root"""
    result = []

    def helper(root, cur=[]):
        if not root:
            return None
        elif not root.left and not root.right:
            cur.append(root.val)
            result.append(cur)
        else:
            if root.left:
                new_cur = cur[:]
                new_cur.append(root.val)
                helper(root.left, new_cur)
            if root.right:
                new_cur = cur[:]
                new_cur.append(root.val)
                helper(root.right, new_cur)

    helper(root)
    return result


if __name__ == '__main__':
    A = genTree([
        1,
        2, 3,
        4, 5, 6, 7
    ])
    print('\nall path:')
    for i in allPath(A):
        print(i)
    # >>>
    # [1, 2, 4]
    # [1, 2, 5]
    # [1, 3, 6]
    # [1, 3, 7]
