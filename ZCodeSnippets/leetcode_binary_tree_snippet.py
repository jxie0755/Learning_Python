# This is just to summarize some useful functions learn from Leetcode Tree problems

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if not T.val:
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


def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    layers = []
    i, L = 0, 1
    while i != len(lst):
        layers.append(lst[i:i + L])
        i += L
        L *= 2
    pre_root = [TreeNode(i) for i in layers[0]]
    root_to_return = pre_root[0]

    for k in range(1, len(layers)):
        cur = [TreeNode(i) for i in layers[k]]
        for j in range(len(cur)):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0:
                pre_root[rt_idx].left = cur[j]
            else:
                pre_root[rt_idx].right = cur[j]
        pre_root = cur

    return root_to_return




def traverse(root):
    """return a flat list of the binary tree including None at the very bottom end"""
    if not root or root.val is None :
        # return [] this can filter out the None if needed
        return [None]

    return [root.val] + traverse(root.left) + traverse(root.right)
           # Sequence of these 3 parts can be maniluated to change travel direction

if __name__ == '__main__':
    A = genTree([3, None, 20, None, None, 15, 7])
    print(traverse(A))
    # >>> [3, None, 20, 15, None, None, 7, None, None]




def showLayers(root):
    """Show the tree layer by layer from top to bottom"""
    if root is None:
        return []

    result, current = [], [root]
    while current:
        next_level, vals = [], []
        for node in current:
            # if node.val is not None:    # So we add another if command to avoid None added into the list
            vals.append(node.val)   # However, this accepts None.
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level
        result.append(vals)

    return result

if __name__ == '__main__':
    A = genTree([3,None,20,None, None, 15, 7])
    print(showLayers(A))
    # >>> [[3], [None, 20], [None, None, 15, 7]]
