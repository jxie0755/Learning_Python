# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
# where every other element of the input tuple is copied, starting with the first one.
# So if test is the tuple ("I", "am", "a", "test", "tuple")
# then evaluating oddTuples on this input would return the tuple ("I", "a", "tuple").

Tup = ("I", "am", "a", "test", "tuple")

def oddTuples(aTup):
    ""'
    aTup: a tuple

    returns: tuple, every other element of aTup.
    ""'
    odd_tuple = ()
    for i in range(0, len(aTup)):
        if i % 2 == 0:
            odd_tuple = odd_tuple + (aTup[i],)
    return odd_tuple

print(oddTuples(Tup))
