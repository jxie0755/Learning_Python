# This is to show the default value can be impacted if it is a mutable type (list, dict, etc)

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
