def checkio(text):
    # raw string process, transfer to lower case and remove spaces
    text = text.lower().replace(' ', '')

    # raw string process 2, create a list, sort and add an empty string at the end.
    text_list = [i for i in text if ord(i) in range(97, 123)]
    text_list = sorted(text_list)
    text_list.append('')

    # create an empty dict and a loop to add data to the dict
    text_dict = {}
    index = len(text_list)
    occurrence = 1
    for i in range(0, index - 1):
        if text_list[i] == text_list[i + 1]:
            occurrence += 1
        else:
            text_dict[text_list[i]] = occurrence
            occurrence = 1

    # generate a list that stores all the values
    occurrence_max = max(list(text_dict.values()))
    for keys in text_dict.keys():
        if text_dict[keys] == occurrence_max:
            break
    return keys

print(checkio("Hello World!"))  # == "l", "Hello test"
print(checkio("How do you do?"))  # == "o", "O is most wanted"
print(checkio("One"))  # == "e", "All letter only once."
print(checkio("Oops!"))  # == "o", "Don't forget about lower case."
print(checkio("AAaooo!!!!"))  # == "a", "Only letters."
print(checkio("abe"))  # == "a", "The First."
print(checkio("a" * 9000 + "b" * 1000))  # == "a", "Long."
print(checkio('Lorem ipsum dolor sit amet 0000000000000000000!!!'))  # == 'm'


# Passed
