# If ZCodeSnippets is not source root, then below won't work:
# from class_tree_pretty import Tree

# This will work regardless if ZCodeSnippets is source root or not
from ZCodeSnippets.class_tree_pretty import Tree

T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
print(T)

# None of above is related to whether ZSimpleLearnings is source root or not
