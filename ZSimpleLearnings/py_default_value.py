# This is to show the default value can be impacted if it is a mutable type (list, dict, etc)
# https://stackoverflow.com/questions/48014503/class-default-parameter-in-python#48014519

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
