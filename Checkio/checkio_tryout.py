data = [1, 2, 3, 1, 3, 5]

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

result = []
for i in range(len(data)):
    if i not in single_element_index_list:
        result.append(data[i])
print(result)


