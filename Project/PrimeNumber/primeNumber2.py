# To tell if a number is prime number or not

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(isPrime(97))

print(list(filter(isPrime, range(100))))


def isPrime2(n):
    """To tell if a number is prime number or not
    n can be any integer"""
    return n != 0 and n != 1 and all(map(lambda x: n % x != 0, range(2, int(n ** 0.5) + 1)))

print(list(filter(isPrime2, range(100))))
