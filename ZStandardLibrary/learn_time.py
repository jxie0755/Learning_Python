# time module
# https://docs.python.org/3/library/time.html#module-time

# Check the time length the python execution


import time

if __name__ == '__main__':
    start_time = time.time()
    # run main() codes
    print(f"--- {time.time() - start_time}s seconds ---\n")


# write into a fucntion
def time_spend(fn_to_check, *args, **kwds):
    import time
    start_time = time.time()
    result = fn_to_check(*args)
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

    time_spend(fib_gen_r, 35)
