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

print(list(itertools.combinations([1,2,3], 2)))





# Combination with replacement
def combinations_with_replacements(candidates: List[int], pick: int) -> List[List[int]]:
    """
    self verison of combination algorithm, with repeating
    almost the same as itertools.combinations_with_replacement
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

    # put proxy answer idx into real elements in candidates
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


