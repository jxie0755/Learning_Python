# CS61A spring 2018 midterm exam 2

# Q1 Buggy Quidditch

# If an error occurs, write Error, but include all output displayed before the error.
# To display a function value, write Function.
# If an expression would take forever to evaluate, write Forever.

class Ball:
    points = 0
    time = lambda: 'Draco'

    def score(self, who):
        print(who, self.points)

    def __str__(self):
        return 'Magic'

class Snitch(Ball):
    points = 100
    time = lambda: 'Harry'

    def __init__(self):
        self.points = self.points + 50

    def score(self, p):
        if not time():
            print(Ball().score(p))
        else:
            Ball.score(self, p)

def chase(r):
    r.time = Snitch.time
    r.points += 1
    quaffle.points += 10
    print(r().points)

quaffle = Ball()
quaffle.points = 10
chasing = quaffle.score
time = lambda: Ball.points
malfoy = lambda: Ball.time()

print('A')
print(Snitch().points)
# >>>
# 150


print(chasing(quaffle))
# quaffle.score(quaffle)
# >>>
# print('Magic', quaffle.points)
# Magic 10

print('B')
print(Snitch().score('Seeker'))
# Ball.score('Seeker')
# >>>
# Seeker 0
# return None
# return None

print('C')
print(chase(Ball))
# Ball.time = lambda: 'Harry'
# Ball.points = 1
# quaffle.points = 20
# >>>
# 1
# return None

print('D')
# print(Snitch().score(malfoy()))
# Snitch().score(Ball.time()())   # 在上一题, Ball.time = Snitch.time, 所以Ball.time改了
# Snitch().score('Harry')  # Snitch()本身是snitch的实例,所以Snitch().points是150
# Ball.score(self, 'Harry') # 虽然转调用Ball.score,但是self.points仍然是Snitch.points
# >>>
# Harry 150
# return None


# Q2
s = 1
def to(s):
    ix = s[1:2]     # [4]
    ward[1] = 6     # ward = [3, 6, 5]
    def re(st):
        if st is not ward:    # ward is ward, skip this
            nonlocal s
            s = s.extend(ix)
            return re(ward)
        else:                 # execute this
            st.append(ix)     # ward.append([4,5])
    return re

ward = [3, 4] + list([5])
# [3, 4, 5]
print(to(ward)(s))  # 注意to(ward) return 函数re, 而re(s)这里调用的s是global的s,不是to(s)那个s, 也就是不是ward
# re(1)
# ward = ward.extend([4]) = [3,6,5,4]
# re(ward)
# ward.append(ix), ward = [3,6,5,4,[4]]
print(ward)
# >>>
# [3, 6, 5, 4, [4]]



# Q3

# Definition. A grid is a list of lists.
# Each list in a grid is called a row, and all rows must have the same length.
# [[1, 2], [3, 4]] is a grid of integers, but [[1, 2], [3, 4, 5]] is not a grid

# (a)
# Implement column, which takes a grid g and a non-negative integer c that is smaller than the length
# of a row in g. It returns a list containing the element at index c of each row in the grid.

def column(g, c):
    """Return the column of g at index c.
    >>> column([[3, 4, 5], [6, 7, 8], [9, 10, 11]], 1)
    [4, 7, 10]
    """
    ### your answer ###
    return [row[c] for row in g ]


# (b)
def print_grid(g):
    """Print each row on a separate line with columns aligned.

    >>> print_grid([[1, 234, 50, 4, 5], [67, 8, 90, 0, 500], [3, 4, 5, -500, 7]])
    1  234 50 4    5
    67 8   90 0    500
    3  4   5  -500 7
    """
    ### your answer ###
    cs = range(len(g[0]))
    widths = [max([len(str(row[c])) for row in g]) for c in cs]

    for row in g:
        line = ''
        for c in cs:
            s = str(row[c])
            line = line + s + ' ' * (widths[c]-len(s)+1)
        print(line)


# (c)
def expand(g, h, w, fill):
    """Expand grid g so that it has at least h rows and w columns.
    >>> g = [[1, 2, 3], [40, 50, 60]]

    >>> print_grid(expand(g, 2, 5, 10))
    1  2  3  10 10
    40 50 60 10 10

    >>> print_grid(expand(g, 5, 6, 0))
    1  2  3  10 10 0
    40 50 60 10 10 0
    0  0  0  0  0  0
    0  0  0  0  0  0
    0  0  0  0  0  0

    >>> print_grid(expand(g, 0, 0, 5))
    1  2  3  10 10 0
    40 50 60 10 10 0
    0  0  0  0  0  0
    0  0  0  0  0  0
    0  0  0  0  0  0
    """
    for row in g:
        row.extend([fill] * (w - len(row)))
    for k in range(h - len(g)):
        g.append([fill] * w)
    return g


# (d)
# Circle the O expression that describes how many new values must be added when a grid with n rows
# and n columns is expanded to 2*n rows and 2*n columns using the expand function. Assume that expand
# is implemented correctly.

# O(1)   O(log n)   O(n)   O(n^2)   O(2^n)   None of these
#                            X


# Q4 Sequences
# Implement stretch, which takes a Link instance s with no cycles.
# It mutates s so that, for each position k in the original s, the kth element is repeated k times.
# You do not need to use the name i.

class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'

# (a)
def stretch(s, repeat=0):
    """Replicate the kth element k times, for all k in s.
    >>> a = Link(3, Link(4, Link(5, Link(6))))
    >>> stretch(a)
    >>> print(a)
    <3, 4, 4, 5, 5, 5, 6, 6, 6, 6>
    """
    if s:
        stretch(s.rest, repeat + 1)
        for i in range(repeat):
            s.rest = Link(s.first, s.rest)



# (b)
# Implement combo, which takes two non-negative integers a and b.
# It returns the smallest integer that contains all of the digits of a in order,
# as well as all of the digits of b in order.

def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).
    >>> combo(531, 432) # 45312 contains both _531_ and 4_3_2.
    45312
    >>> combo(531, 4321) # 45321 contains both _53_1 and 4_321.
    45321
    >>> combo(1234, 9123) # 91234 contains both _1234 and 9123_.
    91234
    >>> combo(0, 321) # The number 0 has no digits, so 0 is not in the result.
    321
    """
    if a == 0 or b == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo(a//10, b//10) * 10 + a % 10
    return min(combo(a//10, b) * 10 + a % 10, combo(a, b//10) * 10 + b % 10)
    # min的使用很精髓



# Q5 Trees
class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])

# (a)
# Implement siblings, which takes a Tree instance t.
# It returns a list of the labels of all nodes in t that have a sibling.
# These labels can appear in any order.

def siblings(t):
    """Return a list of the labels of all nodes that have siblings in t.
    >>> a = Tree(4, [Tree(5), Tree(6), Tree(7, [Tree(8)])])
    >>> siblings(Tree(1, [Tree(3, [a]), Tree(9, [Tree(10)])]))
    [3, 9, 5, 6, 7]
    """
    result = [b.label for b in t.branches if len(t.branches) > 1]
    for b in t.branches:
        result += siblings(b)
    return result



# (b)
# Implement the Sib class that inherits from Tree.
# In addition to label and branches, a Sib instance t has an attribute siblings that stores the number of siblings t has in Sib trees containing t as a node.

# Assume that the branches of a Sib instance will never be mutated or re-assigned.

class Sib(Tree):
    """A tree that knows how many siblings it has.
    >>> a = Sib(4, [Sib(5), Sib(6), Sib(7, [Sib(8)])])
    >>> a.label
    4
    >>> a.branches[1].label
    6
    >>> a.siblings
    0
    >>> a.branches[1].siblings
    2
    """
    def __init__(self, label, branches=[]):
        self.siblings = 0
        self.label = label
        self.branches = branches
        for b in self.branches:
            b.siblings = len(self.branches) - 1
