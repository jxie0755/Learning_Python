# P009 Special Pythagorean triplet


# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagorean_triplet(n):
    """return the pythagorean set when sum == n"""

    max_value = n // 3 + 1  # set maximum for a, not exceed 1/3 of n, to prevent b < a  or c < a
    for a in range(1, max_value):
        rest = n - a
        for b in range((rest-a)//2 + 1, rest//2 + 1):  # set the condition tighter to improve algorithm
            c = n - a - b
            if a < b and a + b > c and a**2 + b**2 == c**2:
                    print(a, "*", b, "*", c)
                    return a * b * c
    else:
        return None  # In case can't find any.

if __name__ == "__main__":
    assert pythagorean_triplet(12) == 60, "regular"
    assert pythagorean_triplet(14) == None, "check None"
    print(pythagorean_triplet(1000))
    # >>>
    # 200 * 375 * 425
    # 31875000
