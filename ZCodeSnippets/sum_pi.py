"""
Calculation of pi
http://composingprograms.com/pages/16-higher-order-functions.html
"""

# accumulating 8/(1*3) + 8/(5*7) + 8/(9*11).......
# which converges to pi very slowly.


def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total

print(pi_sum(1000000))
# >>> 3.141592153589902
