from ZStandardLibrary.learn_time import time_spent

def fib_gen_r(i):
    """
    Fibonacci function generator
    generate the fibonacci number at 'i'th posistion
    """
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib_gen_r(i - 1) + fib_gen_r(i - 2)

time_spent(fib_gen_r, 35)
