# You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.

# Input: List of all rectangles heights in histogram
# Output: Area of the biggest rectangle


def largest_histogram(histogram):
    # 仍然是利用substring这个方式得到所有数字碎片
    temp, result = [], []
    n, m = 0, 0
    index = len(histogram)
    while n < index:
        for m in range(0, n + 1):
            temp.append(histogram[m:index - n + m])
        else:
            n += 1
    for i in temp:
        result.append(min(i) * len(i))
    return max(result)



if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")

