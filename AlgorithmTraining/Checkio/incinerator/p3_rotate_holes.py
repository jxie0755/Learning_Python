"""
https://py.checkio.org/mission/rotate-hole/solve/

Input: Two arguments.
A initial state as a list with 1 and/or 0
Pipe numbers for cannonballs as a list of integers
Output: The rotating variants as a list of integers or an empty list.
"""

def rotate(state, pipe_numbers):
    result = []
    for i in range(len(state)):
        if all(state[x] == 1 for x in pipe_numbers):
            result.append(i)
        state.insert(0, state.pop())
    return result

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
