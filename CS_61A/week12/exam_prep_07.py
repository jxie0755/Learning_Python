# CS61A Exam Prep 07 Object-Oriented Programming, Trees & Linked List

# Tree
class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return "Tree({0}{1})".format(self.label, branch_str)

    def __str__(self):
        return "\n".join(self.indented())

    def indented(self):  # this is to recursively print a Tree.
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append("  " + line)
        return [str(self.label)] + lines
        # This is the original print_tree fucntion is a series of print() at different lines.
        # But __str__ requires to return a str object.

    # Set getter functions
    def get_label(self):
        return self.label

    def get_branches(self):
        return self.branches

    # Set bool function to tell whether it is a leaf
    # There is no need to tell whether it is a tree, because the object is created under the tree class.
    # Leaf has no branches, if it is not a leaf, then it must be a tree with branches.
    def is_leaf(self):
        """To tell whether the tree instance is a leaf or a tree with branches"""
        return not self.branches

# Linked list
class Link:
    """A linked list class"""
    empty = ()

    def __init__(self, value, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        # This is different from type(rest) == Link
        # Check detail from ZSimpleLearnings.py_instance_vs_type.py

        self.value = value
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ", " + repr(self.rest)
        else:
            rest_str = ""
        return "Link({0}{1})".format(self.value, rest_str)

    # def __str__(self):
    #     string = "<"
    #     while self.rest is not Link.empty:
    #         string += str(self.value) + ", "
    #         self = self.rest
    #     return string + str(self.value) + ">"

    @property
    def second(self):
        return self.rest.value

    @second.setter  # Must already exist (means .second should be a property)
    def second(self, value):
        self.rest.value = value

    @ property
    def last(self):
        if self.rest:
            self = self.rest.last
        return self

    @last.setter
    def last(self, value):
        if self.rest:
            self = self.rest.last
        self.value = value


# Tree functions
def linky_paths(t):
    """Takes in a tree, t, and modifies each label to be the path from that node
    to the root
    >>> t = Tree(1, [Tree(2)])
    >>> linky_paths(t)
    >>> t
    Tree(Link(1), [Tree(Link(2, Link(1)))])"""

    def helper(t, path_so_far):
        t.label = Link(t.label, path_so_far)
        for b in t.branches:
            helper(b, t.label)

    helper(t, Link.empty)

def find_file_path(t, file_str):
    """
    >>> t = Tree("data", [Tree("comm", [Tree("dummy.py")]), Tree("ecc", [Tree("hello.py"), Tree("file.py")]), Tree("file2.py")])
    >>> find_file_path(t, "file2.py")
    "/data/file2.py"
    >>> find_file_path(t, "dummy.py")
    "/data/comm/dummy.py"
    >>> find_file_path(t, "hello.py")
    "/data/ecc/hello.py"
    >>> find_file_path(t, "file.py")
    "/data/ecc/file.py"
    """
    def helper(t, file_str, path_so_far):
        if t.label == file_str and t.is_leaf():
                                   # not necessary but to avoid folder and file as the same name
            return path_so_far + "/" + t.label
        elif t.is_leaf():
            return None
        for b in t.branches:
            result = helper(b, file_str, path_so_far + "/" + t.label)
            if result:
                return result
    return helper(t, file_str, "")

# Linked list functions
# Convert to String Implement convert_to_string which takes in a Linked List link
# and coverts the Linked List to a file path.
def convert_to_string(link):
    """
    >>> link = Link("data" , Link("file2.py"))
    >>> convert_to_string(link)
    "/data/file2.py"
    """
    if not link:
        return ""
    return "/" + link.value + convert_to_string(link.rest)

# All Paths Linked Implement all_paths_linked which takes in a Tree t and returns a list of all paths from root to leaf in a tree with one catch â€“ each path is represented as a linked list.

def all_paths_linked(t):
    """
    >>> t1 = Tree(1, [Tree(2), Tree(3)])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    >>> all_paths_linked(t1)
    [Link(1, Link(2)), Link(1, Link(3))]
    >>> all_paths_linked(t2)
    [Link(1, Link(2)), Link(1, Link(3, Link(4))), Link(1, Link(3, Link(5)))]
    """
    # paths = []
    # if t.is_leaf():
    #     paths.append(Link(t.label))
    # for b in t.branches:
    #     for path in all_paths_linked(b):
    #         paths.append(Link(t.label, path))
    # return paths

    # Version 2 from exam_prep_07
    if t.is_leaf():
        return [Link(t.label)]
    result = []
    for branch in t.branches:
        result = result + [Link(t.label, path) for path in all_paths_linked(branch)]
    return result


# Find File Path 2
# For this question, use the definition of all_paths_linked and convert_to_string from previous practice
def find_file_path2(t, file_str):
    """
    >>> t = Tree("data", [Tree("comm", [Tree("dummy.py")]), Tree("ecc", [Tree("hello.py"), Tree("file.py")]), Tree("file2.py")])
    >>> find_file_path2(t, "file2.py")
    "/data/file2.py"
    >>> find_file_path2(t, "dummy.py")
    "/data/comm/dummy.py"
    >>> find_file_path2(t, "hello.py")
    "/data/ecc/hello.py"
    >>> find_file_path2(t, "file.py")
    "/data/ecc/file.py"
    """
    for link in all_paths_linked(t):
        original = link
        while original:
            if original.value == file_str:
                return convert_to_string(link)
            original = original.rest

# Skip Implement skip which takes in a Linked List lnk and an integer n which is great than 1 and mutates lnk such that every nth element is skipped.
def skip(lnk, n):
    """
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> skip(lnk, 2)
    >>> lnk
    Link(1, Link(3, Link(5)))
    >>> lnk2 = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> skip(lnk2, 4)
    >>> lnk2
    Link(1, Link(2, Link(3, Link(5, Link(6)))))
    """
    count = 1
    def skipper(lst):
        nonlocal count
        count += 1
        if not lst:
            return None
        elif count == n:
            lst.rest = lst.rest.rest
            count = 1
        skipper(lst.rest)
    skipper(lnk)
