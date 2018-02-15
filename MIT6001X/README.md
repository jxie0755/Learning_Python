MIT公开课 Introduction to Computer Science and Programming Using Python (python3)
edX: Introduction to Computer Science and Programming Using Python

https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/course/

Week 1 Python Basics

Lecture 1

* Learn how to think like a computer scientist, make computer to do your work.
* Computer, fundamentally, only does two things
    * simple calculation
        * built-in the language
        * define by people as program
    * remember things
* NEED Algorithm to help
    * Example (simple calculation is not good enough)
        * search on the web (45B pages, 1000 words/page, 10 operations/word)
            * with simple calculation need 5.2 days to get result
        * play chess (35 move, look ahead 6 move, 1.8b boards to check, 100 operation/choice)
            * 30 min each move
    * Can't store the whole information for a lot of things (chess games)
* Limitation1
    * some problems are still to complex
    * some problems are fundamentally impossible to compute
* Two types of knowledge
    * declarative knowledge
        * statement of fact
    * imperative knowledge
        * a recipe of 'how to', mechanical to get things done
    * example
        * statement of fact:  sqrt of x is y, such y*y = x.
        * recipe
            * guess a number: g
            * if g*g is close enough to y, stop and say g is the answer
            * otherwise, make a new guess by averaging g and x/g
            * use the new g, repeat until close enough
            *
* Algorithm
    1. sequence of simple steps
    2. flow of control process that specifies when each step is executed
    3. a means to determine when to stop
*   Computers are machines
    * how to capture a recipe in a mechanical process
    * fixed program computer
        * calculator
        * Alan Turing's Bombe (to break German's code during world war II)
    * stored program computer - what we seen
        * machine stores and executes instructions
        * can load different programs
        * have a interpreter
        *
* programming is about how to write the sequence of instructions for computer to run one after one.
    * Turing proved that with 6 primitives, you can computer anything: move left, move right, read, write, scan, do nothing.
    * modern programming language: abstract methods to create new primitives.
    * anything computable in one language is computable in any other programming language
* how to program?
    * a programming language provides a set of primitive operations
    * expressions are complex but legal combinations of primitives in a programming language
    * expression and computations have values and meanings in a programming language
* programming language
    * primitive constructs: numbers, strings, simple operators
    * syntax (语法)
        * cat dog boy - X, cat hugs boy - O.
        * "hi'5 - X, 3.2*5 - O
    * static semantics (语意)
        * I are hungry - X (符合语法,但是语意不对)
        * 3 + "hi" 同上
    * Semantics
        * is the meaning associated with a syntactically correct string of symbols with no static semantic errors.
    * 人类语言可以出现一语双关, 机器语言不可能,但是你写的语意也有可能不是你真正要表达的意思.
    * bugs:
        1. 语法错误,容易找出
        2. 语意错误,容易找出
        3. 没有错误,但是不符合意图 - 出现死机,无限循环,或者错误结果 - 最难修复


* LEARNING python!!
    * write in the shell
        * python console, read what you write and send it to the interpreter
    * store in a file
        * a file that is written and saved and be read by the interpreter anytime.
    * data object
        * every object has a type
        * scalar objects (cannot be subdivided)
            * integers
            * float
            * bool - Boolean values True and False
            * NoneType - special and has one value: None
            * use type() method to see the type of an object
            * can change type
        * non-scalar objects (have internal structure that can be accessed)
            * list
            * tuple
            * dictionary
        * UNDERSTAND: print returns NONE! print return no value, it just print.
    * simply calculation
        * operator
        * calculation sequence
    * variable
        * assign name to the values
        * name should be informative
        * var = var + 1, equal to var += 1 (called incrementing)
        * keywords can not be used as variables
    * comparison
        * >, <, >=, <=, ==, !=
        * and, or, not a
    * branch program
        * if, else, elif
        * condition can be nested (branch in branch)

Lecture 2

* Strings
    * combination(concatenation): use +
    * also * : 'string' * 3 = 'stringstringstring'
    * lent() include the space counting
    * 'string'[0:n]: string is slicable (from 0 to -1).
    * 'string'[::n] '::'不是反向,如果n是负数才是反向
    * print by ',' and '+'
    * input include everything as a string (包括引号和斜杠\,",')
* Branching
    * for loop
    * while loop
* Iteration (Fist class of Algorithm)
    * in most codes, we tend to use the for loop
    * we use while loop when there is going to be a condition that we can't predict, so that we can break the loop.
    * These are the first version of iterative algorithm
    * use while loop to generate the guess, then check with if condition.
        * A loop variable is initialized outside of the loop
        * Then it should change within the loop
        * Test for termination depends on the variable.

Week 2 Simple Programs

Lecture 1

* Simple Algorithms
    * example
        * finding the square root of a number: keep finding the answers that is close enough for the number.
        * You need to define what is close is enough (x**2 - target <= epsilon). If the difference is small enough, then it is close enough
        * small epsilon will slow down program, but more accurate
    * strings are immutable type - can not be modified. 类似tuple, 不同于list
    * bisection search
        * a better method to narrow down the search
        * take looking for the sqrt of x as an example: if g**2=x, g should be somewhere between 1 and x.
        * do not have to start trying from 1.
        * find a middle point as g, if g**2>x, then find a new g between 1 and g.
        *
        *
    * Dealing with float's (how floats present real numbers, how machine store?)
        * Decimal number:  302 = 3*10^2 + 0*10^1 + 2*10^0
        * Binary number: 10011 = 1*2^4 + 0*2^3 + 0*2^2 + 1*2^1 + 1*2^0
        * But internally, computer only represent number in binary
        * if x =  1*2^4 + 0*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 10011 (由于前面每项都可以被2整除,除了最后一个2^0, 所以如果x%2,余数就是二进制数的最后一位
        * 以此类推 x/2 = 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0, 再次除以2,得到余数又是最后一位.
            * 对于floats 3/8 = 0.375 = 3*10^-1+7*10^-2+5*10^-3
            * 0.375*(2^n) = 3(decimal), n=3  (这里对于任何小数,都可以乘以一个足够大的2^n,使其变回一个十进制的整数
            * 3 变成 二进制就是 11(binary), 如果之前乘以2^4,就等于6,也就是110(binary)
            * 然后退回3个数位(之前乘以2^3),就成为0.011(binary), 就算是110(binary)退回4位也还是0.011
            * 有时候这个n会变得非常大,甚至不可得, 这就导致了float的数字转换到二进制,不是完全相等而是取近似值
            * 对比两个floats,不要用 x == y, 而是 abs(x - y) < epsilon.
            * print(float)不会出现问题
    * Newton-Raphson
        * an effective way of algorithm to find root in much less circling of looping

Lecture 2

* small pieces of codes
    * easy for small-scale problems
    * messy for larger problems
    * hard to keep track of details
* Good programming
    * length of code is not important
    * should be measured by functionality
    * introduce functions
* Functions
    * like a black box, don't know how it works
    * but know the interface: input/output
    * know the functionality.
    * mechanism to achieve decomposition and abstraction:
        * Abstraction: do not need to know how it works, but to use it
        * Decomposition: different devices work together to achieve an end goal
        * Work powerful together, and be used many times but only debugged once.
* Decomposition
    * Break a problem into different, self-contained, pieces
    * divide code into modules
        * self-contained
        * used to break up code
        * intended to be reusable
        * keep code organized
        * keep code coherent
* Abstraction
    * Suppress details inside a method, to compute from the use of that computation
        * cannot see details
        * do not need to, do not want to, see details
        * hide tedious codes
* Use Functions
    * not run in a program until called or invoked
        * has a name
        * has parameters (0 or more)
        * has a docstring (optional but recommended) (like a manual)
        * has a body
    * if function has no 'return', then it will return 'None'
        * better both print and return if needed
    * return vs. print
        * return
            * return only has meaning inside a function
            * can have multiple return inside function, but only one return executed inside a function
            * code inside function but after return statement will not be executed
            * has a value associated with it, given to function caller
        * print
            * print can be used outside functions
            * can execute many print inside a function
            * code after a print() can still be executed
            * has a value associated with it, outputted to the console
    * 注意global scope和function scope, 甚至function内还包含另一个function的scope
    * keyword arguments: 参数可以指定f(arg2=x, arg1=y), 如果用等号指定,那么参数顺序不对也没关系)
    * Specification("""docstring""") 必须要写
        * a contract between the implementer of a function and the clients who will use it
        * Assumptions: conditions that must be met by clients of the function. (typically constraints on values of parameters)
        * Guarantees: conditions that must be met by function, providing it has been called in manner consistent with assumptions
    * Recursion 递归
        * a way to design solutions to problems by divide-and-conquer or decrease-and-conquer
        * a programming technique where a function calls itself
        * in programming, the goal is NOT have infinite recursion
            * must have 1 or more base cases that are easy to solve
            * must solve the same problem on some other input with the goal of simplifying the larger problem input
        * help looping iteration
        * example: a*b as a + a + a ... b times
        * BREAK IT DOWN TO A SMALLER VERSION OF THE SAME PROBLEM!
        * because there is multiple scope in each recursion step, same variable can be used.
        * iteration vs recursion
            * recursion may be simpler, more intuitive
            * may be efficient for programmer but, may not be efficient for computer
        * verify recursion
            * first check the base
            * then assume a smaller parameter which would work, then by looping it will also return for larger parameter
        * example: towers of hanoi
            * 64 disks, moving one disk a time, big one must under small one, and how to move the whole pile. in 3 spaces.
        * example: fibonacci
            * two base, two recursions call
        * example of string (palindrome)
            * boolean can also be used in recursion.
* Modules and Files
    * modules contains multiple functions, stored as a *.py file.
    * use command import to invoke the module (import module)
    * invoke variable and functins
        * module.variable
        * module.function()
    * other ways to import
        * from module import * (import everything, no need to use "module." prefix)
            * only apply to the current scope, so you need to import many times when coding
    * file can be invoked by command 'open', open mode ('w', 'r', etc)
        * need to remember to close()
    * new way of opening "with open(xxx, 'w') as f_obj"

Week 3 Structured Types

Lecture 1

Data Structures
* Tuple
    * ordered sequence of elements
    * can mix element types
    * immutable (can not change element values) (like strings)
    * present as ( )
    * can be concatenated by tuple3 = tuple1 + tuple 2
    * if tuple[1] = ('one', ) the comma represents that this is a tuple (not any more)
    * tuple is iterable
* List
    * very similar to tuple, ordered sequence of information
    * difference is elements can be changed.
    * similar slice logic as tuple as well.
    * list methods (del, remove) (append, insert)
    * list methods (list, sort, reverse, sort and reverse)
        * range is a special procedure
        * returns something behaves like a tuple
        * generate the first item, and provide an iteration to make subsequent items
    * problems tricky to understand
        * list in memory
        * list are mutable
        * alias concept
        * change item in one name, will cause change in other names
            * sort() vs sorted
            * alias copy L1 = L2, and cloning L1 = L2[:]
* Method
    * python is formed by objects (nums, int, string, list, tuple, etc...)
    * object has functions and methods
    * method applied on the object use "." after that object.
    * concatenate L3 = L1 + L2
* function as object
    * first class objects
    * have types
    * can be elements of data structure like lists
    * can appear in expressions
        * as part of an assignment statement
        * as an argument to a function
    * particularly useful to use function as arguments when coupled with list
        * high order programming
* common operations
    * seq[i]
    * len()
    * seq1 + seq2 (not range)
    * n * seq     (not range)
    * seq[start:end]
    * e in seq
    * e not in seq
    * for e in seq

Lecture 2

* Dictionary
    * dictionary is essentially a customized indexed list, with keys used as index instead of just 0, 1, 2, 3, etc.
    * used curly braces { }
    * use key as a index to find a value dict[key] = value
    * dictionary is mutable
    * use 'in' for looking for key in a dict. (key in dict)
    * use 'del' to remove a key (del dict[key])
    * keys() method, to generate a list that contains all the keys
    * values() the same as above.
        * value
            * any type
            * can be duplicates
            * can be a data structure(list, tuple, even a dictionary)
        * keys
            * must be unique
            * immutable type (hashable)
            * careful with float type
            * no order until python 3.6
* memorization method
    * use dictionary to avoid repeated computation
    * set dictionary as a base and append new k,v into it, a long with the computation
* global variable
    * could be dangerous to use
        * breaks the scoping of variables by function call
        * allows for side effect of changing variable values in ways that affect other computations
    * but can be convenient when want to keep track of information inside a function


Mid-term exam

Week 4 Good Programming Practices

Lecture 1

Testing for bugs
* bugs in the soup
    * check soup for bugs
        * testing comes in!
    * keep lid closed
        * defensive programming
    * clean kitchen
        * eliminate source of bugs - debugging

* defensive programming
    * write specifications for function
    * Modularize programs
    * Check conditions on inputs/outputs (assertions)
        * Testing/Validation
            * compare input/output pairs to specification
            * "it is not working"
            * "How can I break my program?"
        * Debugging
            * Study events leading up to an error
            * "Why is it not working?"
            * "How can I fix my program?"
        * Set yourself up for easy testing and debugging
            * from the start design code to ease this part
            * break programs into modules that can be tested and debugged individually
            * document constraints on modules
                * what do you expect the input to be? the output to be?
            * document assumptions behind code design
    * Classes of tests
        * Unit testing
            * valid each piece of programs
            * testing each function seprately
        * Regression testing
            * add test for bugs as you find them in a function
            * catch reintroduced errors that were previously fixed
            * do multiple Unit and Regression test
        * Integration testing
            * does overall program work?
            * tend to rush to do this
    * Testing approaches
        * intuition about natural boundaries to the problem
        * if no natural partitions, might do random testing
        * black box testing
            * explore paths through specification
            * assumes a variety of cases
        * glass box testing
            * explore paths through code


def sqrt(x, eps):
    """
    :param x: floats, x >= 0
    :param eps: floats, eps > 0
    :return: Returns res such that x-eps <= res*res <= x + eps
    """
# black box testing
# designed without looking at the code, can be done by anyone, other than the programmer
# testing can be reused if implementation changes
# paths through specification
    # build test cases in different natural space partitions
    # also consider boundary conditions (empty lists, singleton list, large numbers, small numbers)

# test boundary:
# boundary: x = 0
# Perfect square: x = 25
# Less than 1: x = 0.05
# Irrational square root(imperfect): x = 2
# extremes: large epslon
# extremes: small eplon
# large number


# glass box testing
# use code directly to guide design of test cases
# called path-complete if every potential path through code is tested as leaset once
# what are the drawbacks of this type of testing?
    # can go through loops arbitrarily many times
    # missing pathts
# guildelines
    # branches - exercise all parts of a conditional
    # for loops - loop not entered, body of loop executed exactly once, or more than once
    # while loops - same as for loops, cases that catch all ways to exit loop
* Runtime Bugs
    * Overt vs Covert:
        * Over has an obvious manifestation - code crashes or runs forever
        * Cover has no obvious manifestation - returns a value which may be incorrect but hard to determine
    * Persistent vs Intermittent
        * Persistent: occurs everytime
        * Intermittent: only occurs some times, even if run on same input (maybe some other factors/time)
    * Obert and Persistent
        * obvious to detect, use defensive programming, if error is made, bug will fall into this category
    * Overt and intermittent
        * more frustrating, harder to debug, need to find the condition that reproduce the bug
    * Covert
        * highly dangerous, as may not realize for a long period.
* debug strategy
    * use print statement
        * when enter function
        * check argument
        * function results
    * use bisection method
        * put print halfway in code
        * decide where the bug is.
    * common error message
        * IndexError - Index exceed the range
        * TypeError - object not the right type for this function/method
        * NameError - nonexistent variable
        * SyntaxError - wrong syntax
    * look for explanation for incorrect behavior
        * add print() bisection ways

Lecture 2

Exception and Assertions
* Exception
    * when hit an unexpected condition
        * NameError - local or global name not found
        * TypeError - operand doesn't have correct type
        * SyntaxError - python can't parse program
        * AttributeError - attribute reference fails
        * ValueError - operand type okay, but value is illegal
        * IOError - IO system reports malfunction (like file not found)
    * what to do
        * fail silently
            * substitue default value or just continue
            * bad idea! user gets no warning
        * return an 'error' value
            * what value to choose?
            * complicates code have to check for a special value
        * stop execution, signal error condition
            * in python, raise an exception
    * use try...except command
        * try a code
        * if exception raise, to do the except part of the code
        * except does not need a specific value
        * try:
    xxx
except:
    xxx
        * or use except 'SpecificErrorName'
        * can use multiple except command
        * can also use else and finally
            * else - body of this is executed when execuation of associated try body completes with no exceptions
            * finally - body of this is always executed after try, else and except clauses.
    * Can subjectively raise an exception
        * raise <exceptionName> (<arguments>)
        * raise ValueError ('something is wrong)
    * Assertions
        * want to be sure that assumptions on state of computation are expected
        * use assert statement
        * an example of good defensive programming
        * don't allow program to control repsponse to unexpected conditions
        * ensure that execution halts when an expected condition is not met
        * typically used to check inputs to functions
        * can be used to check outpus
        * can make it easier to locate a source of a bug
            * where to use?
                * use as a supplement to teting
                * raise exceptions if users supplies bad data input
                * use to
                    * check types of args
                    * check that invariants on data structure are met
                    * check constrains on return values
                    * check for violations of constraints on procedure

Week 5 Object Oriented Programming

Lecture 1

Switch to manufacturer side, but creating new type of object, other use what was given.

Python built-in object types:
* integer
* floats
* strings
* lists
* and others etc.

Each object is an instance of its class, and it carries:
* type
* internal data representation
* a set of procedures for interaction with the object

Everything in Python is an object and has a type, and these objects are a data abstraction that capture:
* internal representation through daa attributes
* interface for interacting with object through methods

Objects can be created by new instance and destroyed by "del" command or just forget about them, and let Python reclaim destroyed or inaccessible - a process called "garbage collection".

Example:
list as L = [1,2,3,4]
how is it represented internally? it is a linked list of cells.

This is internal!

And it has a few method to be manipulated: len(), slice[], min(), max(), .append(), etc. We use these methods to manipulate without knowing the internal representations.

Creating a class:
* Name of the class
* attributes of the class
* give methods

Why do this?
* bundle data into packages together with procedures that work on them through well-defined interfaces
* divide-and-conquer development
    * implement and test behavior of each class separately
    * increase modularity reduces complexity
* makes it easy to reuse code

class Coordinate(object):  # object is parent class
    <define attributes here>

two type of attributes:
* data attributes (attribute)
* procedural attributes (method)

__ini__() define how to create an instance of object.
self is used for binding the attributes with the object

Two way of Calling method:


__str__() special method to represent the object in a string.
together with __repr__() another special method
difference between __str__() and __repr__() is __str__ is for user to read, __repr__ is for python to read:
Example - coordinate (3,4):
__str__ : <3,4>
__repr__: Coordinate(3,4) when repr gets run as a command, will create this object.

Power of OOP
* bundle together objects that share common attributes
* use abstraction to make a distinction between how to implement an object vs how to use the object
* build layers of object abstractions that inherit behaviors from other classes of objects
* create our own classes of objects on top of Python's basic classes.

OOP way of coding:
implementing the class:
    * define class
    * define attributes and methods
using the class:
    * creating instances
    * do operation with instances

ALWAYS USE GETTER AND SETTER to access data and method in a class.

Instance variable and Class variable
* Instance variable is defined in __init__, only exist when instance are created
* Class variable should be defined outside of __init__


Lecture 2

Lecture 2 introduced more OOP examples for classes hierarchy and inheritance, by:

Example 1 People structure:
* Creating a superclass Person(object)
* Creating a subclass MITPerson(Person)
* Creating a subclass Student(MITPerson)
* Creating UG(Student), Grads(Student), TransferStudent(Student)
* Creating Professor(MITPerson)

Example 2 Grade Book:
* Creating a class Grade(object)
* Giving functions to add student, grades and export grades, etc.

Generator
* any procedure or method with yield statement called generator
* separates the concept of computing a very long sequence of objects, from the actual process of computing them explicitly
* allows one to generate each new objects as needed as part of another computation (and throw it away after using it)
* range() is a generator that creates a range of numbers
* for fibonacci example: if you need 12th number of a fib list, you just go to the 12th one, instead of creating a long list of fib numbers first, then ask for the 12th one.

Week 6 Algorithmic Complexity

Lecture 1

* Some algorithms are faster than the others, we need to decide the efficiency of the algorithm
* Time and Space are sometimes traded. (to store data to save time to calculate)
* Focus on time
* How to evaluate?
    * Measure with a timer
        * not just measuring algorithm
        * but also measuring the speed of computer
    * Count the operations
        * count depends on implementations
        * no real definition of which operation to count
    * Abstract notion of order of growth - focus on this
        * best case, worst case, average case
        * worst case more useful, gives estimation on worst possible situation - generally focus on
    * Orders of growth - goals:
        * evaluate when input is very big
        * express the growth of program's runtime as input size grows (input size vs. time)
        * want to put a upper bound on growth
        * do not need to be exact: just the order of growth not exact growth
        * look at the largest factors in runtime
        * types of growth:



* Big 'O' notation, expressed as 'O()'
    * Measures an upper bound on the asymptotic growth (order of growth)
    * Describe worst case
        * Worst case often occurs, and is the bottle neck when a program runs
        * Express the rate of growth of program relative to input size
        * only evaluate algorithm, not machine or implementation
* Quick example:


    * this function computes the factorial of a number
    * number of steps: 1 + 5n + 1 as 5n + 2
    * worst case asymptotic complexity
        * ignore additive constants
        * ignore multiplicative constant
        * called linear or order n algorithm: o(n)
    * focus on dominant terms
        * n^2 + 2n + 2 -- O(n^2)
        * n^2 + 10000n + 3^1000 -- O(n^2)
        * log(n) + n + 4 -- O(n)
        * 0.0001 * n * log(n) + 300n -- O(n*log(n))
        * 2n^30 + 3^n -- O(3^n)


* Analyzing programs and complexity
    * Combine complexity classes
        * analyze statements inside functions
        * apply some rules, foucs on dominant term
    * Law of addition for O()
        * used with sequential statements
        * O(f(n)) + O(g(n)) = O(f(n)+g(n))
            * example: O(n) + O(n*n) = O(n+n*n) = O(n^2)
        * O(f(n)) * O(g(n)) = O(f(n)*g(n))  # nexted statements
            * example: O(n) * O(n) = O(n*n) = O(n^2)
    *  Complexity classes
        * O(1): very rare, but sometime a piece of codes can be, and doesn't exclude loop.
        * O(logn): binary/bisection search
        * O(n): searching a list to see if an element is present, etc.
        * O(n^c): nested loops
        * O(2^n): recursive function to call the function more than once in every return


Lecture 2

Lecture 2 introduces some algorithms used in searching and sorting applications

* search algorithm
    * method for finding an item or a group of items with specific properties within a collection of items.
* collection could be implicit, i.e. find a square root of a number
    * exhaustive enumeration
    * bisection search
    * Newton-Raphson
* collection could be explicit
    * finding a student record in a stored collection of student records
* Search algorithm
    * linear search
        * brute force search
        * list does not have to be sorted
    * bisection search
        * list must be sorted
        * divided into two  different implementations of the algorithm

    * retrieve a item in a list is O(1) constant time
        * homogeneous list (list[int])
            * Each item takes 4 bytes of memory space.
            * the ith item can be directly visited at 4*bytes area in the memory
            * so that no matter if the first or last time, to retrieve the item takes a constant amount of time
        * heterogeneous list
            * work like a linked-list
            * where we emumerate the list, and directly visit the memory like a homogenous list
            * and then that address will point to the value of the item (mapping)

    * When should we sort the list first so that we can use binary search method?
        * when SORT + O(log(n)) < (O(n), which Sorting < O(n) - O(log(n))
        * But that is never TRUE!!! because sorting is about O(n)
        * But one sort can be good for multiple search algorithm, so that makes sense again!
        * This is called amortize the cost
        * SORT + K*O(log(n)) < K*(O(n), when K is large, SORT is not important anymore
        * SO that is saying: SORTING is important


* Sorting methods
    * Monkey Sort (aka bogosort, stupid sort, permutation sort, shotgun sort)
        * keep randomly shuffle until it reaches to a sorted status
        * not a very good idea unless the sample size is small enough
        * complexity
            * best case O(n) for n = len(L)
            * worst case O(?), unbounded if really unlucky
    * Bubble Sort
        * compare consecutive paris of elements
        * swap them in pair so that becomes (small, large)
        * when reach to end of the list, start over again
        * stop when no more swap have been made fore a whole loop
    * Selection Sort
        * first step
            * extract the minimum element
            * swap it with element at index 0
        * subsequent step
            * in remaining sublist, extract minium element
            * swap it with the element at index 1
        * keep the left portion of the list sorted
            * at ith step, first i elements in list are sorted
            * all other elements are bigger than first i elements
    * Merge Sort
        * use a divide-and-conquer approach (recursion)
            * if list is of length 0 or 1, already sorted
            * if list has more than one element, split into two list and sort each
            * merge sorted sublist
                * look at first elements of each, move smaller to end of the result
                * when one list empty, just copy rest of other list
        * complexity
            * divide: O(log(n))
            * merge: O(n)
            * overall: O(n*log(n))
        * This is the fastest a sort can be



































