# Logistics
# First unlock some tests:
# python3 ok -u

# Part I: The reader

# Problem 1 > Suite 1 > Case 1
# -- Already unlocked --


# Problem 1 > Suite 1 > Case 2
from scheme_reader import *
tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
src = Buffer(tokens)

src.current()
# >>> '('

src.remove_front()
# >>> '('

src.current()
# >>> '+'

src.remove_front()
# >>> '+'

src.remove_front()
# >>> 1

scheme_read(src)  # Returns and removes the next complete expression in src
# >>> Pair(23, Pair(4, nil))

src.current()
# >>> ')'


# Problem 1 > Suite 1 > Case 3
from scheme_reader import *

scheme_read(Buffer(tokenize_lines(['(23 4)'])))
# >>> Pair(23, Pair(4, nil))

read_line('(23 4)')  # Shorter version of above!
# >>> Pair(23, Pair(4, nil))


# Problem 1 > Suite 1 > Case 4
from scheme_reader import *

read_tail(Buffer(tokenize_lines([')'])))
# >>> nil

read_tail(Buffer(tokenize_lines(['1 2 3)'])))
# >>> Pair(1, Pair(2, Pair(3, nil)))

read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
# >>> Pair(2, Pair(Pair(3, Pair(4, nil)), nil))


# Problem 1 > Suite 1 > Case 5
# -- Already unlocked --


# Problem 1 > Suite 1 > Case 6
# -- Already unlocked --


# Problem 1 > Suite 1 > Case 7
read_line("(+ (- 2 3) 1)")
# >>> Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
# 相当于一个分叉链表


# Problem 1 > Suite 1 > Case 8
# -- Already unlocked --

# OK! All cases for Problem 1 unlocked.



# Problem 2 > Suite 1 > Case 1 - Case 4, Case 6-8 omitted
from scheme_reader import *

read_line("(a . b)")
# >>> Pair('a', 'b')

read_line("(a b . c)")
# >>> Pair('a', Pair('b', 'c'))

read_line("(a b . c d)")
# >>> Syntax Error   # 若'.'不在末尾, 则不行, 必须是 (a (b . c) d)

read_line("(a . (b . (c . ())))")
# >>> Pair('a', Pair('b', Pair('c', nil)))  # 就是标准链表

read_line("(a . ((b . (c))))")
# >>> Pair('a', Pair(Pair('b', Pair('c', nil)), nil))  # 双括号则又相当于分叉链表了

# OK! All cases for Problem 2 unlocked.






# Part II: The evaluator

# Understanding scheme.py > Suite 1 > Case 1 - Case
# Q: A Scheme expression can be either...
# A: A primitive expression or a list expression

# Q: What expression in the body of scheme_eval finds the value of a name?
# A: env.lookup(expr)

# Q: How do we know if a given list expression is a special form?
# A: Check if the first element in the list is a symbol and that that symbol is in the dictionary SPECIAL_FORMS

# Q: What exception should be raised for the expression (1)?
# SchemeError("1 is not callable")


# Problem 3 > Suite 1 > Case 1
from scheme import *
global_frame = create_global_frame()
global_frame.define("x", 3)
global_frame.parent is None
# >>> True

global_frame.lookup("x")
# >>> 3

global_frame.define("x", 2)
global_frame.lookup("x")
# >>> 2

global_frame.lookup("foo")
# >>> SchemeError

# Problem 3 > Suite 1 > Case 2
from scheme import *

first_frame = create_global_frame()
first_frame.define("x", 3)
second_frame = Frame(first_frame)
second_frame.parent == first_frame
# >>> True

second_frame.lookup("x")
# >>> 3


# Problem 4 > Suite 1 > Case 1
from scheme import *

env = create_global_frame()
twos = Pair(2, Pair(2, nil))
plus = PrimitiveProcedure(scheme_add) # + procedure
scheme_apply(plus, twos, env) # Type SchemeError if you think this errors
# >>> 4

env = create_global_frame()
twos = Pair(2, Pair(2, nil))
oddp = PrimitiveProcedure(scheme_oddp) # odd? procedure
scheme_apply(oddp, twos, env) # Type SchemeError if you think this errors
# >>> SchemeError


