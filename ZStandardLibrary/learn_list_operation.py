# list operation
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range


print('class list([iterable])')

# add and remove items from a list
listA = ['A', 'B', 'C', 'D', 'E', 'F']

listA[2] = 'G'         # replace item

n = 3

listA.append('G')      # add item at the end (one at a time)
listA.insert(n, 'G')   # add item and assign it at location n, other move down
                       # add multiple items: create a list, then merge the list
listA.insert(0, 'G')   # if n = 0, then always add items at the beginning
                       # if n = -1 是倒数第二个位置,不会在最后一个位置加入

del listA[n]           # remove item at location n.
listA.remove('B')      # remove specific items (one at a time)

a=1
b=4
listA[a:b] = []        # remove a serious of items together

listA = ['A', 'B', 'C', 'D', 'E', 'F']
listA.pop()            # pop an end item for use, and remove from the list
listA.pop(n)           # pop the item at position n in the list (index)

# revise tuple is not allowed, just re-write it.

# 两个list相减
list1 = [1,3,5]
list2 = [1,2,3,4,5,6]
for i in list1:
    list2.remove(i)
print(list2)

# Concatenation and method extend

L1 = [2, 1, 3]
L2 = [4, 5, 6]

L3 = [L1, L2]  # 这样不是merge,只是创造了一个List包含两个子List
L3 = L1 + L2   # 这样才是合并
print(L3)

L3.extend((7, 8))
L3.extend(['X', 'Y'])
L3.extend({'a': 1, 'b': 2})
# does not have to be a list, tuple or dict are also ok.(iterable)

print(L3)

# >>>
# [2, 1, 3, 4, 5, 6]
# [2, 1, 3, 4, 5, 6, 7, 8, 'X', 'Y', 'a', 'b']

# del and remove
L4 = [1, 2, 3, 1, 2, 3, 4, 5]

del(L4[1])    # del an item in the list
L4.remove(1)  # remove a value in the list(only the first one occured
print(L4)


# convert string to list
s = 'abc'
l = list(s)
print(l)

# split
s2 = 'I <3 cs'
l2 = list(s2)
print(l2)

s3 = s2.split('<')
print(s3)

# join
s4 = ''.join(l2)
print(s3)

# sort
L = [9, 6, 0, 3]
print(sorted(L))  # does not change L
print(L)

L.sort()          # change L
# This method sorts the list in place, using only < comparisons between items
print(L)

# reverse
L.reverse()       # reverse order only, not sorted
print(L)

L2 = [4, 6, 0, 3]
L2.sort(reverse=True)  # sort first, then reverse
print(L2)

# mutation, alias, cloning

warm = ['red', 'yellow', 'orange']
hot = warm

print(warm)
print(hot)

hot.append('pink')
print(hot)
# change items in hot leads to change items in warm as well
print(warm)


cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']

# These two list looked like the same, but not the same item in the memory
cool[2] = 'blue'
print(chill)
# change items in chill does not change items in cool
print(cool)

# This will also create a copy
cool = ['blue', 'green', 'grey']
chill = cool[:]

# sort vs sorted
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()          # sort() returns None, and change the original list
reversedwarm = warm.reverse()     # same above

print(sortedwarm)
print(reversedwarm)

cool = ['blue', 'green', 'grey']
sortedcool = sorted(cool)       # sorted(list) returns a new list, but does not change the original list
reversedcool = reversed(cool)   #

print(sortedcool)
print(reversedcool)



# list of list of list

warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]

brightcolors.append(hot)
print(brightcolors)

hot.append('pink')
print(hot)
print(brightcolors)
del warm[0]
print(brightcolors)


# slice of list
# String can also be sliced!!

listA = ['A', 'B', 'C', 'D', 'E', 'F']
# listA[:]    # a copy of listA
# listA[::-1] # 相当于reversed(listA)
# listA[-1]   # listA 的最后一个item
# listA[i:n]  # 从第i个数起,按顺序包括n-i个数(不包括position n的item)

# IMPORTANT:
# The slice of s from i to j is defined as the sequence of items with index k such that i <= k < j.
# If i or j is greater than len(s), use len(s).
# If i is omitted or None, use 0. If j is omitted or None, use len(s).
# If i is greater than or equal to j, the slice is empty.


# YOU SHOULD AVOID MUTATING A LIST WHEN ITERATING OVER IT!!!
def remove_dups(L1, L2):
    # L1_copy = L1[:]      # add this line could avoid the problem
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)

print(L1)
# >>> [2, 3, 4]
# not as expected to be [3, 4]

# python uses an internal counter to keep track of index when in loop
# mutating changes the list during iteration changed list length, but index counter was not updated


# mutable items in a list is a pointing system.
a = [1,2,3, ['a', 'b']]
b = list(a) # this creates a new list, but it is the same.
print(a == b) # True [1, 2, 3, ['a', 'b']]
print(a is b) # >>> False

a[0] = 5
print(a) # >>> [5, 2, 3, ['a', 'b']]
print(b) # >>> [1, 2, 3, ['a', 'b']]  # 5 will not be in b

a[3][0] = 'F'
print(a) # >>> [5, 2, 3, ['F', 'b']]
print(b) # >>> [1, 2, 3, ['F', 'b']]  # F will be added in b
