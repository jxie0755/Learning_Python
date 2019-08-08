"""
A pangram or holoalphabetic sentence for a given alphabet is a sentence using every letter of the alphabet at least once.
Perhaps you are familiar with the well known pangram "The quick brown fox jumps over the lazy dog".
Input: A text as a string.
Output: Whether the sentence is a pangram or not as a boolean.
"""

import string
def check_pangram(text):
    return all(i in text.upper() for i in list(string.ascii_uppercase))

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print("If it is done - it is Done. Go Check is NOW!")
