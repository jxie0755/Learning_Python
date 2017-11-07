# You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.
# Input: A text as a string (unicode).
# Output: The secret message as a string or an empty string.

def find_message(text):
    return ''.join(filter(lambda x: x.isupper(), text))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# other solutions:
def find_message(text):
    return "".join([char for char in text if char.isupper()])
