"""CS61A week09 Exam Prep 06 Orders of Growth and Linked List"""

from CS_61A.week09.csm_05 import Link


# Order of Growth

# Q1
# The Weakest Link (Su15 Midterm 2 Q5d)
def append(link, value):
    """Mutates link by adding value to the end of link."""
    if link.rest is Link.empty:
        link.rest = Link(value)
    else:
        append(link.rest, value)

# O(n)

def extend(link1, link2):
    """Mutates link1 so that all elements of link2 are added
    to the end of link1.
    """
    while link2 is not Link.empty:
        append(link1, link2.first)
        link2 = link2.rest

# O(n^2)


# Q2 Interpretation (Fa14 Mock Final Q5e)
def g(n):
    if n % 2 == 0 and g(n + 1) == 0:
        return 0
    return 5

# O(1)


# Q3 Not with a fizzle, but with a bang (Su13 Midterm 2 Q2b)
def boom(n):
    if n == 0:
        return "BOOM!"
    return boom(n - 1)
# O(n)

def explode(n):
    if n == 0:
        return boom(n)  # O(1)
    i = 0
    while i < n:
        # boom(n)  o(n)
        i += 1
    return boom(n)

# explode(n)
# O(n^2)


# Q4 Not with a fizzle, but with a bang (Su13 Midterm 2 Q2c)
def dreams(n):
    if n<= 0:
        return n
    if n > 0:
        return n + dreams(n // 2)

# O((log(n))


# Q5 Various Programs (Sp14 Final Q5c)
def a(m, n):
    for i in range(m):
        for j in range(n // 100):
            print("hi")
# O(m*n)

def b(m, n):
    for i in range(m // 3):
        print("hi")
    for j in range(n * 5):
        print("bye")
# O(m+n)

def d(m, n):
    for i in range(m):
        j = 0
        while j < i:
            print("hi")
            j = j + 100
# O(m^2)


# Linked list

def conserve_links(a, b):
    """Makes Linked List a share as many Link instances as possible with
    Linked List b.a can use b's i-th Link instance as its i-th Link
    instance if a and b have the same element at position i.
    Should mutate a. b is allowed to be destroyed. Returns the new first
    Link instance of a.
    >>> x = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> y = Link(1, Link(9, Link(3, Link(4, Link(9, Link(6))))))
    >>> z = conserve_links(x, y)
    >>> curr_x, curr_z = x, z
    >>> assert z == y
    >>> assert z.rest.rest == y.rest.rest
    >>> assert z.rest.rest.rest.rest.rest == y.rest.rest.rest.rest.rest
    >>> assert z.rest.rest.rest.rest.rest == y.rest.rest.rest.rest.rest
    """
    if a.first == b.first:
        b.rest = conserve_links(a.rest, b.rest)
        return b
    else:
        return a


def slice_reverse(s, i, j):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> slice_reverse(s, 1, 2)
    >>> s
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> slice_reverse(s, 2, 4)
    >>> s
    Link(1, Link(2, Link(4, Link(3, Link(5)))))
    """
    start = s
    for _ in range(i-1):
        start = start.rest
    reverse = Link.empty
    current = start.rest

    for _ in range(j-i):
        rest = current.rest
        current.rest = reverse
        reverse = current
        current = rest

    start.rest.rest = current
    start.rest = reverse
