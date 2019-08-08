"""
You are given an expression with numbers, brackets and operators. For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).
Output: A verdict on the correctness of the expression in boolean (True or False).
"""


def checkio(expression):
    OPEN_BRACKETS = ("(", "{", "[", )
    CLOSE_BRACKETS = (")", "}", "]", )

    occurrences = []

    for letter in expression:
        if letter in OPEN_BRACKETS:
            occurrences.append(OPEN_BRACKETS[OPEN_BRACKETS.index(letter)])
        if letter in CLOSE_BRACKETS:
            # If ocurrences of opening brackets is zero
            # it means that we have bad closing brackets.
            # 意思是如果存在close bracket但是没有open与之对应 (close多于open)
            if len(occurrences) == 0:
                return False

            # 这里巧妙运用.pop()来对应其close和open bracket,作为验证方式,来规避结构性错误.
            if occurrences.pop() != OPEN_BRACKETS[CLOSE_BRACKETS.index(letter)]:
                return False

    # 最终如果open和close是一一对应的话,occurences的长度应该归零, 不然就是close少于open
    return len(occurrences) == 0

# 综上: 排除了open和close数量的差别造成错误, 也排除了位置不对应的结构性错误.
# 思路: 创建一个空list,若出现正符号则加入,若出现反符号则抵消对应的正符号,最终list回到empty状态为True, 反之为False

if __name__ == "__main__":
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    print("done")
