def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    answer = 0
    count = 0
    for i in s:
        try:
            answer += int(i)
            count += 1
        except:
            pass
    if count != 0:
        return answer
    else:
        raise ValueError


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    # Process the two lists
    L1_int, L1_str = [], []
    for i in L1:
        if type(i) == int:
            L1_int.append(i)
        elif type(i) == str:
            L1_str.append(i)

    L2_int, L2_str = [], []
    for i in L2:
        if type(i) == int:
            L2_int.append(i)
        elif type(i) == str:
            L2_str.append(i)

    # Compare if they are the same permutations
    if sorted(L1_int) != sorted(L2_int) or sorted(L1_str) != sorted(L2_str):
        return False
    else:
        result = None
        count = 0
        for i in set(L1):
            new_count = L1.count(i)
            if new_count > count:
                count = new_count
                result = i
        return (result, count, type(result)) if result else (None, None, None)

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).

        key_code is a dictionary with N keys mapping str to str where each key is a letter in map_from at index i and the corresponding value is the letter in map_to at index i.

        decoded is a string that contains the decoded version of code using the key_code mapping. """
    dict_result = dict(zip(map_from, map_to))

    decode = ''
    for i in code:
        decode += dict_result[i]
    return (dict_result, decode)


class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


# Write a class that implements the specifications below. Do not override any methods of Container.
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        try:
            del self.vals[e]
        except:
            pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        return e in self.vals
