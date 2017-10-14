# Recursion on strings
# Challenge: how to tell if a character is palindrome (回词,调转字母顺序,单词相同)

# Non-recursion way
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome('exe'))

# Recursion method

# Convert a string to just characters
# CAUTION: be careful with return when it involves boolean
def palindrome(raw_text):
    """
    To tell if a string is palindrome

    :param text: any string
    :return: True if it is palindrome, else False.
    """
    text = raw_text.lower()
    text = text.replace(' ', '')
    print('text is now', text)
    print('length of text is', len(text))
    if len(text) <= 3:
        return text[0] == text[-1]
    else:
        return palindrome(text[1:-1])  # DO NOT FORGET TO RECURSE properly, with a return command here!

raw_text = 'a bca'
print(palindrome(raw_text))

print()
# MIT 另解
def palindrome2(raw_text):
    text = raw_text.lower()
    text = text.replace(' ', '')
    if len(text) <= 3:
        return text[0] == text[-1]
    else:
        return text[0] == text[-1] and palindrome(text[1:-1])

raw_text = 'a bcbaa'
print(palindrome2(raw_text))
