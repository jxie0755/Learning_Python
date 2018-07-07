# From CS61a
# http://composingprograms.com/pages/23-sequences.html


# Linked list

# Common representation of a sequence constructed fro nested aris is called a linked list
four = [1, [2, [3, [4, 'empty']]]]
# a pair containing the first element of the sequence (in this case 1) and the rest of the sequence

empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest"""
    assert is_link(rest), 'rest must be a linked list'
    return [first, rest]

def first(s):
    """return the first element of a linked list s."""
    assert is_link(s), 'only apllies to linked list'
    assert s != empty, 'empty linked list has no first element'
    return s[0]

def rest(s):
    """Return the rest of the elemetns of a linked list s"""
    assert is_link(s), 'rest only applies to linked lists'
    assert s != empty, 'empty linked list has no rest'
    return s[1]


# Test
if __name__ == '__main__':
    four = [1, [2, [3, [4, 'empty']]]]
    four = link(1, link(2, link(3, link(4, empty))))
    print(four)
    # >>>
    # [1, [2, [3, [4, 'empty']]]]


def len_link(s):
    """Return the length of linked list"""
    assert is_link(s), 'must apply on linked list'
    if len(s) == 2:
        return 1 + len_link(rest(s))
    else:
        return 0


def getitem_link(s, i):
    """Return the element at index i of linked list s"""
    assert is_link(s)
    if i == 0:
        return first(s)
    else:
        return getitem_link(rest(s), i-1)

# Test
if __name__ == '__main__':
    print(len_link(four))
    # >>> 4

    print(getitem_link(four, 1))
    # >>> 2
