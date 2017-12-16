# https://py.checkio.org/mission/box-probability/
# You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the number of the step (N).
# The order of the pearls does not matter.

# Input: The start sequence of the pearls as a string and the step number as an integer.
# Output: The probability for a white pearl as a float.

import itertools


def checkio(marbles, step):
    marbles = [list(marbles)]
    totalp = []
    wchance = []

    def pull(x):
        """ return the toptalp with a list array of all possible pull result, then convert to chance of white ball"""

        # gnerate the pull result list and chance for each pull result
        result = []
        chance = []
        for i in x:
            if 'w' in i:
                a = i[:]
                a.remove('w')
                a.append('b')
                result.append(a)
                chance.append(i.count('w') / len(i))
            if 'b' in i:
                b = i[:]
                b.remove('b')
                b.append('w')
                result.append(b)
                chance.append(i.count('b') / len(i))
            if 'w' not in i:
                a = []
                result.append(a)
                chance.append(0)
            if 'b' not in i:
                b = []
                result.append(b)
                chance.append(0)

        totalp.append(result)
        wchance.append(chance)
        return result

    for i in range(1, step):
        marbles = pull(marbles)

    for i in totalp:
        print(i)
    for i in wchance:
        print(i)

    # 未完成
    return 0.50

    # if __name__ == '__main__':
    #     assert checkio('bbw', 3) == 0.48, "1st example"
    #     assert checkio('wwb', 3) == 0.52, "2nd example"
    #     assert checkio('www', 3) == 0.56, "3rd example"
    #     assert checkio('bbbb', 1) == 0, "4th example"
    #     assert checkio('wwbb', 4) == 0.5, "5th example"
    #     assert checkio('bwbwbwb', 5) == 0.48, "6th example"
