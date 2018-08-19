# Obtained from CS61A Extra Class for Containers
# https://inst.eecs.berkeley.edu/~cs61a/sp18/extra.html

# This in a way introduced how some container objects (including some built-in) were made

#############
# Container #
#############

def box(contents):
    """Return a container that is manipulated by two functions."""
    def get():
        return contents
    def put(value):
        nonlocal contents
        contents = value
    return get, put

def make_box(contents):
    """Return a dispatch function representing a container.

    >>> c = make_box('Hello')
    >>> c('contents')
    'Hello'
    >>> c('put')('Goodbye')
    >>> c('contents')
    'Goodbye'
    """
    def dispatch(m):
        if m == 'contents':
            return contents
        if m == 'put':
            def put(value):
                nonlocal contents
                contents = value
            return put
    return dispatch

if __name__ == '__main__':
    print('CONTAINER - box:')

    get, put = box('Hello')
    print(get())
    # >>> 'Hello'
    put('Goodbye')
    print(get())
    # >>> 'Goodbye'

    c = make_box('Hello')
    print(c('contents'))
    # >>> 'Hello'
    c('put')('Goodbye')
    print(c('contents'))
    # >>> 'Goodbye'

    print('-------------------------')

# A bot container is a pair of functions who controls put-in and take-out.
# the put function has no memory, therefore the box can only contain one item

########
# List #
########

def pair(x, y):
    """A pair (x, y)."""
    def dispatch(m):
        if m == 'first':
            return x
        elif m == 'second':
            return y
    return dispatch

# Summary:
# This is to create a list as a function, which contains two elements as a pair
# It is a nested pair, that the second elemetn is a new pair which also contains two elements
# It is a linked-list structure, similar to tree object.

nil = None

def append(s, x):
    """Append value x to the end of a sequence s."""
    if s is nil:
        return pair(x, nil)
    else:
        first, second = s('first'), s('second')
        return pair(first, append(second, x))

# This is to add an element by creating a new pair in the very last nested pair, at the second item.
# And it is appended to the list, it leaves an opening (nil as the second element, so that for further appending)

def list_print(s):
    """A printing representation of a list."""
    print('[', end='')
    comma = False
    while s is not nil:
        if comma:
            print(', ', end='')
        first, s = s('first'), s('second')
        print(first, end='')
        comma = True
    print(']')

# Summary:
# This is to print a number of strings (use end='' to ensure one lineer)
# use while loop to iterate all sub-pairs as the second item of a pai

# Non recursion
def list_len(s):
    length = 0
    while s is not nil:
        s = s('second')
        length += 1
    return length

# Simple recursion way
def list_len(s):
    """Length of a list."""
    if s is nil:
        return 0
    else:
        return 1 + list_len(s('second'))

def list_get(s, i):
    """Return element i of list s."""
    if i == 0:
        return s('first')
    else:
        return list_get(s('second'), i-1)

def list_sub(s, i, v):
    """Return a copy of s with element i replaced by v."""
    if i == 0:
        return pair(v, s('second'))
    else:
        return pair(s('first'), list_sub(s('second'), i-1, v))

def make_list():
    """Return a dispatch function representing a list."""
    s = make_box(nil)
    def dispatch(m):
        if m == 'append':
            return lambda x: s('put')(append(s('contents'), x))
        elif m == 'len':
            return list_len(s('contents'))
        elif m == 'get':
            return lambda i: list_get(s('contents'), i)
        elif m == 'set':
            return lambda i, v: s('put')(list_sub(s('contents'), i, v))
        elif m == 'print':
            return list_print(s('contents'))
    return dispatch

# Summary:
# Same idea as box, use dispatch function to pack all list functions together.
# But the idea of list is achieved by developing the box by using put and content keyords.

if __name__ == '__main__':
    print('CONTAINER - List:')

    L1 = pair(1, nil)
    L2 = append(L1, 2)

    print(L2('first'))
    # >>> 1
    print(L2('second')('first'))
    # >>> 2

    # L2 相当于:
    L2B = pair(1, pair(2, nil))

    # Print list
    list_print(L2)  # >>> [1, 2]
    list_print(L2B) # >>> [1, 2]

    s = pair(3, pair(4, pair(5, nil)))
    print(list_len(s)) # >>> 3
    print(list_get(s, 1)) # >>> 4
    list_print(list_sub(s, 1, 6)) # >>> [3, 6, 5]


    c = make_list()
    c('print')
    # >>> []
    c('append')(3)
    c('append')(4)
    c('append')(5)
    c('print') # >>> [3, 4, 5]

    print(c('len')) # >>> 3
    print(c('get')(2)) # >>> 5

    c('set')(1, 6)
    c('print') # >>> [3, 6, 5]


    print('-------------------------')

########
# Dict #
########

def make_dict():
    """Return a dispatch function representing a dict."""
    s = make_list() # A list of (key, value) pairs
    def lookup(k):
        """Return the index for a key."""
        for i in range(s('len')):
            if s('get')(i)('first') == k:
                return i
    def set(k, v):
        """Set or add v as the value for key k."""
        i = lookup(k)
        if i is None:
            s('append')(pair(k, v))
        else:
            s('set')(i, pair(k, v))
    def dispatch(m):
        if m == 'get':
            return lambda k: s('get')(lookup(k))('second')
        elif m == 'set':
            return set
        elif m == 'items':
            return s
    return dispatch

# Summary
# The dictionary is devloped based on the list, instead of storing a value as the first element in a pari, it stores a pair as the first element of a pair, which links key and value.

# So the dictionary is still a nested pair which both the first element and second element is a pair.
# The first element stores keys and value,/
# The second element is nested to store next pair.
# i.e.:  pair(pair('I', 1), pair(pair('V', 5), pair(pair('X', 10), nil)))

if __name__ == '__main__':
    print('CONTAINER - Dictionary:')

    d = make_dict()
    d('set')('I', 1)
    d('set')('V', 5)
    print(d('get')('V'))
    # >>> 5

    d('set')('X', 10)
    d('set')('V', 'five')
    print(d('get')('V'))
    # >>> 'five'
    print(d('items')('len'))
    # >>> 3

    # Essentially it is:
    D1 = pair(pair('I', 1), pair(pair('V', 'five'), pair(pair('X', 10), nil)))
    list_print(D1)
    # >>>
    # [<function pair.<locals>.dispatch at 0x00000241D3199510>, <function pair.<locals>.dispatch at 0x00000241D3199840>, <function pair.<locals>.dispatch at 0x00000241D31999D8>

    print(list_len(D1)) # >>> 3

    print(list_get(D1, 1)('first'))   # >>> V     # The Key
    print(list_get(D1, 1)('second'))  # >>> five  # The Value

    print('-------------------------')

#########################
# Dispatch Dictionaries #
#########################

def box_dict(contents):
    """Return a dispatch function representing a container."""
    def put(value):
        d['contents'] = value
    d = {'contents': contents, 'put': put}
    return d

# Summary
# This is to make a box as one dictionary with two keys.
# The first key tied to the content, the second key tied to the function to put content


if __name__ == '__main__':
    print('CONTAINER - Box by Dictionary:')

    c = box_dict('Hello')
    print(c['contents'])
    # >>> Hello
    c['put']('Goodbye')
    print(c['contents'])
    # >>> Goodbye

    print('-------------------------')

#######################
# Constraint Networks #
#######################

def connector(name=None):
    """A connector between constraints.

    >>> celsius = connector('Celsius')
    >>> fahrenheit = connector('Fahrenheit')
    >>> converter(celsius, fahrenheit)

    >>> celsius['set_val']('user', 25)
    Celsius = 25
    Fahrenheit = 77.0

    >>> fahrenheit['set_val']('user', 212)
    Contradiction detected: 77.0 vs 212

    >>> celsius['forget']('user')
    Celsius is forgotten
    Fahrenheit is forgotten

    >>> fahrenheit['set_val']('user', 212)
    Fahrenheit = 212
    Celsius = 100.0
    """
    informant = None  # The source of the current val
    constraints = []  # A list of connected constraints

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

def ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b)=a."""
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

from operator import add, sub, mul, truediv

def adder(a, b, c):
    """The constraint that a + b = c."""
    return ternary_constraint(a, b, c, add, sub, sub)

def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return ternary_constraint(a, b, c, mul, truediv, truediv)

def constant(connector, value):
    """The constraint that connector = value."""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def converter(c, f):
    """Connect c to f to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)
