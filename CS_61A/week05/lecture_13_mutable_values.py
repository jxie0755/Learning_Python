# CS61A Lecture 13 Mutable Values

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

def make_withdraw2(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        # nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        return balance - amount
    return withdraw

if __name__ == '__main__':

    hundred = make_withdraw(100)
    print(hundred(25)) # >>> 75
    print(hundred(15)) # >>> 60  balance changed from previous operation

    hundred = make_withdraw2(100)
    print(hundred(25)) # >>> 75
    print(hundred(15)) # >>> 85 balance not changed, still calculate from 100 everytime

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g

a = f(1)
b = a(2)
b(3) + b(4)

# Additinal from reading chapter 2.4

a = [1,2,3]
b = list(a)
print(b)  # >>> [1,2,3]
b[0] = a
print(b)  # >>> [[1, 2, 3], 2, 3]


# Develop an implementation of mutable linked list
# Codes below are not executable
def mutable_link():
    """Return a functional implementation of a mutable linked list"""
    contents = 'empty'

    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ", ")

    return dispatch

def to_mutable_link(source):
    """Return a functional list with the same contents as source."""
    s = mutable_link()
    for element in reversed(source):
        s('push_first', element)
    return s

# Implement Dictionaries
def dictionary():
    """Return a functional implementation of a dictionary."""
    records = []

    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value

    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)

    return dispatch


d = dictionary()
d('setitem', 3, 9)
d('setitem', 4, 16)

print(d) # >>> <function dictionary.<locals>.dispatch at 0x00000129BB1956A8>
print(d('getitem', 3))  # >>> 9
print(d('getitem', 4))  # >>> 16
