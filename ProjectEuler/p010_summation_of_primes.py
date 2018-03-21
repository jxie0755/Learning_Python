142913828922# PE010 Summation of primes


# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def prime_summation(prime_under):
    """return the summation of all prime numbers under the limit"""

    def isPrime(n):
        return all(n % divisor != 0 for divisor in range(2, int(n**0.5)+1))
    result, sample = 0, 2
    while sample < prime_under:
        if isPrime(sample):
            result += sample
        sample += 1

    return result

if __name__ == '__main__':
    assert prime_summation(10) == 17, 'regular'
    print(prime_summation(2000000))
    # >>> 142913828922
    # passed