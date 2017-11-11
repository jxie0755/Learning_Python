# Help Nicola write a function which will determine the age of a ghost based on its opacity. You are given opacity measurements as a number ranging from 0 to 10000 inclusively. The ghosts cannot be older than 5000 years as they simply disappear after such a long time (really!).

# On every birthday, a ghost's opacity is reduced by a number of units equal to its age when its age is a Fibonacci number (Read about this here) or increased by 1 if it is not.

# For example:
# A newborn ghost -- 10000 units of opacity.
# 1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
# 2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
# 3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
# 4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
# 5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).

# Input: An opacity measurement as an integer.
# Output: The age of the ghost as an integer.

def checkio(opacity):
    # create a list of fibonaci number
    f_list = [1, 2]
    while len(f_list) <= 100:
        new = f_list[-1] + f_list[-2]
        f_list.append(new)

    # create age calculation
    if opacity == 10000:
        return 0
    else:
        target = 10000
        for i in range(1, 5000):
            if i in f_list:
                target -= i
            if i not in f_list:
                target += 1
            if target == opacity:
                return i

if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
    print('done')

