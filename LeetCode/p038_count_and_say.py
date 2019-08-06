"""
https://leetcode.com/problems/count-and-say/
p038 Count and Say
Easy

The count-and-say sequence is the sequence of integers with the first five terms as following:
1. 1
2. 11
3. 21
4. 1211
   1 is 11
     2 is 12
      11 is 21, so next number is: 11 - 12 - 21
5. 111221

each number is a read of previous number
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.
"""


# Basically we need a generator here
class Solution:

    # Version A
    # To create the say logic, then loop the say() to get nth number
    def countAndSay(self, n: int) -> str:

        # Helper
        def say(num):
            num = str(num) + " "
            lenth = 1
            result = ""
            for i in range(len(num) - 1):
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

    # Version B
    # Combine the say() and loop together
    def countAndSay(self, n: int) -> str:

        number = 1
        for i in range(1, n):
            number = str(number) + " "  # 占一个末尾符
            lenth = 1
            result = ""
            for i in range(len(number) - 1):
                if number[i] == number[i + 1]:
                    lenth += 1
                else:
                    result += str(lenth) + number[i]
                    lenth = 1
            number = int(result)
        return str(number)

    # Version C
    # Avoid type convert between int and String
    def countAndSay(self, n: int) -> str:

        number = "1"
        for i in range(1, n):
            number += " "
            lenth = 1
            result = ""
            for i in range(len(number) - 1):
                if number[i] == number[i + 1]:
                    lenth += 1
                else:
                    result += str(lenth) + number[i]
                    lenth = 1
            number = result
        return number


if __name__ == "__main__":
    assert Solution().countAndSay(1) == "1", "first"
    assert Solution().countAndSay(2) == "11", "second"
    assert Solution().countAndSay(3) == "21", "third"
    assert Solution().countAndSay(4) == "1211", "forth"
    assert Solution().countAndSay(5) == "111221", "fifth"
    assert Solution().countAndSay(6) == "312211", "sixth"
    assert Solution().countAndSay(10) == "13211311123113112211", "Very Long"
    print("all passed")
