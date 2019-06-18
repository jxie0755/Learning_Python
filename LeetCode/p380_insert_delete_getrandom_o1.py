# P380 Insert Delete GetRandom O(1)
# Medium

# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """



if not __name__ == '__main__':
    obj = RandomizedSet(1,2,3)
    print(obj)

    assert not obj.insert(1)
    assert obj.insert(4)

    print(obj)

    assert not obj.remove(5)
    assert obj.remove(1)


    print(obj.getRandom())

    print('all passed')
