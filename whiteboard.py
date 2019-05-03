# A sequence of n numbers is consdiered valid if the sequence begins with 1 and ends with a given number j
# No two adjeacent numbers are the same
# Sequences may use any intergers between 1 and a given number k where 1 <= j <= k
# Count the number of valid sequences.



def foo(n, k, j):
    base = k-1
    expo = n-2-2

    # 直接算,导致数字太大溢出
    # A = pow(base, expo) * (base - 1) * (base - 1)
    # B = pow(base, expo) * 1 * (base)
    # print((A + B) % 10)

    # 迭代计算余数
    ans = 1
    for i in range(expo):
        ans *= base
        if ans >= 10:
            ans = ans % 10
    ans_A = ans * (base-1) * (base-1) % 10
    ans_B = ans * base % 10

    return (ans_A + ans_B) % 10

# Q1:
# n = 100, k = 100, j = 1
print(foo(100, 100, 1)) # >>> 3

# Q2:
# n = 347, k = 2281, j = 829
print(foo(347, 2281, 829)) # >>>  0



