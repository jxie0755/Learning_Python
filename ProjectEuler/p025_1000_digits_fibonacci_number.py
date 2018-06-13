# P025 1000-digit Fibonacci number

# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144

# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fib(n):
    array = [0, 1, 1]
    if n == 1:
        return array[1]
    elif n == 2: 
        return array[2]
    else:
        for i in range(3, n+1):
            array.append(array[i-2] + array[i-1])
    return array[-1]

def count_fib_digit(length):
    n = 1
    while len(str(fib(n))) < length:
        n += 1
    return n

print(count_fib_digit(1000))
# >>> 4782
