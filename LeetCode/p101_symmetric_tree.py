# P101 Symmetric Tree
# Easy

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val:
                s = str(T.val)
                if T.left and T.right:
                    return s + '\n' + '  ' * L + layer(T.left, L+1) + '\n' + '  ' * L + layer(T.right, L+1)
                elif T.left and not T.right:
                    return s + '\n' + '  ' * L + layer(T.left, L+1) + '\n' + '  ' * L + 'N'
                elif not T.left and T.right:
                    return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L+1)
                else:
                    return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'
            else:
                return 'N'

        return layer(self)

def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    layers = []
    i, L = 0, 1
    while i != len(lst):
        layers.append(lst[i:i+L])
        i += L
        L *=2
    k = 1
    pre_root = [TreeNode(i) for i in layers[0]]
    root_to_return = pre_root[0]
    while k != len(layers):
        cur = [TreeNode(i) for i in layers[k]]
        j = 0
        while j != len(cur):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0:
                pre_root[rt_idx].left = cur[j]
            else:
                pre_root[rt_idx].right = cur[j]
            j += 1
        k += 1
        pre_root = cur

    return root_to_return

print(genTree([1, 2, 2, 3, 4, 4, 3]))
print(genTree([1]))







A1 = TreeNode(1)
B1 = TreeNode(2)
B2 = TreeNode(2)
C1 = TreeNode(3)
C2 = TreeNode(4)
C3 = TreeNode(4)
C4 = TreeNode(3)

A1.left = B1
A1.right = B2
B1.left = C1
B1.right = C2
B2.left = C3
B2.right = C4

# print(A1)




class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        pass



# if __name__ == '__main__':
#     pass
