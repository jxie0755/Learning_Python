# Logistics
# First unlock some tests:
# python3 ok -u

# Part I: The reader

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

# Problem 1 > Suite 1 > Case 7
read_line("(+ (- 2 3) 1)")
# >>> Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
# 相当于一个分叉链表


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

# Problem 4 > Suite 1 > Case 2
env = create_global_frame()
twos = Pair(2, Pair(2, nil))
oddp = PrimitiveProcedure(scheme_oddp) # odd? procedure
scheme_apply(oddp, twos, env) # Type SchemeError if you think this errors
# >>> SchemeError


# Problem 5 > Suite 1 > Case 1
from scheme_reader import *
from scheme import *

expr = read_line('(+ 2 2)')
scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
# >>> 4

expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
# >>> 12

expr = read_line('(yolo)')
scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
# >>> SchemeError

# scm> (+ 2 3) ; Type SchemeError if you think this errors
# >>> 5

# scm> (* (+ 3 2) (+ 1 7)) ; Type SchemeError if you think this errors
# >>> 40

# scm> (1 2) ; Type SchemeError if you think this errors
# >>> SchemeError

# scm> (1 (print 0)) ; check_procedure should be called before operands are evaluated
# >>> SchemeError


# Problem 6 > Suite 1 > Case 1 - Case 2

# Q: What is the structure of the expressions argument to do_define_form?
# A: Pair(A, Pair(B, nil)), where:
#        A is the symbol being bound,
#        B is an expression whose value should be bound to A

# Q: What method of a Frame instance will binda value to a symbol in that frame?
# A: define


# Problem 6 > Suite 2 > Case 1 - Case 4

# scm> (define size 2)
# >>> size

# scm> size
# >>> 2

# scm> (define x (+ 2 3))
# >>> x

# scm> x
# >>> 5

# scm> (define x (+ 2 7))
# >>> x

# scm> x
# >>> 9

# scm> (eval (define tau 6.28))
# >>> 6.28


# Problem 7 > Suite 1 > Case 1

# Q: What is the structure of the expressions argument to do_quote_form?
# A: Pair(A, nil), where:
#        A is the quoted expression

# Problem 7 > Suite 2 > Case 1

# scm> (quote hello)
# >>> hello

# scm> 'hello
# >>> hello

# scm> ''hello
# >>> (quote hello)

# scm> (quote (1 2))
# >>> (1 2)

# scm> '(1 2)
# >>> (1 2)

# scm> (quote (1 . 2))
# >>> (1 . 2)

# scm> '(1 . (2))
# >>> (1 2)

# scm> (car '(1 2 3))
# >>> 1

# scm> (cdr '(1 2))
# >>> (2)

# scm> (car (car '((1))))
# >>> 1

# scm> (quote 3)
# >>> 3

# scm> (eval (cons 'car '('(4 2))))
# >>> 4

# Problem 7 > Suite 3 > Case 1
from scheme_reader import *

read_line(" (quote x) ")
# >>> Pair('quote', Pair('x', nil))

read_line(" 'x ")
# >>> Pair('quote', Pair('x', nil))

read_line(" (a b) ")
# >>> Pair('a', Pair('b', nil))

read_line(" '(a b) ")
# >>> Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))

read_line(" '((a)) ")
# Pair('quote', Pair(Pair(Pair('a', nil), nil), nil))


# Problem 8 > Suite 1 > Case 1
from scheme import *

env = create_global_frame()
eval_all(Pair(2, nil), env)
# >>> (0)

eval_all(Pair(4, Pair(5, nil)), env)  # 从末尾开始
# >>> (5)

# Problem 8 > Suite 2 > Case 1


# scm> (begin (+ 2 3) (+ 5 6))  # 从末尾开始
# >>> 11

# scm> (begin (define x 3) x)
# >>> 3

# scm> (begin 30 '(+ 2 2))
# >>> (+ 2 2)

# scm> (define x 0)
# >>> x

# scm> (begin 42 (define x (+ x 1)))
# >>> x

# scm> x
# >>> 1   # 之前定义了x=0


# Problem 9 > Suite 1 > Case 1

# scm> (lambda (x y) (+ x y)
# >>> (lambda (x y) (+ x y))


# Problem 10 > Suite 1 > Case 1

# scm> (define (f x y) (+ x y))
# >>> f

# scm> f
# >>> (lambda (x y) (+ x y))


# Problem 11 > Suite 1 > Case 1
from scheme import *

global_frame = create_global_frame()
frame = global_frame.make_child_frame(Pair('a', Pair('b', Pair('c', nil))), Pair(1, Pair(2, Pair(3, nil))))
global_frame.lookup('a') # Type SchemeError if you think this errors
# >>> SchemeError

frame.lookup('a')  # Type SchemeError if you think this errors
# >>> 1

frame.lookup('b')  # Type SchemeError if you think this errors
# >>> 2

frame.lookup('c')  # Type SchemeError if you think this errors
# >>> 3

# Problem 11 > Suite 1 > Case 2

from scheme import *
global_frame = create_global_frame()
frame = global_frame.make_child_frame(nil, nil)
frame.parent is global_frame
# >>> True


# Problem 12 > Suite 2 > Case 1
# scm> (define (outer x y)
# ....   (define (inner z x)
# ....     (+ x (* y 2) (* z 3)))
# ....   (inner x 10))
# >>> outer               # 只是一个定义方程

# scm> (outer 1 2)
# 相当于执行 (inner 1 10)
# (+ 10 (* 2 2) (* 1 3))
# >>> 17

# scm> (define (outer-func x y)
# ....   (define (inner z x)
# ....     (+ x (* y 2) (* z 3)))
# ....   inner)
# >>> outer-func

# scm> ((outer-func 1 2) 1 10)
# 相当于(inner 1 10), x为inner的参数, 所以是10
# (+ 10 (* 2 2) (* 1 3))
# >>> 17




# Special Forms

# Problem 13 > Suite 1 > Case 1

# Your interpreter should evaluate each sub-expression from left to right
# and if any of these evaluates to a false value, then #f is returned.
# Otherwise, it should return the value of the last sub-expression.
# If there are no sub-expressions in an and expression, it evaluates to #t

# scm> (and)
# >>> #t

# (and 1 False)
# >>> #f

# scm> (and (+ 1 1) 1)
# >>> 1
#

# scm> (and False 5)
# >>> #t

# scm> (and 4 5 (+ 3 3))
# >>> 6

# scm> (and True False 42 (/ 1 0))
# >>> #f
# 忽略error直接给False

# scm> (or)
# >>> #f

# scm> (or (+ 1 1))
# >>> 2

# scm> (or False (- 1 1) 1)  ; 0 is a true value in Scheme
# >>> 0

# scm> (or False)
# >>> #f

# scm> (define (t) True)
# >>> t

# scm> (or (t) 3)
# >>> #t

# scm> (or 5 2 1)
# >>> 5

# scm> (or False (- 1 1) 1)
# >>> 0

# scm> (or 4 True (/ 1 0))
# >>> 4


# Problem 14 > Suite 1 > Case 1
# scm> (cond ((> 2 3) 5)
# ....       ((> 2 4) 6)
# ....       ((< 2 5) 7)
# ....       (else 8))
# >>> 7

# scm> (cond ((> 2 3) 5)
# ....       ((> 2 4) 6)
# ....       (else 8))
# >>> 8


# Problem 15 > Suite 1 > Case 1
# The let special form binds symbols to values locally, giving them their initial values

# scm> (define x 1)
# >>> x

# scm> (let ((x 5))
# ....    (+ x 3))
# >>> 8

# scm> x
# >>> 1

# Problem 15 > Suite 1 > Case 2

# scm> (let ((a 1) (b a)) b)
# >>> 1
#
# scm> (let ((x 5))
# ....    (let ((x 2)
# ....          (y x))
# ....        (+ y (* x 2))))   # 此时y = 5, x = 2
# >>> 9


# Problem 16 > Suite 1 > Case 1
# A mu expression is similar to a lambda expression,
# but evaluates to a MuProcedure instance that is dynamically scoped

# scm> (define y 1)
# >>> y

# scm> (define f (mu (x) (+ x y)))
# >>> f

# scm> (define g (lambda (x y) (f (+ x x))))
# >>> g

# scm> (g 3 7)
# g is lambda fucntion (g 3 8) = f(+ 3 3) = f 6
# but when mu(x) look for y, y is found in last scope y=7 instead of y in global y=1.
# therefore, f(6) = 6 + 7 = 13
# >>> 13

# In Python:
y = 5

def foo(bar):
    y = 10
    return bar()

def bar():
    return y

print(foo(bar)) # >>> 5
# not 10, because it does not look scope up, but start from global
# it will raise error if can't find y in global, instead of binding to 5




# Part III: Write Some Scheme
# See questions.scm
