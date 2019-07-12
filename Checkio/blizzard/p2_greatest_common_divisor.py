# You are given an arbitrary number of positive integers.
# You should find the greatest common divisor for these numbers.
# Input: An arbitrary number of positive integers.
# Output: The greatest common divisor as an integer.


# The iteration algorithm (reverse the check sequence to stop after find the first one)
def greatest_common_divisor(*args):
    for i in range(1, min(args)+1)[::-1]:
        if all(x % i == 0 for x in args):
            return i


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
    print("done")


# 辗转相除法，又称欧几里得算法（英语：Euclidean algorithm)
# for two numbers
def greatest_common_divisorA(x, y):
    if x == y:
        return x
    else:
        if x < y:
            return(greatest_common_divisor(x, y-x))
        if x > y:
            return(greatest_common_divisor(y, x-y))


# for multiple numbers, 还是会最大递归数溢出
def greatest_common_divisorB(*args):
    if len(set(args)) <= 1:
        return args[0]
    else:
        maxv, minv, argvs = max(args), min(args), sorted(args)[:-1]
        argvs.append(maxv - minv)
        return greatest_common_divisorB(*argvs)


# for multiple numbers 两种算法结合
def greatest_common_divisorX(*args):
    if len(set(args)) <= 1:
        return args[0]
    else:
        # For one of the args is lower than 1000, it is better to use the iteration way
        if min(args) <= 1000:
            for i in range(1, min(args) + 1)[::-1]:
                if all(x % i == 0 for x in args):
                    return i
        # If all args are large numbers, it is better to use the Euclidean algorithm in a recursive way
        else:
            maxv, minv, argvs = max(args), min(args), sorted(args)[:-1]
            argvs.append(maxv - minv)
            return greatest_common_divisorX(*argvs)

print(greatest_common_divisorX(4294967296, 2))
print(greatest_common_divisorX(2226172404, 2652430846, 3702223254, 3260139372, 2021191608))
print(greatest_common_divisorX(6, 4))

# module fractions can solve this problem easily with a function called gcd()
