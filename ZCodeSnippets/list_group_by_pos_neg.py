# process a list to group contiguous positive and negative numbers in sums

def group_pos_neg_list(nums):
    """
    nums: list[int]
    return a processed-list that groups in the sum of consecutive positive numbers (and 0) and negative numbers
    example: [1,2,3, -1,-2,-3, 1,2,3, -1,-2,-3] will return [6,-6,6,-6]
    """
    p_nums = []

    # to determine if the first element >=0 or <0
    # create pos_combined and neg_combined as a list to check the length in the future
    if nums[0] >= 0:
        pos_combined, neg_combined = [nums[0]], []
    elif nums[0] < 0:
        pos_combined, neg_combined = [], [nums[0]]

    # loop over each element from position 1 to the end
    # accumulate pos num and neg nums and set back to 0 if next element is different
    index = 1
    while index < len(nums):
        if nums[index] >= 0 and nums[index - 1] >= 0:  # both posivite
            pos_combined.append(nums[index])
            index += 1
        elif nums[index] < 0 and nums[index - 1] < 0:  # both negative
            neg_combined.append(nums[index])
            index += 1
        else:
            if len(pos_combined) > 0:
                p_nums.append(sum(pos_combined))
                pos_combined, neg_combined = [], [nums[index]]
            elif len(neg_combined) > 0:
                p_nums.append(sum(neg_combined))
                pos_combined, neg_combined = [nums[index]], []
            index += 1

    # finish the last combined group
    if len(pos_combined) > 0:
        p_nums.append(sum(pos_combined))
    elif len(neg_combined) > 0:
        p_nums.append(sum(neg_combined))

    return p_nums

# Version 2




if __name__ == '__main__':
    assert group_pos_neg_list([1, 2, 3, -1, -2, -3, 1, 2, 3, -1, -2, -3]) == [6, -6, 6, -6]
    assert group_pos_neg_list([0, 0, -3, 1]) == [0, -3, 1]
    assert group_pos_neg_list([-1, -1, -1]) == [-3]
    assert group_pos_neg_list([0]) == [0]
    assert group_pos_neg_list([1, 2, 3, 4]) == [10]
    assert group_pos_neg_list([-1, 0, -1, 0, -1, 123]) == [-1, 0, -1, 0, -1, 123]
    print('all passed')


# see more at:
# https://stackoverflow.com/questions/48652109/shorten-a-list-of-integers-by-sums-of-contiguous-positive-or-negative-numbers#48652134

