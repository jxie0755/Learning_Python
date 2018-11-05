# CS61A week09 Exam Prep 06 Orders of Growth and Linked List

from CS_61A.week09.csm_05 import Link, Tree

# Order of Growth
# The Weakest Link (Su15 Midterm 2 Q5d)
def append(link, value):
    """Mutates link by adding value to the end of link."""
    if link.rest is Link.empty:
        link.rest = Link(value)
    else:
        append(link.rest, value)

def extend(link1, link2):
    """Mutates link1 so that all elements of link2 are added
    to the end of link1.
    """
    while link2 is not Link.empty:
        append(link1, link2.first)
        link2 = link2.rest


# Consider the following linked list functions: Circle the order of growth that best describes the runtime of calling append, where n is the number of elements in the input link.


# Assuming the two input linked lists to extend both contain n elements, circle the order of growth that best describes the runtime of calling extend.
