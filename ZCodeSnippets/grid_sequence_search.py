# From ProjectEuler P001
# https://projecteuler.net/problem=11


def gen_diagonal_search_topleft_bottomright(n, grid):
    """diagonally search consecutive elements from top-left to bottom-right in a grid

    n: numbers of consecutive elements
    grid: a list of sub-lists which all contains same number of elements

    yield: each group of consecutive elements
    """
    width, height = len(grid[0]), len(grid)
    if width < n or height < n:
        yield None

    for y in range(0, height - n + 1):
        for x in range(0, width - n + 1):
            sample = [grid[y + i][x + i] for i in range(n)]
            yield sample


def gen_diagonal_search_bottomleft_topright(n, grid):
    """diagonally search consecutive elements from bottom-left to top-right in a grid

    n: numbers of consecutive elements
    grid: a list of sub-lists which all contains same number of elements

    yield: each group of consecutive elements
    """
    width, height = len(grid[0]), len(grid)
    if width < n or height < n:
        yield None

    for y in range(n-1, height):
        for x in range(0, width - n + 1):
            sample = [grid[y - i][x + i] for i in range(n)]
            yield sample


def gen_horizontal_search(n, grid):
    """horizontally search consecutive elements in a grid

    n: numbers of consecutive elements
    grid: a list of sub-lists which all contains same number of elements

    yield: each group of consecutive elements
    """
    width, height = len(grid[0]), len(grid)
    if width < n:
        yield None

    for y in range(0, height):
        for x in range(0, width - n + 1):
            sample = [grid[y][x + i] for i in range(n)]
            yield sample


def gen_veritical_search(n, grid):
    """vertically search consecutive elements in a grid

    n: numbers of consecutive elements
    grid: a list of sub-lists which all contains same number of elements

    yield: each group of consecutive elements
    """
    width, height = len(grid[0]), len(grid)
    if height < n:
        yield None

    for y in range(0, height - n + 1):
        for x in range(0, width):
            sample = [grid[y + i][x] for i in range(n)]
            yield sample

if __name__ == '__main__':

    grid_test = [
        ['01','02','03','04','05'],
        ['06','07','08','09','10'],
        ['11','12','13','14','15'],
        ['16','17','18','19','20']
    ]

    print('Test function topleft_bottomright:')
    t1 = gen_diagonal_search_topleft_bottomright(3, grid_test)
    for i in t1:
        print(i)
    print()

    print('Test function bottomleft_topright:')
    t2 = gen_diagonal_search_bottomleft_topright(3, grid_test)
    for i in t2:
        print(i)
    print()

    print('Test function horizontal:')
    t3 = gen_horizontal_search(3, grid_test)
    for i in t3:
        print(i)
    print()

    print('Test function vertical:')
    t4 = gen_veritical_search(3, grid_test)
    for i in t4:
        print(i)
    print()
