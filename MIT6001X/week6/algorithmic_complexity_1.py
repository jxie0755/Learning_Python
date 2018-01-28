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

