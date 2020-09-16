"""
This is a way to record self constructed Permutaion and Combination

Similar python built-in method can be found in itertools

Permutation

Combiantion:
    itertools.combiantions_with_replacement
    itertools.combinations

"""

from typing import *
import itertools


# Combinations with no replacement
def combinations(candidates: List[int], pick: int) -> List[List[int]]:
    """
    Self verison of combination algorithm, with no repeating
    Use a proxy helper to generate indices of based on length of candidates, then convert to real elments
    """
    # this can individually work as a combination of list of elements
    def combinesSolo(n: int, pick: int) -> List[List[int]]:
        """
        Helper function
        Combination of indices
        """
        if pick == 0:
            return [[]]
        elif pick == n:
            return [list(range(n))]
        elif pick == 1:
            return [[i] for i in range(n)]
        else:
            return [com + [n - 1] for com in combinesSolo(n - 1, pick - 1)] + combinesSolo(n - 1, pick)
                          # n-1 because end index of n length is n-1

    proxy_ans = combinesSolo(len(candidates), pick)

    # convert proxy answer into real elements in candidates
    ans = []
    for proxy_comb in proxy_ans:
        ans_comb = [candidates[i] for i in proxy_comb]
        ans.append(ans_comb)

    return ans


if __name__ == '__main__':
    assert sorted(combinations([1,2,3,4], 2)) == [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4]
    ]



# Combinations with replacement
def combinations_with_replacements(candidates: List[int], pick: int) -> List[List[int]]:
    """
    Self verison of combination algorithm, with repeating
    Almost the same as itertools.combinations_with_replacement
    Also use a proxy to generate indices of based on length of candidates, then convert to real elments
    """
    if pick == 0:
        return []

    # setup a proxy (idx of candidates)
    proxy = [i for i in range(len(candidates))]
    proxy_ans = [[i] for i in proxy]

    p = 1
    while p < pick:
        new_proxy_ans = []
        for comb in proxy_ans:
            for idx in proxy:
                if idx >= max(comb):  # a very critical step to remove repeating
                    new = comb + [idx]
                    new_proxy_ans.append(new)
        proxy_ans = new_proxy_ans
        p += 1

    # convert proxy answer into real elements in candidates
    ans = []
    for proxy_comb in proxy_ans:
        ans_comb = [candidates[i] for i in proxy_comb]
        ans.append(ans_comb)

    return ans


if __name__ == '__main__':
    assert sorted(sorted(i) for i in combinations_with_replacements([1, 2, 3], 3)) == [
        [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3], [1, 3, 3],
        [2, 2, 2], [2, 2, 3], [2, 3, 3],
        [3, 3, 3]
    ]
