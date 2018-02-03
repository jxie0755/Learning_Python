# p038 Count and Say
# Easy

# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1. 1
# 2. 11
# 3. 21
# 4. 1211
# 5. 111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.

# """
# :type n: int
# :rtype: str
# """

# Basically we need a generator here
class Solution:
    def countAndSay(self, n):  # a version to create the say logic, then loop the say() to get nth number
        def say(num):
            num = str(num) + ' '
            lenth = 1
            result = ''
            for i in range(len(num)-1):
                if num[i] == num[i + 1]:
                    lenth += 1
                elif num[i] != num[i + 1]:
                    result += str(lenth) + num[i]
                    lenth = 1
            return int(result)

        number = 1
        for i in range(1, n):
            number = say(str(number))
        return str(number)

    def countAndSay(self, n):  # combine the say() and loop together
        number = 1
        for i in range(1, n):
            number = str(number) + ' '
            lenth = 1
            result = ''
            for i in range(len(number) - 1):
                if number[i] == number[i + 1]:
                    lenth += 1
                elif number[i] != number[i + 1]:
                    result += str(lenth) + number[i]
                    lenth = 1
            number = int(result)
        return str(number)

if __name__ == '__main__':
    assert Solution().countAndSay(1) == '1', 'first'
    assert Solution().countAndSay(2) == '11', 'second'
    assert Solution().countAndSay(3) == '21', 'third'
    assert Solution().countAndSay(4) == '1211', 'forth'
    assert Solution().countAndSay(5) == '111221', 'fifth'
    assert Solution().countAndSay(6) == '312211', 'sixth'
    print('all passed')
