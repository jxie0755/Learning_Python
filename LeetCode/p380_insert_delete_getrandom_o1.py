# P380 Insert Delete GetRandom O(1)
# Medium

# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


from random import randint

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use a list to track sequence and use a hashtable to remember the sequence of the value
        self.set = []
        self.used = {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.used: # check in by hashtable O(1)
            return False

        self.set.append(val)              # add to the end
        self.used[val] = len(self.set)-1  # record the value: last idx, last index by length of array O(1)

        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.used: # check in by hashtable O(1)
            return False

        # switch val and last val in array and hashtable

        self.used[self.set[-1]] = self.used[val]  # hastable中将最后一个值得index改成remove值得idx

        # 把当前index与last交换
        self.set[self.used[val]], self.set[-1] = self.set[-1], self.set[self.used[val]]

        # 把last值弹出, hashtable中remove val
        self.used.pop(val)
        self.set.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.set[randint(0, len(self.set)-1)]



if __name__ == "__main__":
    obj = RandomizedSet()

    assert obj.insert(1)
    print(obj.set)
    print(obj.used)

    assert obj.insert(2)
    print(obj.set)
    print(obj.used)

    assert not obj.insert(1)
    obj.insert(3)
    obj.insert(4)
    obj.insert(5)

    print()
    print(obj.set)
    print(obj.used)

    assert not obj.remove(6)
    assert obj.remove(2)
    print(obj.set)
    print(obj.used)

    print(obj.getRandom())

    print("all passed")
