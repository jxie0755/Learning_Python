# You are given a non-empty list of integers (X).
# For this task, you should return a list consisting of only the non-unique elements in this list.
# Input: A list of integers.
# Output: The list of integers.
# To do so you will need to remove all unique elements
# (elements which are contained in a given list only once).
# When solving this task, do not change the order of the list.


def checkio(data):
    # create a list of recording the number of occurrence of element in data
    # this list is the same length as data, but the 1 in there represent the single element
    # the position of the 1 is the same of position of the single elments in data
    data_count = []
    for i in data:
        data_count.append((data.count(i)))

    # isolate the index number of 1, and add it to a new list
    single_element_index_list = []
    for i in range(len(data)):
        if data_count[i] == 1:
            single_element_index_list.append(i)
    print(single_element_index_list)

    # create a result by adding everthing item in data in, except for the specific index
    result = []
    for i in range(len(data)):
        if i not in single_element_index_list:
            result.append(data[i])
    return result

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
