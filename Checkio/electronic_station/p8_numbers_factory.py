# You are given a two or more digits number N. For this mission, you should find the smallest positive number of X, such that the product of its digits is equal to N. If X does not exist, then return 0.

# Input: A number N as an integer.
# Output: The number X as an integer.

# example:N = 20. We can factorize this number as 2*10, but 10 is not a digit. Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.

# 本质上是求一个数能不能被分解成全是个位数的因数,如果不能就return 0, 如果可以,就return这些因数的组成的最小数字

def checkio(number):
    # Form a list for all the divisor
    z = number
    result = []
    def divx(x):
        for i in range(9, 1, -1):
            if x % i == 0:
                a = i
                b = x // i
                result.append(i)
                return b
        return str(x)
    # cycling to get all divisor's divisor into the list if < 10.
    while True:
        try:
            number = divx(number)
        except TypeError:
            break

    # problem fixing:
    try:
        # if number is > 10 and have no divisor, return 0
        if int(number) !=1 and int(number) not in result:
            return 0
        else:
            return int(''.join([str(i) for i in sorted(result)]))
    # if number is prime number in the first place return 0
    except IndexError:
        return 0

if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    print('done')

# Good Version
# 思路几乎完全相同,但是他写了一个更好的循环
def checkio2(number):
    res = []
    # 将我的divx()和后面的while循环合为一体了.
    while number != 1:
        for i in range(9, 1, -1):
            if number % i == 0:
                res.append(str(i))
                number //= i
                break
        # 精髓就是利用一个else把所有情况都return 0: number只要不能整除9-2之间的数就马上return 0
        else:
            return 0
    return int("".join(sorted(res)))

dd = 20
print(checkio2(dd))
