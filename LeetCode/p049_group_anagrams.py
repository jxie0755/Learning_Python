# P049 Group Anagrams
# Medium


# Given an array of strings, group anagrams together.

# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.


class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return [[]]
        hmp = {}
        for word in strs:
            k = tuple(sorted(list(word)))
            if k not in hmp:
                hmp[k] = [word]
            else:
                hmp[k].append(word)
        return list(hmp.values())


if __name__ == "__main__":
    edge_1 = []
    assert Solution().groupAnagrams(edge_1) == [
        []
    ], "edge 1"

    edge_2 = ["a"]
    assert Solution().groupAnagrams(edge_2) == [
        ["a"]
    ], "edge 2"

    sample_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert Solution().groupAnagrams(sample_1) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"]
    ], "Example 1"

    print("all passed")
