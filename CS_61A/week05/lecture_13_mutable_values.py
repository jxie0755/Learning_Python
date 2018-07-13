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


# Constraint system
# Fahrenheit and Celsius convert:
# 9 * c = 5 * (f - 32)

# The adder function constructs an adder constraint over three connectors, where the first two must add to the third: a + b = c

from operator import add, sub

def adder(a, b, c):
    """The constraint that a + b = c."""
    return make_ternary_constraint(a, b, c, add, sub, sub)

# A multiplier is very similar to an adder

from operator import mul, truediv

def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

# define constant a value
def constant(connector, value):
        """The constraint that connector = value."""
        constraint = {}
        connector['set_val'](constraint, value)
        return constraint

def make_ternary_constraint(a, b, c, ab, ca, cb):
        """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
        def new_value():
            av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
            if av and bv:
                c['set_val'](constraint, ab(a['val'], b['val']))
            elif av and cv:
                b['set_val'](constraint, ca(c['val'], a['val']))
            elif bv and cv:
                a['set_val'](constraint, cb(c['val'], b['val']))
        def forget_value():
            for connector in (a, b, c):
                connector['forget'](constraint)
        constraint = {'new_val': new_value, 'forget': forget_value}
        for connector in (a, b, c):
            connector['connect'](constraint)
        return constraint

# Design the connector

def connector(name=None):
    """A connector between constraints."""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,
                    'set_val': set_value,
                    'forget': forget_value,
                    'has_val': lambda: connector['val'] is not None,
                    'connect': lambda source: constraints.append(source)}
    return connector


def inform_all_except(source, message, constraints):
        """Inform all constraints of the message, except source."""
        for c in constraints:
            if c != source:
                c[message]()


def converter(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [connector() for i in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')
converter(celsius, fahrenheit)

if __name__ == '__main__':
    fahrenheit['set_val']('user', 212)
    fahrenheit['forget']('user')
    fahrenheit['set_val']('user', 450)
    fahrenheit['forget']('user')
    celsius['set_val']('user', 37)
    # >>>
    # Fahrenheit = 212
    # Celsius = 100.0
    # Fahrenheit is forgotten
    # Celsius is forgotten
    # Fahrenheit = 450
    # Celsius = 232.22222222222223
    # Fahrenheit is forgotten
    # Celsius is forgotten
    # Celsius = 37
    # Fahrenheit = 98.6