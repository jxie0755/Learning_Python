# Best case and worst case

# Exercise 1
# Function 1
def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

# Express your answer in terms of n, the number of elements in the list L
# Best case: list is empty, so (1 op), return False
# Worst case: x not in L, so go through every element in L (n op), then check each time if e==x, (n op), then return False (1 op), in total: 2n+1

# Exercise 2
# Function 1
def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total

# Express your answer in terms of n, the size of the input x
# Best case: set total (1 op), i in range (1000), (1000 op), total+=1 (2000 op), check x <= 0 (1 op), return (1 op), total 3003
# Worst case: same as best case, but iterate x, by checking (1n), x -= 1 (2n), total change (2n), total 5n + 3003

# Fucntion 2
def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x = x//2
        total += x

    return total

# Express your answer in terms of n, the size of the input x
# Best case: before while loop (2001 op), if x < 0 (1 op), then return (1 op), total 2003
# Worst case:2001 op + check x (1+n/2) + calculate x (n/2) + total change (n/2), then return, total 3/2*n + 2003


# Function 3
def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)

# Express your answer in terms of n, the number of elements in the list L.
# Best case: 3 op for empty list
# Worst case: 2 op + for loop 1 (3n) + for loop 2 (4n), total 7n + 2


# Exercise 3
# Function 1
def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples

# Express your answer in terms of n, the number of elements in the list L
# Best case: List is empty, 2 ops
# Worst case: double for loop, each step 3 ops, therefore 3n^2 + n + 2
# Complexity: O(n^2)


# Function 2
def program2(L):
    squares = []
    for x in L:
        for y in L:
            if x == y:
                squares.append(x*y)
    return squares

# Express your answer in terms of n, the number of elements in the list L
# Best case: List is empty: 2 ops
# Worst case: one more step in double for loop than previous, 4 steps in the for loop 4n^2 + n + 2
# Complexity: O(n^2)


# Function 3
def program3(L1, L2):
    intersection = []
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection

# Express your answer in terms of n, the number of elements in the list L1 (assume len(L1) == len(L2)
# Best case: both L1 L2 empty, 2 ops
# Worst case: still double loop one iteration one check elt in List, but not nested, therefore n^2 + 2n + 2
# Complexity: O(n^2)


# A function to transfer integer to a string O(log(n))
def intToStr(i):
    """i is a poositive integer"""
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i //= 10
    return result
# as integer become larger, every 10 times, one more digit will be shown, means one more op.
# actually o(n) as to numbers of digits, but this is not the input size.

# A function to calculate the sum of a string made of digits O(n)
def addDigits(s):
    """s is a string of digits"""
    val = 0
    for c in s:
        val += int(c)
    return val
# strings gets longer, more digits will be added, linear complexity
# a loop with constant number of operation

# A function to calculate factorial recursively O(n)
def fact_iter(n):
    val = 1
    for i in range(1, n+1):
        val *= i
    return val
# obviously linear

def fact_recur(n):
    """assume n>= 0, integer"""
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)
# still linear even if it is recursive

# A quadratic function to verify if L1 is a subset of L2 O(n^2)
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
# nested loop found

# Exponential complexity, most expensive type
# A function that could be exponential (Tower of Hanoi) is typically a function that more than one recursive call.
def genSubset(L):
    """L as a list"""
    res = []
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = genSubset(L[:-1])  # the list without last element
    extra = L[-1:]  # a list of just the last element
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

print(genSubset([1,2,3]))  # >>> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# O(2^n)



