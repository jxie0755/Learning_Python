# sort vs sorted, reverse an order
l = [2, 3, 1, 'b', 'c', 'a']
# l1.sort()  # can not sort a mixed list.

l1 = [2, 3, 1, 4]
# sort() returns None, and change the original list
l1.sort()
print(l1.sort())  # >>> None
l2 = l1.sort()
print(l2) # >>> None, still none, can not use this to create new variables
print(l1)  # >>> [1, 2, 3, 4]

l2 = [2, 3, 1, 4]
# sorted(list) returns a new list, but does not change the original list
print(sorted(l2))  # >>> [1, 2, 3, 4]
print(l2)  # >>> [2, 3, 1, 4]
# unless assigned it a new variable
l2b = sorted(l2)
print(l2b)  # >>> [1, 2, 3, 4]

# reversely sorted, sort first, then reverse
l3 = [2, 3, 1, 4]
l3.sort(reverse=True)  # add argument to .sort()
print(l3)  # >>> [4, 3, 2, 1]



# reverse a list order
l4 = [2, 3, 1, 4]
# similar to .sort(), returns None, can not assign to new variables
l4.reverse()
print(l4)  # >>> [4, 1, 3, 2]

# another way to reverse the order
# this is the best way to reverse the order
l5 = [2, 3, 1, 4]
print(l5[::-1])  # >>> [4, 1, 3, 2]  # this only temporary reverse
print(l5)  # >>> [2, 3, 1, 4]  # l5 was not changed
l5b = l5[::-1]
print(l5b)  # >>> [4, 1, 3, 2] # make a copy for new variable



# reversed() does not work like sorted() !!!!!
# it returns an iterator ready to traverse the list in reversed order
# if want to temporary reverse the order, use the slice
l6 = [2, 3, 1, 4]
l7 = reversed(l6)
print(l7)  # >>> <list_reverseiterator object at 0x10410a3c8>

l8 = []
for i in reversed(l6):
    l8.append(i)
print(l8)  # >>> [4, 1, 3, 2]
# reverse the sequence of l6 in the iteration


for i in reversed(range(5, 10)):  # this range is 5, 6, 7, 8 , 9. Then reverse the order
    print(i)
# same as above
9
8
7
6
5
# other use
seqRange = range(5, 10)  # >>> [9, 8, 7, 6, 5]
print(list(reversed(seqRange)))

seqString = 'Python'
print(list(reversed(seqString)))  # >>> ['n', 'o', 'h', 't', 'y', 'P']

seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple)))  # >>> ['n', 'o', 'h', 't', 'y', 'P']

seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))  # >>> [5, 3, 4, 2, 1]
