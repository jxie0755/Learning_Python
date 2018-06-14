# http://composingprograms.com/pages/17-recursive-functions.html#example-partitions

# 递归法
def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

if __name__ == '__main__':
    assert count_partitions(6, 4) == 9
    assert count_partitions(5, 5) == 7
    assert count_partitions(10, 10) == 42
    assert count_partitions(15, 15) == 176
    assert count_partitions(20, 20) == 627
    print('all passed')
