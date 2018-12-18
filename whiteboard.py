def pour(status, first, second):
    """
    return the level of water in first and second
    after pour from first to second
    """
    available = second - status[1]
    if available <= 0:
        return status
    elif available > status[0]:
        return [0, status[0] + status[1]]
    else:
        return [status[0] - available, second]


first = 5
second = 2
status = [5,1]

print(pour(status, first, second))
print(pour([1, 5][::-1], 5, 2)[::-1])