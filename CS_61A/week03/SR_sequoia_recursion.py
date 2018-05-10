# Sequoia's notes on recursion
# https://sequoia-tree.github.io/textbook/Recursion.pdf

# Self access
def f():
    return f
f()    # >>> function f
f()()  # >>> still function f
print(f()()())  # >>> <function f at 0x0000020BA83501E0>

def f():
    return f()
# f()
# evluating f() will open a new frame to evaluate f()
# and this will go forever
# this is called stack overflow error (RecursionError)

def f(n):
    if n == 0:
        return 1
    return f(n)
# f(4)
# here we defined a stop recursion condition
# but this will still stack forever as it will never move to the stop condition

def f(n):
    if n == 0:
        return 1
    return f(n-1)

print(f(4))  # >>> 1

# here we make n smaller each new frame until it hits 0
# so the whole function will return 1

# TWO IMPORTANT IDEAS
# 1. Recursion is all about making the parameters smaller
# 2. Stay in the same frame


# Practice 1
def sum_lst(lst):
    if lst == []:
        return 0
    ### Your code here ###
    return lst.pop() + sum_lst(lst)

print(sum_lst([1,2,3,4]))
# >>> 10

# Practice 2
def comprehension(lst, f, pred):
    if lst  == []:
        return []
    ### Your code here ###
    first = [f(lst[0])] if pred(lst[0]) else []
    return first + comprehension(lst[1:], f, pred)

# Variable as Parameters
def count(total):
    i = 0
    while i < total:
        i += 1
        print(i)
count(5)
# >>>
# 1
# 2
# 3
# 4
# 5

def count(total, i=0):
    i += 1
    print(i)
    if i < total:
        return count(total, i)
count(5)
# >>>
# 1
# 2
# 3
# 4
# 5

# Practice 3
# a function to tell whether the parenthesis is balanced inside the string
def balanced(s, depth=0):
    ### Your code here ###

    if not s:
        return depth == 0
    if depth < 0:
        return False
    if s[0] == '(':
        return balanced(s[1:], depth+1)
    if s[0] == ')':
        return balanced(s[1:], depth - 1)
    else:
        return balanced(s[1:], depth)

print(balanced('(h(;;;)i)'))
# >>> True

