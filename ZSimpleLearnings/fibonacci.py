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

print(fib_gen_r(30))

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

print(fib_gen_nr(30))

# if need to output a list of fibonacci numbers till 'i'th position
# only need to revise the nr method slightly
def fiblist_gen_nr(i):
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
        return lst

print(fiblist_gen_nr(30))
