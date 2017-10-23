# Implement a function that meets the specifications below.

def max_val(t):
    """ t, tuple
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    result = 0
    for i in t:
        try:
            if i > result:
                result = i
                print(result)
        except:
            if max_val(i) > result:
                result = max_val(i)
    return result


t1 = (3, 4, (1,2), 5, [[1],[2]])
t2 = (5, 6, 7, (1,2), [[1],[9]])
print(max_val(t1))
# print(max_val(t2))

