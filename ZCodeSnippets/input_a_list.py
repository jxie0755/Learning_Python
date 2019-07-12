# Input a list

# MAP creates iterator that will be consumed by a list() command.
# Without the list() to save it, the iterator can only be used once.
def input_list_numbers():
    return list(map(int, input("input and output numbers:").split()))

def input_list_strings():
    return list(input("input and output strings:").split())

# Input should use " "space to separate, not ","comma
if __name__ == "__main__":
    numArray = input_list_numbers()
    print("numArray is", numArray)
    stringArray = input_list_strings()
    print("StringArray is", stringArray)

# STOF answer

# An iterator is like a generator, it is not necessarily a space in memory.
# Therefore if you convert the iterator to a list, by list(iterator)
# you modify the pointer to the original so that it cannot be used later.
# iterator can only be called once!
