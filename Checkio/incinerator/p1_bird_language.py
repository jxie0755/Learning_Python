# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);

# Input: A bird phrase as a string.
# Output: The translation as a string.

VOWELS = "aeiouy"
CONSONANTS = "bcdfghjklmnpqrstvwxz"

def translate(phrase):
    result = list(phrase)
    # filter out the vowels after the cononants
    for i in range((len(phrase) - 1)):
        if phrase[i] in CONSONANTS:
            result[i + 1] = ""
    result = "".join([x for x in result if x])

    # translate the triple vowel to single vowel
    trans = dict(zip([i * 3 for i in VOWELS], VOWELS))
    for k, v in trans.items():
        result = result.replace(k, v)
    return result

# It would be much easier to solve the problem with while loop
def translate(phrase):
    result = ""
    i = 0
    while i < len(phrase):
        if phrase[i] in CONSONANTS:
            result += phrase[i]
            i += 2
        elif phrase[i] in VOWELS:
            result += phrase[i]
            i += 3
        else:
            result += phrase[i]
            i += 1
    return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

print(translate("hieeelalaooo"))
