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

P = genPrimes()
print(type(P))
for i in range(20):
    print(next(P))

