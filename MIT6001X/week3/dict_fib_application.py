# if write a fibonacci number search function by recursion
# return the number at position n, if the number start from 1
# this code is considered as inefficient because it has to call the function twice in each recursion

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

numFibCalls = 0
print(fib(35))
print('called', numFibCalls, 'times')
# it repeatedly compute the fib(3), fib(2), and fib(1)
# use dict to avoid

def fib_e(n, d):
    global numFibCalls
    numFibCalls += 1

    if n in d:
        return d[n]
    else:
        ans = fib_e(n-1, d) + fib_e(n-2, d)
        d[n] = ans         # add calculated result of n > 2, to the dict
        return ans         # called memorization method

# set a base dict
numFibCalls = 0
d = {1: 1, 2: 2}
print(fib_e(35, d))  # the dict will become longer and longer during the run, calculation become faster
print('called', numFibCalls, 'times')




