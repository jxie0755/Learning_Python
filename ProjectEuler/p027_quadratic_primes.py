# P027 Quadratic primes



# Euler discovered the remarkable quadratic formula:
# n^2+n+41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However,
# when n=40, 40^2+40+41 = 40(40+1)+41 is divisible by 41,
# and certainly when n=41,41^2+41+41 is clearly divisible by 41.

# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
# The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:
# n^2+an+b, where |a|<1000 and |b|≤1000

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

def quad_build(a, b):
    def quad(n):
        return n ** 2 + a * n + b
    return quad

def is_prime(n):
    return all([n % div != 0 for div in range(2, int(n ** 0.5) + 1)])

def solution(r1, r2):
    result = {}
    for a in range(-r1+1, r1):
        for b in range(-r2, r2+1):
            Q = quad_build(a, b)
            n = 0
            while Q(n) >= 2 and is_prime(Q(n)):
                n += 1
            result[(a, b)] = n

    answer = max(result, key=result.get)
    print('maximum consecutive prime number:', result[answer[0], answer[1]])
    print('from', answer)
    return answer[0] * answer[1]


if __name__ == '__main__':
    print(solution(1000, 1000))
    # >>>
    # maximum consecutive prime number: 71
    # from (-61, 971)
    # -59231
    # passed
