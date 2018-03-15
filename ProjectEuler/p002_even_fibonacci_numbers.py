# P002 Even Fibonacci numbers


# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# use generator in fibonacci function
# but modify the while loop condition to limit maximum value at 4000000
def genFib_PE002():  # this created a generator for fibonacci numbers
    a, b = 0, 1
    # yield a  # no need to yield 0
    # yield b  # cancel yield b because it is not even
    while a + b <= 4000000:
        next = a + b
        if next % 2 == 0:  # also add a condition to only generator fib numer that is even
            yield next
        a, b = b, next

print(list(genFib_PE002()))
# >>> [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]
print(sum(genFib_PE002()))
# >>> 4613732
# passed
