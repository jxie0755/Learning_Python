# Asterisk is used different in def statement and actual code application.
# in def statement, it allows function to carry multiple arguments
# in code application, it force to unpack the iterable variables

def asterisk(*args): # this allows carry multiple arguments
    print(*args)  # this does not pack args into a single items
    # because print let you carry multiple args as well
    # can not use:
    # return *args

asterisk(1,2,'a','b')
# >>> 1 2 a b
# this allows to process each arg individually

asterisk([1,2,'a','b'])
# >>> [1, 2, 'a', 'b']
# if a iterable get passed in, it will be treated like a single item

asterisk(*[1,2,'a','b'])
# this is basically equals to asterisk(1,2,'a','b')
# as it unpacks before execution
# >>> 1 2 a b


def asterisk2(*args): # this allows carry multiple arguments
    return args  # this forced pack of args into a number of single items (tuple)

a = asterisk2(1,2,'a','b')
print(a)
print(type(a))
# >>> (1, 2, 'a', 'b') 
# >>> <class 'tuple'>
# this forced all individual items to pack

b = asterisk2([1,2,'a','b'])
print(b)
# >>> [1, 2, 'a', 'b'] # same, a tuple with one list item.
# even if the arg is a single packed iterable, it will add another layer of package on it ([1, 2, 'a', 'b'])

print(asterisk2(*[1,2,'a','b']))
# Again, equal to asterisk2(1,2,'a','b'), as it forced to break down the list into individual args.
# But then force to pack back into a tuple
# >>> (1, 2, 'a', 'b')



# double asterisk for keyword arguments
def keyword(**kwargs):
    print(kwargs)

keyword(first='A', second='B', fourth='C', third='D', fifth='E')
# >>>
# {'first': 'A', 'second': 'B', 'fourth': 'C', 'third': 'D', 'fifth': 'E'}
# kwargs output a dictionary


def keyword(**kwargs):
    return kwargs

a = keyword(first='A', second='B', fourth='C', third='D', fifth='E')
print(a)
# >>> {'first': 'A', 'second': 'B', 'fourth': 'C', 'third': 'D', 'fifth': 'E'}
print(type(a))
# >>> <class 'dict'>
