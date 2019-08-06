def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if len(line) == 0:
        return 0
    else:
        line = line + " "
        result= []
        count = 1
        for i in range(1, len(line)):
            if line[i] == line[i-1]:
                count += 1
            else:
                result.append(count)
                count = 1
        return max(result)

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat("sdsffffse") == 4, "First"
    assert long_repeat("ddvvrwwwrggg") == 3, "Second"
    print(""Run" is good. How is 'Check'?")
