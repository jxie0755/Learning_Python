# A sequence of n numbers is consdiered valid if the sequence begins with 1 and ends with a given number j
# No two adjeacent numbers are the same
# Sequences may use any intergers between 1 and a given number k where 1 <= j <= k
# Count the number of valid sequences.
# Return the answer of remainder of 10^10 + 7



def foo(n, k, j):
    R = pow(10, 10) + 7
    base = k-1
    expo = n-2-2

    # 直接算,导致数字太大溢出
    # A = pow(base, expo) * (base - 1) * (base - 1)
    # B = pow(base, expo) * 1 * (base)
    # print((A + B) % R)

    # 迭代计算余数
    ans = 1
    for i in range(expo):
        ans *= base
        if ans >= R:
            ans = ans % R
    ans_A = ans * (base-1) * (base-1) % R
    ans_B = ans * 1 * base % R

    return (ans_A + ans_B) % R

# Q1:
# n = 100, k = 100, j = 1
print(foo(100, 100, 1)) # >>> 8691140351

# Q2:
# n = 347, k = 2281, j = 829
print(foo(347, 2281, 829)) # >>>  9256858202



