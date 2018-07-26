def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.
    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] = table[prev] + [word]
        prev = word
    return table

def build_successors_table2(tokens):
    """Return a dictionary: keys are words; values are lists of successors.
    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    for word in tokens:
        if word not in table:
            "*** YOUR CODE HERE ***"
            table[word] = [tokens[i] for i in range(len(tokens)) if tokens[i-1] == word]
        "*** YOUR CODE HERE ***"
        # no need any codes


    return table

a = ['a', 'b', 'c', 'd', 'a']
print(build_successors_table(a))
print(build_successors_table2(a))