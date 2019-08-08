# We want to write some simple procedures that work on dictionaries to return information.
# First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.

animals = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati"]}

animals["d"] = ["donkey"]
animals["d"].append("dog")
animals["d"].append("dingo")

def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    """
    animal_number = 0
    for v in aDict.values():
        animal_number += len(v)
    return animal_number

print(how_many(animals))
