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


class Solution_A:
    """Basically we need to build the concept of a generator here"""

    def countAndSay(self, n: int) -> str:
        """
        To create the say logic, then loop the say() to get nth number
        """

        def say(num: str) -> int:
            """Helper"""
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

class Solution_B:
    def countAndSay(self, n: int) -> str:
        """
        Combine the say() and loop together
        """
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

class Solution_C:
    def countAndSay(self, n: int) -> str:
        """
        Avoid type convert between int and String
        """

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
    testMethod = Solution_C().countAndSay
    assert testMethod(1) == "1", "first"
    assert testMethod(2) == "11", "second"
    assert testMethod(3) == "21", "third"
    assert testMethod(4) == "1211", "forth"
    assert testMethod(5) == "111221", "fifth"
    assert testMethod(6) == "312211", "sixth"
    assert testMethod(10) == "13211311123113112211", "Very Long"
    print("all passed")
