# - "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
# - "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
# - "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x is true then the value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however the operation must return some truth value and there are only two choices, so the return value is the one that entails less, namely true.
# - "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
# - "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.
# Here you can see the truth table for these operations:
#
#  x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
# --------------------------------------
#  0 | 0 |  0  |  0  |  1  |  0  |  1  |
#  1 | 0 |  0  |  1  |  0  |  1  |  0  |
#  0 | 1 |  0  |  1  |  1  |  1  |  0  |
#  1 | 1 |  1  |  1  |  1  |  0  |  1  |
# --------------------------------------

# Input: Three arguments. X and Y as 0 or 1. An operation name as a string.
# Output: The result as 1 or 0.


OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == 'conjunction':
        if x == 1 and y == 1:
            return 1
        else:
            return 0
    elif operation == 'disjunction':
        if x == 0 and y == 0:
            return 0
        else:
            return 1
    elif operation == 'implication':
        if x == 1 and y == 0:
            return 0
        else:
            return 1
    elif operation == 'exclusive':
        if x == y:
            return 0
        else:
            return 1
    elif operation == 'equivalence':
        if x == y:
            return 1
        else:
            return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

# 另解
def boolean(x, y, operation):
    if operation == 'conjunction':
        return int(x and y)
    elif operation == 'disjunction':
        return int(x or y)
    elif operation == 'exclusive':
        return int(x != y )
    elif operation == 'equivalence':
        return int(x == y)
    elif operation == 'implication':
        return int(not(x) or y)
