"""
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z
You are given a block of text with different words.
You should count the number of words (striped words) where the vowels with consonants are alternating
that is; words that you count cannot have two consecutive vowels or consonants.
Input: A text as a string (unicode)
Output: A quantity of striped words as an integer.
"""

import string

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    # process the text into a striped text in a list
    punc = string.punctuation
    space = " " * len(punc)
    trantab = str.maketrans(punc, space)
    text_list = text.translate(trantab).upper().split()

    # verify each word if the vowels with consonants are alternating
    def verify(x):
        if x.isalpha() and len(x) >1:
            for i in range(len(x) - 1):
                if x[i] in VOWELS and x[i+1] in VOWELS:
                    return False
                if x[i] in CONSONANTS and x[i+1] in CONSONANTS:
                    return False
            return True

    # apply the verification function to each element in the text_list
    return len(list(filter(verify, text_list)))

if __name__ == "__main__":
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
