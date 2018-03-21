# PE014 Longest Collatz sequence


# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1


# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_chain_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1

    return length


def longest_collatz_chain(limit):
    n, max_so_far = 1, 1
    for num in range(1, limit):
        current = collatz_chain_length(num)
        if current >= max_so_far:
            max_so_far = current
            answer = num

    print(max_so_far, 'is the maximum chain length')
    return answer


if __name__ == '__main__':
    assert collatz_chain_length(13) == 10, 'regular'
    print(longest_collatz_chain(1000000))
    # >>>
    # 525 is the maximum chain length
    # 837799
    # passed
