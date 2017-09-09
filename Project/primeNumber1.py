# V1 allow to find any number in a range defined by user

def find_primes(n):
    primeList = []
    for x in range(2, n+1):
        isPrime = True
        for y in range(2, int(n**0.5) + 1):
            if x % y == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(x)
    print(primeList)

max = int(input('Find primes up to what numbers?:'))
find_primes(max)

