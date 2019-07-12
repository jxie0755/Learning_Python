# Asterisk is used different in def statement and actual code application.
# in def statement, it allows function to carry multiple arguments
# in code application, it force to unpack the iterable variables

def asterisk(*args): # this allows carry multiple arguments
    print(*args)  # this does not pack args into a single items
    # because print let you carry multiple args as well
    # can not use:
    # return *args

asterisk(1,2,"a","b")
# >>> 1 2 a b
# this allows to process each arg individually

asterisk([1,2,"a","b"])
# >>> [1, 2, "a", "b"]
# if a iterable get passed in, it will be treated like a single item

asterisk(*[1,2,"a","b"])
# this is basically equals to asterisk(1,2,"a","b")
# as it unpacks before execution
# >>> 1 2 a b


def asterisk2(*args): # this allows carry multiple arguments
    return args  # this forced pack of args into a number of single items (tuple)

a = asterisk2(1,2,"a","b")
print(a)
print(type(a))
# >>> (1, 2, "a", "b")
# >>> <class "tuple">
# this forced all individual items to pack

b = asterisk2([1,2,"a","b"])
print(b)
# >>> [1, 2, "a", "b"] # same, a tuple with one list item.
# even if the arg is a single packed iterable, it will add another layer of package on it ([1, 2, "a", "b"])

print(asterisk2(*[1,2,"a","b"]))
# Note! You must use * in def as the excution will unpack, it functio must allow multiple args in the first place!
# Again, equal to asterisk2(1,2,"a","b"), as it forced to break down the list into individual args.
# But then force to pack back into a tuple
# >>> (1, 2, "a", "b")


# Example for *args in iteration:
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    """

    def __init__(self, *args):
        "*** YOUR CODE HERE ***"
        self.buttons = {a.pos: a for a in args}  # do not use * in iteration.


class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0


b1 = Button(0, "H")
b2 = Button(1, "I")
k = Keyboard(b1, b2)
print(k.buttons[0].key)




# double asterisk for keyword arguments
def keyword(**kwargs):
    print(kwargs)

keyword(first="A", second="B", fourth="C", third="D", fifth="E")
# >>>
# {"first": "A", "second": "B", "fourth": "C", "third": "D", "fifth": "E"}
# kwargs output a dictionary


def keyword(**kwargs):
    return kwargs

a = keyword(first="A", second="B", fourth="C", third="D", fifth="E")
print(a)
# >>> {"first": "A", "second": "B", "fourth": "C", "third": "D", "fifth": "E"}
print(type(a))
# >>> <class "dict">
