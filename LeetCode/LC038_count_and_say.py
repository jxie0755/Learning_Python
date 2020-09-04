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

        ans = "1"
        if n == 1:
            return ans
        else:
            for i in range(n - 1):
                ans = self.say(ans)
        return ans

    def say(self, word: str) -> str:
        """Helper function to say next number based on current number"""
        ans = ""
        cur = ""
        count = 0
        for letter in word:
            if cur == "":
                cur = letter
                count += 1
            else:
                if letter == cur:
                    count += 1
                else:
                    ans += str(count) + cur
                    cur = letter
                    count = 1

        ans += str(count) + cur  # finish last set
        return ans

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
    testCase = Solution_A()
    assert testCase.countAndSay(1) == "1", "first"
    assert testCase.countAndSay(2) == "11", "second"
    assert testCase.countAndSay(3) == "21", "third"
    assert testCase.countAndSay(4) == "1211", "forth"
    assert testCase.countAndSay(5) == "111221", "fifth"
    assert testCase.countAndSay(6) == "312211", "sixth"
    assert testCase.countAndSay(10) == "13211311123113112211", "Very Long"
    print("all passed")
