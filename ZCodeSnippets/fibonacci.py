# this is to learn different ways of creating fibonacci number/list

# if only need to get one number
# recursive way (recursion)
# Time O(2^N)
def fib_gen_r(i):
    """
    Fibonacci function generator
    generate the fibonacci number at "i"th posistion
    """
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib_gen_r(i - 1) + fib_gen_r(i - 2)

if __name__ == "__main__":
    print(fib_gen_r(7))  # >>> 13
    print()


# [0, 1, 1, 2, 3, 5, 8, 13]
#  0  1  2  3  4  5  6  7

# non-recursive way
# actually non-recursive way is much more efficient!!!
# 这其实就是最基础的动态规划 Time O(N)
def fib_gen_nr(i):
    """
        Fibonacci function generator
        generate the fibonacci number at "i"th posistion
    """
    lst = [0, 1]
    if i == 0:
        return lst[0:1]
    elif i == 1:
        return lst[0:2]
    elif i >= 2:
        for j in range(2, i+1):
            temp = lst[j-1] + lst[j-2]
            lst.append(temp)
        return lst[-1]

if __name__ == "__main__":
    print(fib_gen_nr(7))  # >>> 13
    print()



# if need to output a list of fibonacci numbers till "i"th position
# only have Non-recursive way
# just need to revise the nr method slightly
def fiblist_gen_nr(i):
    """
        Fibonacci function generator
        generate the fibonacci list till "i"th posistion
    """
    lst = [0, 1]
    if i == 0:
        return lst[0:1]
    elif i == 1:
        return lst[0:2]
    elif i >= 2:
        for j in range(2, i+1):
            temp = lst[j-1] + lst[j-2]
            lst.append(temp)
        return lst

if __name__ == "__main__":
    print(fiblist_gen_nr(7))  # >>> [0, 1, 1, 2, 3, 5, 8, 13]
    print()

# 新写法

def fib_gen_nr2(i):
    a, b = 0, 1
    for x in range(i):
        a, b = b, a+b  # 必须是同排,这样会调用上一次的a,b值,a值不会由于a=b后改变!
    return a

if __name__ == "__main__":
    print(fib_gen_nr2(7))  # >>> 13
    print()


def fiblist_gen_nr2(i):
    lst = [0]
    a, b = 0, 1
    for x in range(i):
        a, b = b, a+b
        lst.append(a)
    return lst

if __name__ == "__main__":
    print(fiblist_gen_nr2(7))  # >>> [0, 1, 1, 2, 3, 5, 8, 13]
    print()



# use generator in fibonacci function
def genFib():  # this created a generator for fibonacci numbers
    a, b = 0, 1
    yield a
    yield b
    while True:
        next = a + b
        yield next
        a, b = b, next

# print a list of any length for fibonacci numbers
def fib_gen_nr3(x):
    """x is the threshold to stop when a fib number is larger than it"""
    for n in genFib():
        if n >= x:
            break
if __name__ == "__main__":
    fib_gen_nr3(13)
    # >>>
    # 0
    # 1
    # 1
    # 2
    # 3
    # 5
    # 8
    # 13


# Memorization method + recursion
# This will increase efficiency as the recursion method repeatedly calculate f(n-1), f(n-2)...to f(0) many times.

def fib_gen_r_mem(n):
    mem_dict = {0: 0, 1: 1}

    def helper(n):
        if n in mem_dict:
            return mem_dict[n]
        else:
            ans = helper(n-1) + helper(n-2)
            mem_dict[n] = ans
            return ans

    return helper(n)



# Use Memoization method as a decorator
# First define the memo method as a high-order function:
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
# Then create the regular fib method, and use memo as decorator
@ memo
def fib_gen_r(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib_gen_r(i - 1) + fib_gen_r(i - 2)

# print(fib_gen_r(50))  # >>> 12586269025
# This is the same as above integrated memoization method


# Additional: Fib tree by using the tree class
from class_tree import Tree

@memo
def fib_tree(n):
    """A Fibonacci tree."""
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


def fib_leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        s = []
        for b in t.branches:
            s.extend(fib_leaves(b))
        return s



if __name__ == "__main__":

    import time

    start_time = time.time()
    print(fib_gen_r(30))
    # >>> 832040
    # this could take some time
    print(f"--- {time.time() - start_time}s seconds ---\n")

    print(fib_gen_r(35))
    # >>> 9227465
    # this could take some time
    print(f"--- {time.time() - start_time}s seconds ---\n")

    start_time = time.time()
    print(fib_gen_r(40))
    # >>> 102334155
    # this could take some time
    print(f"--- {time.time() - start_time}s seconds ---\n")

    start_time = time.time()
    print(fib_gen_r_mem(40))
    # >>> 354224848179261915075
    # which is impossible to calculate in regular recursion method
    print(f"--- {time.time() - start_time}s seconds ---\n")

    start_time = time.time()
    print(fib_gen_r_mem(500))
    # >>> 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
    # which is impossible to calculate in regular recursion method
    print(f"--- {time.time() - start_time}s seconds ---\n")

    a = fib_tree(4)
    b = fib_leaves(a)
    print(a)
    # 3
    #   1
    #     0
    #     1
    #   2
    #     1
    #     1
    #       0
    #       1

    print(b) # >>> [0, 1, 1, 0, 1]
    assert sum(b) == fib_gen_r(4)  # The 4th fib number is 3, also as the root of fib_tree(4)
