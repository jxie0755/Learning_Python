# rotate the data array
data = [0,1,2,3]
for i in range(len(data)):
    data.insert(0, data.pop())
    print(data) # if check data after pop(), it will start with one move, end at original
print('at the end')
print(data)

# >>>
# [3, 0, 1, 2]
# [2, 3, 0, 1]
# [1, 2, 3, 0]
# [0, 1, 2, 3]
# at the end
# [0, 1, 2, 3]

print()

data = [0,1,2,3]
for i in range(len(data)):
    print(data) # if check data before pop(), it will start with orginal, end at last move.
    data.insert(0, data.pop())

print('at the end')
print(data)  # but at the end the data still roll back to original, which is good!
# >>>
# [0, 1, 2, 3]
# [3, 0, 1, 2]
# [2, 3, 0, 1]
# [1, 2, 3, 0]
# at the end
# [0, 1, 2, 3]

# >>>
# [3, 0, 1, 2]
# [2, 3, 0, 1]
# [1, 2, 3, 0]
# [0, 1, 2, 3]

print()

# The best method that gives flexibility
data = [0,1,2,3]
for i in range(len(data)):
    print(data)
    data = data[-1:] + data[0:-1]
    # the good thing is that it is not limited to rotating one element at a time
print('at the end')
print(data)
# >>>
# [0, 1, 2, 3]
# [3, 0, 1, 2]
# [2, 3, 0, 1]
# [1, 2, 3, 0]
# at the end
# [0, 1, 2, 3]



# rotate more than once
data = [0,1,2,3]
for i in range(3): # number of rotation
    for i in range(len(data)):
        print(data) # if check data before pop(), it will start with orginal, end at last move.
        data = data[-1:] + data[0:-1]
    print()
print('at the end')
print(data)
# >>>
# [0, 1, 2, 3]
# [3, 0, 1, 2]
# [2, 3, 0, 1]
# [1, 2, 3, 0]

# [0, 1, 2, 3]
# [3, 0, 1, 2]
# [2, 3, 0, 1]
# [1, 2, 3, 0]
f
# [0, 1, 2, 3]
# [3, 0, 1, 2]
# [2, 3, 0, 1]
# [1, 2, 3, 0]

# at the end
# [0, 1, 2, 3]

# another way without using pop(), create a repeat data array and iterate the same length over
print()

data = [0,1,2,3]
datarotate = data * 3  # '3' gives 2 rotates
for i in range(len(datarotate)-len(data)):
    print(datarotate[i:i+len(data)])
# >>>
# [0, 1, 2, 3]
# [1, 2, 3, 0]
# [2, 3, 0, 1]
# [3, 0, 1, 2]
# [0, 1, 2, 3]
# [1, 2, 3, 0]
# [2, 3, 0, 1]
# [3, 0, 1, 2]