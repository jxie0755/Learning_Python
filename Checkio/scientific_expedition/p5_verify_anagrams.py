# You are given two words or phrase. Try to verify are they anagrams or not.
# Input: Two arguments as strings.
# Output: Are they anagrams or not as boolean (True or False)

def verify_anagrams(first_word, second_word):
    def word_breakdown(word):
        return sorted(word.lower().replace(' ', ''))
    return word_breakdown(first_word) == word_breakdown(second_word)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

# use re
import re
def verify_anagrams(first_word, second_word):
    def word_breakdown(word):
        return sorted(''.join(re.findall("[a-z]+", word.lower())))
    return word_breakdown(first_word) == word_breakdown(second_word)
