# You are given a two or more digits number N. For this mission, you should find the smallest positive number of X, such that the product of its digits is equal to N. If X does not exist, then return 0.

# Input: A number N as an integer.
# Output: The number X as an integer.

# example:N = 20. We can factorize this number as 2*10, but 10 is not a digit. Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.

# 本质上是求一个数能不能被分解成全是个位数的因数,如果不能就return 0, 如果可以,就return这些因数的组成的最小数字

def checkio(number):
    # Form a list for all the divisor
    result = []
    def divx(x):
        for i in range(2, 10)[::-1]:
            if number % i == 0:
                a = i
                b = number // i
                result.append((a, b))
                if b >= 10:
                    divx(b)
    divx(number)
    print(result)

# if __name__ == '__main__':
#     assert checkio(20) == 45, "1st example"
#     assert checkio(21) == 37, "2nd example"
#     assert checkio(17) == 0, "3rd example"
#     assert checkio(33) == 0, "4th example"
#     assert checkio(3125) == 55555, "5th example"
#     assert checkio(9973) == 0, "6th example"
#     print('done')

print(checkio(3125))
