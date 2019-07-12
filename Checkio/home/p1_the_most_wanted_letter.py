# Input: A text for analysis as a string.
# Output: The most frequent letter in lower case as a string.

# def checkio(text):
#     # raw string process, transfer to lower case and remove spaces
#     text = text.lower().replace(" ", "")
#
#     # raw string process 2, create a list, sort and add an empty string at the end.
#     text_list = [i for i in text if ord(i) in range(97, 123)]
#     text_list = sorted(text_list)
#     text_list.append("")
#
#     # create an empty dict and a loop to add data to the dict
#     text_dict = {}
#     index = len(text_list)
#     occurrence = 1
#     for i in range(0, index - 1):
#         if text_list[i] == text_list[i + 1]:
#             occurrence += 1
#         else:
#             text_dict[text_list[i]] = occurrence
#             occurrence = 1
#
#     # generate a list that stores all the values
#     occurrence_max = max(list(text_dict.values()))
#     for keys in text_dict.keys():
#         if text_dict[keys] == occurrence_max:
#             break
#     return keys

# another method
# import string
#
# def checkio(text):
#     """
#     We iterate through latyn alphabet and count each letter in the text.
#     Then "max" selects the most frequent letter.
#     For the case when we have several equal letter,
#     "max" selects the first from them.
#     """
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)

def checkio(text):
    import string
    text = "".join(sorted(list(filter(lambda x: x in string.ascii_lowercase, text.lower()))))
    for i in text:
        if text.count(i) == max(map(text.count, string.ascii_lowercase)):
            return i

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
