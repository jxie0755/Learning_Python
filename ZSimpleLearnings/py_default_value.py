# This is to show the default value can be impacted if it is a mutable type (list, dict, etc)
# STOF https://stackoverflow.com/q/48014503/8435726

def f(x=[]):
    return x

print(f())  # >>> []

# since this default empty list is mutable, if the default is changed, for other purpose.
list1 = f()
list1.append(99)
list1.append(101)
print(list1)  # >>> [99, 101]

# previous operation of list1 changed the function's default parameter
print(f())  # >>> [99, 101]

list2 = f()[:]  # a good way is to create a copy to avoid
list2.append(300)
print(list2)  # >>> [99, 101, 300]
print(f())  # >>> [99, 101]

# Just be careful about this issue

def g(x=5):
    return x

print(g())  # >>> 5
a = g()
print(a)  #  >>> 5
a += 4
print(a)  # >>> 9

print(g()) # >>> 5 # not impacted because int is not mutable


# A good way to avoid this from happening, is to use None then define the default in the function
def h(x=None):
    if x is None:
        x = []
    return x

print(h())  # >>> []
list3 = h()
list3.append(33)
list3.append(44)
print(list3)  # >>> [33, 44]
print(h())  # >>> []


# Use mutable default variable is dangerous but could work for some recursion method
# STOF: https://stackoverflow.com/q/54577667/8435726

def list_from_zero(n, lst=[]): # in the beginning, empty lst is created when at n

    if n > 0:
        list_from_zero(n-1)
        # when call n-1, because lst is called for n,
        # then this call will no longer create a new empty lst,
        # but to keep use the lst in n

    lst.append(n)

    return lst

# Same idea but switch append and recursion
def list_to_zero(n, lst=[]):  # in the beginning, empty lst is created when at n

    lst.append(n)

    if n > 0:
        list_to_zero(n - 1)
        # when call n-1, because lst is called for n,
        # then this call will no longer create a new empty lst,
        # but to keep use the lst in n

    return lst

print(list_from_zero(5))
# >>> [0, 1, 2, 3, 4, 5]

print(list_to_zero(5))
# >>> [5, 4, 3, 2, 1, 0]

# It"s taking advantage of the fact that the same list (which is initially empty) is shared by all recursive calls that don"t explicitly provide a list
# Essentiall equal to:

L = []
def list_to_zero_global(n):
    global L
    L.append(n)
    if n > 0:
        list_to_zero_global(n-1)
    return L

list_to_zero_global(4)
print(L)
# >>> [4, 3, 2, 1, 0]
# But in this case, L is truly global, but in recursive method, L is only global to all recursive calls
