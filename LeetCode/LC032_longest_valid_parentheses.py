"""
https://leetcode.com/problems/longest-valid-parentheses/
LC020 Longest Valid Parentheses
Hard

Given a string containing just the characters "(" and ")", find the length of the longest valid (well-formed) parentheses substring.
"""


class Solution_A:

    def longestValidParentheses(self, s: str) -> int:
        """
        Iterate all substring from long to short and find the first valid
        This will exceed max time
        """
        for lenth in range(len(s), 0, -1):
            for start_idx in range(len(s) - lenth + 1):
                sample = s[start_idx:start_idx + lenth]
                if self.parenIsValid(sample):
                    return len(sample)
        return 0

    def parenIsValid(self, s: str) -> bool:
        """
        Helper function from LC020
        Modified with just to evaluate curved parentheses
        """
        brackets = 0
        for i in s:
            if i == "(":
                brackets += 1
            if i == ")":
                if brackets == 0:
                    return False
                else:
                    brackets -= 1

        return brackets == 0


class Solution_B:

    def longestValidParentheses(self, s: str) -> int:
        """
        O(log(N)*N) new idea, Divide and Conquer

        )) (  ) ((( ) (( )) ( )) convert to
        -1 1 -1  3 -1 2 -2  1 -2 then merge L positive + R negative
        -1  00   200  0000  00 -1
        -1  00 1 000  0000  00  0

        longest string of 0 is length = 10
        TODO not passing the last testCase
        """
        # first translate sequence to digits
        trans = []
        for i in s:
            if not trans:
                if i == "(":
                    trans.append(1)
                elif i == ")":
                    trans.append(-1)
            else:
                if i == "(":
                    if trans[-1] > 0:
                        trans[-1] += 1
                    else:
                        trans.append(1)
                elif i == ")":
                    if trans[-1] < 0:
                        trans[-1] -= 1
                    else:
                        trans.append(-1)

        trans_data = [[i, abs(i)] for i in trans]

        # keep merging  left pos + right nega
        merged = True
        while merged:
            merged = False
            L, R = -1, -1
            i = 0
            while i < len(trans_data):
                if trans_data[i][0] == 0:  # found a pre-merged 0
                    while i + 1 < len(trans_data) and trans_data[i+1][0] == 0:
                        trans_data[i][1] += trans_data[i+1][1]
                        trans_data.pop(i+1)
                    i += 1
                else:
                    if trans_data[i][0] < 0 and L != -1 and R == -1:  # already found a L before this R
                        R = i
                    elif trans_data[i][0] > 0 and L == -1 and R == -1: # only find the first L
                        L = i
                    i += 1
                if L != -1 and R != -1:  # find a pair, merge L and R
                    merged = True
                    if trans_data[L][1] > trans_data[R][1]:
                        trans_data[L][0] = trans_data[L][0] + trans_data[R][0]
                        trans_data[L][1] = trans_data[L][1] - trans_data[R][1]
                        trans_data[R][0] = 0
                        trans_data[R][1] = trans_data[R][1] * 2
                    elif trans_data[L][1] == trans_data[R][1]:
                        trans_data[L][0] = 0
                        trans_data[R][0] = 0
                    elif trans_data[L][1] < trans_data[R][1]:
                        trans_data[R][0] = trans_data[L][0] + trans_data[R][0]
                        trans_data[L][0] = 0
                        trans_data[R][1] = trans_data[R][1] - trans_data[L][1]
                        trans_data[L][1] = trans_data[L][1] * 2
                    L, R = -1, -1
        print(trans_data)
        # screen out the max_zero to return
        max_zero = 0
        for i in trans_data:
            if i[0] == 0 and i[1] > max_zero:
                max_zero = i[1]
        return max_zero


class Solution_C:

    def longestValidParentheses(self, s: str) -> int:
        """
        O(log(N)*N) new idea, merge using a stack

         )  ) (  ) ( ( (  ) ( (  )  ) (  )  )  ( convert to
        -1 -1 1 -1 1 1 1 -1 1 1 -1 -1 1 -1 -1  ( then merge L positive + R negative
        -1 -1  2   1 1  2   1  2   -1  2   -1  1
        -1 -1  2   1 1  2      4       2   -1  1
        -1 -1  2   1 1         8          -1   1
        -1 -1  2   1           10              1
        longest string of 0 is length = 10
        passed with slow time
        """
        if not s:
            return 0

        # translate the string into a list of intergers represented by 1 and -1
        trans_data = [1 if i == "(" else -1 for i in s]

        merged = True
        while merged:
            merged = False
            stack = []
            new_trans_data = []
            for elem in trans_data:
                if elem == 1: # find L
                    if not stack: # no L found
                        stack.append(elem)
                    else:
                        new_trans_data += stack
                        stack.clear()
                        stack.append(elem)
                elif elem == -1: # find R
                    if stack and stack[0] == 1: # merge the stack
                        stack.append(elem)
                        new_trans_data.append(sum(stack) + 2) # existing pairs + newly formed (-1+1)
                        stack.clear()
                        merged = True
                    else:
                        new_trans_data += stack
                        stack.clear()
                        new_trans_data.append(elem)
                else: # existing pairs
                    if stack and stack[-1] > 1:
                        stack[-1] += elem
                    else:
                        stack.append(elem)

            if stack: # check if there is anything left in the stack with no ending ")"
                new_trans_data += stack
            trans_data = new_trans_data

        ans = max(trans_data)
        if ans >= 2:
            return ans
        else:
            return 0


if __name__ == '__main__':
    testCase = Solution_C()

    assert testCase.longestValidParentheses("(()") == 2, "Example 1, '()'"
    assert testCase.longestValidParentheses(")()())") == 4, "Example 2, '()()'"
    assert testCase.longestValidParentheses("") == 0, "Example 3, Edge 0"
    assert testCase.longestValidParentheses("(") == 0, "Example 4, Edge 1"
    assert testCase.longestValidParentheses(")") == 0, "Example 5, Edge 2"

    assert testCase.longestValidParentheses("()(()") == 2, "Additional 1"
    assert testCase.longestValidParentheses("()(()()") == 4, "Additional 2"
    assert testCase.longestValidParentheses("(()(((()") == 2, "Additional 3"
    assert testCase.longestValidParentheses("(()((()))") == 8, "Additional 4"
    assert testCase.longestValidParentheses("(((()())))") == 10, "Additional 5"
    assert testCase.longestValidParentheses("))()((()(())())(") == 10, "Additional 6"

    long = ")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())"
    assert testCase.longestValidParentheses(long) == 132, "Additional 7, --)(2(2((132((2(36--"

    print("All passed")
