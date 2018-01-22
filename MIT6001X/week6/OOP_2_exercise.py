# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method:
# 2, 3, 5, 7, 11, ...

def genPrimes():
    i = 2
    while True:
        for x in range(2, i):
            if i % x == 0:
                i += 1
                break
        else:
            yield i
            i += 1

if __name__ == '__main__':
    P = genPrimes()
    print(type(P))
    for i in range(10):
        print(next(P))

def genPrimes2():
    i = 2
    while True:
        if all(i % x != 0 for x in range(2, i)):
            yield i
        i += 1

if __name__ == '__main__':
    print()
    P2 = genPrimes2()
    for i in range(10):
        print(next(P2))
