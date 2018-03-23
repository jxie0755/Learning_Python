# From ProjectEuler P001
# https://projecteuler.net/problem=11

# diagonal from top left to down bottom
    for y in range(0, length - n):
        for x in range(0, length - n):
            sample = [int(grid[y + i][x + i]) for i in range(n)]
            product = reduce(lambda x, y: x * y, sample)
            if product > max_so_far:
                max_so_far = product

    # diagonal top right to down left
    for y in range(n-1, length):
        for x in range(0, length - n):
            sample = [int(grid[y - i][x + i]) for i in range(n)]
            product = reduce(lambda x, y: x * y, sample)
            if product > max_so_far:
                max_so_far = product

    # horizontally
    for y in range(0, n):
        for x in range(0, length - n):
            sample = [int(grid[y][x + i]) for i in range(n)]
            product = reduce(lambda x, y: x * y, sample)
            if product > max_so_far:
                max_so_far = product

    # vertically
    for y in range(0, length - n):
        for x in range(0, n):
            sample = [int(grid[y + i][x]) for i in range(n)]
            product = reduce(lambda x, y: x * y, sample)
            if product > max_so_far:
                max_so_far = product
