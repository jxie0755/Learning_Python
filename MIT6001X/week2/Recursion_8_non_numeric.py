# Recursion on strings
# Challenge: how to tell if a character is palindrome (回词,调转字母顺序,单词相同)

# Non-recursion way
def is_palindrome(text):
    return text == text[::-1]

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
        if text[0] == text[-1]:
            return palindrome(text[1:-1])
        else:
            return False
        # DO NOT FORGET TO RECURSE properly, with a return command here!

raw_text = 'a bca'
print(palindrome(raw_text))

print()
# MIT 另解
def palindrome2(raw_text):
    text = raw_text.lower()
    text = text.replace(' ', '')

    print('text is now', text)
    print('length of text is', len(text))

    if len(text) <= 3:
        return text[0] == text[-1]
    else:
        return text[0] == text[-1] and palindrome2(text[1:-1])

raw_text2 = 'zabcbaz'
print(palindrome2(raw_text2))
