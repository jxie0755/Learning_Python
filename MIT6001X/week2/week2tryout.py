def palindrome(raw_text):
    # first to convert raw_text to a string of lower case letters and remove the space
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

raw_text = 'abcdcda'
print(palindrome(raw_text))
