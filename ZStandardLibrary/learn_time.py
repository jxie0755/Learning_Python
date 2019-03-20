# time module
# https://docs.python.org/3/library/time.html#module-time

# Check the time length the python execution


import time

# For direct use
if __name__ == '__main__':
    start_time = time.time()
    # run main() codes
    print(f"--- {time.time() - start_time}s seconds ---\n")

# write into a fucntion
def time_spent(fn_to_check, *args, **kwds):
    start_time = time.time()
    result = fn_to_check(*args, **kwds)
    print(result)
    print(f"--- {time.time() - start_time}s seconds ---\n")



if __name__ == '__main__':

    # testing function
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

    time_spent(fib_gen_r, 10)

    def foo(a,b,c, d=0,e=5):
        return a, b, c, d, e

    time_spent(foo, 1,2,3,e=5)
    # >>>
    # (1, 2, 3, 0, 5)
    # --- 0.0sseconds - --



