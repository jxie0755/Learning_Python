# P022 Names Scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 Ã— 53 = 49714.

# What is the total of all the name scores in the file?


def name_scores(txt_file):
    # Process the data
    with open(txt_file) as f_obj:
        content = sorted([i[1:-1] for i in f_obj.readline().split(',')])
    
    # Calculate the value
    result, index = 0, 1
    while index <= len(content):
        name_score = 0
        for ltr in content[index-1]:
            name_score += ord(ltr) - 64
        result += name_score * index
        index += 1
    return result

if __name__ == '__main__':
    print(name_scores('p022_data.txt'))
    # >>> 871198282
    # passed
