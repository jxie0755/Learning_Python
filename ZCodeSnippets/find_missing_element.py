# Compare two most identical list.
# One of them missed one element
# Use bit ^ calculation to find out the missing element

# Developed from Leetcode P268 Missing numbers

def find_miss(lst1, lst2):
    check = 0
    for i in lst1 + lst2:
        check ^= i

    return check

if __name__ == "__main__":
    a = [2,3,4,1,2]
    b = [4,2,3,8,2,1]

    assert find_miss(a, b) == 8, "Test case"
    print("all passed")
