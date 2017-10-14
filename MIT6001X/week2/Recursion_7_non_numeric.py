# Recursion on strings
# Challenge: how to tell if a character is palindrome (回词,调转字母顺序,单词相同)

# Non-recursion way
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome('exe'))

# Recursion method

# Convert a string to just characters
def palindrome(raw_text):
    """
    To tell if a string is palindrome

    :param text: any string
    :return: True if it is palindrome, else False.
    """
    text = raw_text.lower()
    text = text.replace(' ', '')
    if text[0] == text[-1]:
        return True
    else:
        palindrome(text[1:-1])

s = 'abcedfg'
print(s[-1])
l = ['1', '2', '3', '4']
print(l[-1])
