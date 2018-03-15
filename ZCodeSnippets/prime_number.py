# Different way to get prime numbers

# Version 1
def prime_list_original(n1, n2):
    pnumber_list = []
    for x in range(n1, n2+1):
        for i in range(2, x):
            if x % i == 0:
                break
                # 这是两重迭代,第一重:历遍每一个x去除以i. 第二重:x要除以历遍的每一个i.
                # 这个break是针对第二重迭代,使得只要有一个i能满足余数=0,那么这个x就不符合质数条件
                # 然后回到第一重迭代,试下一个x,如此往复.
        else:
            pnumber_list.append(x)
    return pnumber_list

if __name__ == '__main__':
    print(prime_list_original(2,20))
    # >>> [2, 3, 5, 7, 11, 13, 17]

# generator version
def genPrimes(max=None):  # set a max limit
    p = 2
    while max == None or p <= max:
        if all(p % x != 0 for x in range(2, p)):
            yield p
        p += 1

if __name__ == '__main__':
    P = genPrimes(17)
    print(list(P))
    # >>> [2, 3, 5, 7, 11, 13, 17]

# 最简练

# To tell if a number is prime number or not
def isPrime(n):
    """To tell if a number is prime number or not
    n can be any integer"""
    return n != 0 and n != 1 and all(map(lambda x: n % x != 0, range(2, int(n ** 0.5) + 1)))

if __name__ == '__main__':
    print(list(filter(isPrime2, range(100))))

def show_prime_list(n1, n2):
    pnumber = [x for x in range(n1, n2+1) if all(x % i for i in range(2, int(x**0.5)+1))]
    return pnumber

if __name__ == '__main__':
    print(show_prime(10,30))
    # >>> [11, 13, 17, 19, 23, 29]
