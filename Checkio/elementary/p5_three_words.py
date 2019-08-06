"""
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.
"""

def checkio(words):
    result = 0
    for i in words.split():
        if i.isalpha():
            result += 1
            if result == 3:
                break
        else:
            result = 0
    return result == 3

if __name__ == "__main__":
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
