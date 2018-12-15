# There is a staircase with N steps and two platforms; one at the beginning, the other at the end of the stairs.
# On each step a number is written (ranging from -100 to 100 with the exception of 0.) Zeros are written on both platforms.
# You start going up the stairs from the first platform, to reach the top on the second one.
# You can move either to the next step or to the next step plus one.
# You must find the best path to maximize the sum of numbers on the stairs on your way up and return the final sum.

# https://py.checkio.org/mission/stair-steps/
# Input: Numbers on each stair as a list of integers.
# Output: The final sum for the best way as an integer.

def checkio(numbers):
    # get sub groups of consecutive neg nums (1 to 3), into a matrix
    # maximum lenth of consecutive neg nums is 3, if more than 3, start a new group
    temp, neglst = [], []
    for i in range(len(numbers)):
        if numbers[i] < 0:
            temp.append(numbers[i])
        elif numbers[i] > 0:
            neglst.append(temp)
            temp = []
    if numbers[-1] < 0:
        neglst.append(temp)

    # 写一个函数处理算法,当连续两个负数取其小,当连续三个负数,去中间数,除非头尾加起来更小.
    negstep = []

    def negprocess(x):
        if len(x) == 2:
            negstep.append(max(x))
        elif len(x) >= 3:
            if x[0] + x[2] >= x[1]:
                negstep.append(x[0] + x[2])
                return negprocess(x[3:])
            else:
                negstep.append(x[1])
                return negprocess(x[2:])

    for i in neglst:
        negprocess(i)

    return sum(negstep) + sum(filter(lambda x: x > 0, numbers))
    # TODO 算法不正确

# 其他算法不理解
def checkio2(numbers):
    c = [0] * (len(numbers) + 1)
    c[1] = numbers[0]
    for i in range(2, len(numbers) + 1):
        print((c[i - 1], c[i - 2]), numbers[i - 1])
        c[i] = max(c[i - 1], c[i - 2]) + numbers[i - 1]

    return max(c[-1], c[-2])

# 其他算法,不理解
def checkio3(numbers):
    prevmax = curmax = 0
    for n in numbers + [0]:
        nextmax = max(curmax + n, prevmax + n)
        prevmax = curmax
        curmax = nextmax
    return curmax

if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, '1st test, (5-1+2=6)'
    assert checkio([5, 6, -10, -7, 4]) == 8, '2nd test, (5+6-7+4=8)'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, '3rd test, (69+77+23+67+35+27+95=393)'
    assert checkio([1,-1,-10,-100,-50,-5000,-100,9999]) == 9840, '4th test, (1-10-50-100+9999=9840)'

    print(checkio([1, -1, -10, -100, -5000, -5, -100, 9999])) # 9885
    print(1-1-100-5+9999) # 9894
    print(1-10-100-5+9999) # 9885
    assert checkio([1, -1, -10, -100, -5000, -5, -100, 9999]) == 9894, '5th test, (1-1-100-5+9999=9894)'

    assert checkio([1, -1, -10, -100, -101, -101, -10, 9999]) == 9879, '6th test, (1-10-101-10+9999)'
    assert checkio([1, -1, -10, -500, -500, -500, -10, 9999]) == 9480, '7th test, (1-10-500-10+9999)'
    print('All ok')

