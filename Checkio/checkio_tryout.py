data = [1, 2, 3, 4, 5, 1, 2, 3]
index = (len(data))
print('index is', index)

# create a list of recording the number of occurrence of element in data
# this list is the same length as data, but the 1 in there represent the single element
# the position of the 1 is the same of position of the single elments in data
data_count = []
for i in data:
    data_count.append((data.count(i)))
print(data_count)

# isolate the index number of 1, and add it to a new list
single_element_index_list = []
for i in range(index):
    if data_count[i] == 1:
        single_element_index_list.append(i)
print('index of single elements are', single_element_index_list)

# iterate the single_elemetn_index_list to remove the same index items in data
for i in single_element_index_list:
    del data[i]
print(data)
