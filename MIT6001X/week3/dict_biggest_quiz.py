# We want to write some simple procedures that work on dictionaries to return information.
# Write a procedure, called biggest,
# which returns the key corresponding to the entry with the largest number of values associated with it.
# If there is more than one such entry, return any one of the matching keys.

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    v_number = []
    for v in aDict.values():
        v_number.append(len(v))
    high = max(v_number)

    for k, v in aDict.items():
        if len(v) == high:
            return k

print(biggest(animals))
