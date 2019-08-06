"""
rotate the data array
can also solve by using collection.deque, by using the .rotate() method
"""

def array_rotate_EH(lst, n):
    """rotate the list elements, from End to Head"""
    for i in range(n):
        lst.insert(0, lst.pop())
    return lst

if __name__ == "__main__":
    print(array_rotate_EH([0,1,2,3], 1))
    print(array_rotate_EH([0,1,2,3], 2))
    print(array_rotate_EH([0,1,2,3], 3))
    print(array_rotate_EH([0,1,2,3], 4))
    # >>>
    # [3, 0, 1, 2]
    # [2, 3, 0, 1]
    # [1, 2, 3, 0]
    # [0, 1, 2, 3]
    print()


def array_rotate_HE(lst, n):
    """rotate the list elements, from Head to End"""
    for i in range(n):
        lst.append(lst.pop(0))
    return lst

if __name__ == "__main__":
    print(array_rotate_HE([0,1,2,3], 1))
    print(array_rotate_HE([0,1,2,3], 2))
    print(array_rotate_HE([0,1,2,3], 3))
    print(array_rotate_HE([0,1,2,3], 4))
    # >>>
    # [1, 2, 3, 0]
    # [2, 3, 0, 1]
    # [3, 0, 1, 2]
    # [0, 1, 2, 3]
    print()



# The best method that gives flexibility by using slice
def array_rotate(lst, n):
    """rotate the list elements, from End to Head if n > 0, and from Head to End if n < 0"""
    if n > 0:
        for i in range(n):
            lst = lst[-1:] + lst[0:-1]
    if n < 0:
        for i in range(abs(n)):
            lst = lst[1:] + lst[0:1]
    return lst


if __name__ == "__main__":
    print(array_rotate([0,1,2,3], 1))
    print(array_rotate([0,1,2,3], -1))
    # >>>
    # [3, 0, 1, 2]
    # [1, 2, 3, 0]
    print()
