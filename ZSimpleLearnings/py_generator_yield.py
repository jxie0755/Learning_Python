# any procedure or method with yield statement called generator

mylist = [1, 2, 3]  # iterable
rrange = range(5)   # iterator
print()

# create an iterable using list comprehension:
mylist2 = [x*x for x in mylist]
print(type(mylist2), mylist2)
# >>> <class 'list'> [1, 4, 9]

# Iterator is stored in the memory, can be iterated over multiple times
print(list(rrange))
print(list(rrange))

# Generators are iterators, but you can only iterate over them once.
# Itâ€™s because they do not store all the values in memory, they generate the values on the fly
# Generators are made through list comprehension with a '()' instead of '[]'
print()
mygenerator = (x*x for x in mylist)
print(type(mygenerator), mygenerator)
# >>> <class 'generator'> <generator object <genexpr> at 0x7f5c5c48a620>

# it has next() function just like a iterator
print(next(mygenerator))  # >>> 1
print(next(mygenerator))  # >>> 4

print()
# Yield is a keyword that is used like return, except the function will return a generator.
# must be used in a function, like 'return'
def createGenerator(x):
    for i in x:
        yield i*i

# basically, this is a function to return a generator
gg = createGenerator(range(4))
print('gg is', gg)      # >>> gg is <generator object createGenerator at 0x7fa19f18c678>

# it can be treated like an itertor but just once
lst1 = list(gg)            # >>> gg is <generator object createGenerator at 0x7fe495e4b678>
print('lst1 is', lst1)       # >>> ll is [0, 1, 4, 9]
print('gg is still', gg)   # it will still show the same information as before.
lst2 = list(gg)
print('lst2 is', lst2)     # >>> ll2 is [], after consumption, it becomes empty.

# generator is consumed once by each call
hh = createGenerator(range(8))
# list(hh) will be [0, 1, 4, 9, 16, 25, 36, 49]
for i in hh:
    print (i)
    if i >10:
        break
# >>> iterator over 0, 1, 4, 9, then break
# now hh is half consumed
print(list(hh)) # >>> [25, 36, 49]


# from https://www.ics.uci.edu/~pattis/ICS-33/lectures/generators.txt

# example of mixing yield and return in a generator
def createGenerator(x):
    for i in range(x):
        yield i*i
        if i == 5:
            return 'time to stop'
            # raise StopIteration('time to stop')   # equal with return line

g1 = createGenerator(15)
# for i in range(14):
#     print(next(g1))
# >>> iteration output 0,1,4,9,16,25 then raise StopIteration:time to stop
print(list(g1))  # >>> [0, 1, 4, 9, 16, 25]  # stoped after i == 5.
