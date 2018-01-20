# if only need to get one number
# recursive way (recursion)
def fib_gen_r(i):
    """
    Fibonacci function generator
    generate the fibonacci number at 'i'th posistion
    """
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib_gen_r(i - 1) + fib_gen_r(i - 2)

if __name__ == '__main__':
    print(fib_gen_r(7))  # >>> 13

# [0, 1, 1, 2, 3, 5, 8, 13]
#  0  1  2  3  4  5  6  7

# non-recursive way
# actually non-recursive way is much more efficient!!!
def fib_gen_nr(i):
    """
        Fibonacci function generator
        generate the fibonacci number at 'i'th posistion
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

if __name__ == '__main__':
    print(fib_gen_nr(7))  # >>> 13


# if need to output a list of fibonacci numbers till 'i'th position
# only have Non-recursive way
# just need to revise the nr method slightly
def fiblist_gen_nr(i):
    """
        Fibonacci function generator
        generate the fibonacci list till 'i'th posistion
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

if __name__ == '__main__':
    print(fiblist_gen_nr(7))  # >>> [0, 1, 1, 2, 3, 5, 8, 13]


# 新写法
def fib_gen_nr2(i):
    a, b = 0, 1
    for x in range(i):
        a, b = b, a+b
    return a

if __name__ == '__main__':
    print(fib_gen_nr2(7))  # >>> 13

def fiblist_gen_nr2(i):
    lst = [0]
    a, b = 0, 1
    for x in range(i):
        a, b = b, a+b
        lst.append(a)
    return lst

if __name__ == '__main__':
    print(fiblist_gen_nr2(7))  # >>> [0, 1, 1, 1, 2, 3, 5, 8, 13]



