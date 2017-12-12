# reversed()
# list()

# reversed () generate an iterator

# for string
seqString = 'Python'
print(list(reversed(seqString)))
>>>
['n', 'o', 'h', 't', 'y', 'P']

# for tuple
seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple)))
['n', 'o', 'h', 't', 'y', 'P']

# for range
seqRange = range(5, 9)
print(list(reversed(seqRange)))
[8, 7, 6, 5]

# for list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))
[5, 3, 4, 2, 1]
