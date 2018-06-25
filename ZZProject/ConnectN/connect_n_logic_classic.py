def create_row(size):
    """Returns a single, empty row with the given size. Each empty spot is
    represented by the string '-'.
    """
    return ['-'] * size


def create_board(rows, columns):
    """Returns a board with the given dimensions.
    """
    return [create_row(columns)] * rows


def replace_elem(lst, index, elem):
    """Create and return a new list whose elements are the same as those in
    LST except at index INDEX, which should contain element ELEM instead.
    """
    assert index >= 0 and index < len(lst), 'Index is out of bounds'
    result = lst[:]
    result[index] = elem
    return result


def get_piece(board, row, column):
    """Returns the piece at location (row, column) in the board.
    """
    return board[row][column]


def put_piece(board, column, player):
    """Puts PLAYER's piece in the bottommost empty spot in the given column of
    the board. Returns a tuple of two elements:

        1. The index of the row the piece ends up in, or -1 if the column
           is full.
        2. The new board
    """
    # get the index
    index = -1
    for i in board:
        if i[column] == '-':
            index += 1
    # get the new board
    if index != -1:
        board[index] = replace_elem(board[index], column, player)
    return (index, board)


def make_move(board, max_cols, col, player):
    """Put player's piece in column COL of the board, if it is a valid move.
    Return a tuple of two values:

        1. If the move is valid, make_move returns the index of the row the
           piece is placed in. Otherwise, it returns -1.
        2. The updated board
    """
    if 0 <= col < max_cols:
        return put_piece(board, col, player)
    else:
        return (-1, board)


def print_board(board, max_rows, max_cols):
    """Prints the board. Row 0 is at the top, and column 0 at the far left.
    """
    print('')

    for i in range(0, max_rows):
        board_view = ''
        for j in range(0, max_cols):
            board_view += get_piece(board, i, j) + ' '
        print(board_view.strip())

    print(' '.join(str(i) for i in range(max_cols)))
    print('')


def check_win_row(board, max_rows, max_cols, num_connect, player):
    """ Returns True if the given player has a horizontal win
    in the given row, and otherwise False.
    """
    for i in range(0, max_rows):
        check = ''
        for j in range(0, max_cols):
            check += get_piece(board, i, j)
        if player * num_connect in check:
            return True
    return False


def check_win_column(board, max_rows, max_cols, num_connect, player):
    """ Returns True if the given player has a vertical win in the given column,
    and otherwise False.
    """
    for i in range(0, max_cols):
        check = ''
        for j in range(0, max_rows):
            check += get_piece(board, j, i)
        if player * num_connect in check:
            return True
    return False


def check_win_diagonal(board, max_rows, max_cols, num_connect, row, col, player):
    """ Returns True if the given player has a diagonal win passing the spot
    (row, column), and False otherwise.
    """
    # Find top left of diagonal passing through the newly placed piece.
    adjacent = 0
    row_top_left, col_top_left = row, col
    while row_top_left > 0 and col_top_left > 0:
        row_top_left -= 1
        col_top_left -= 1

    # Loop through top left to bottom right diagonal and check for win.
    while row_top_left < max_rows and col_top_left < max_cols:
        piece = get_piece(board, row_top_left, col_top_left)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_left += 1
        col_top_left += 1

    # Find top right of diagonal passing through the newly placed piece.
    adjacent = 0
    row_top_right, col_top_right = row, col
    while row_top_right > 0 and col_top_right < max_cols - 1:
        row_top_right -= 1
        col_top_right += 1

    # Loop through top right to bottom left diagonal and check for win.
    while row_top_right < max_rows and col_top_right >= 0:
        piece = get_piece(board, row_top_right, col_top_right)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_right += 1
        col_top_right -= 1

    return False


def check_win(board, num_connect, row, col, player):
    """Returns True if the given player has any kind of win after placing a
    piece at (row, col), and False otherwise.
    """
    diagonal_win = check_win_diagonal(board, row, col, num_connect, row, col, player)
    horrizontal_win = check_win_row(board, row, col, num_connect, player)
    veritcal_win = check_win_column(board, row, col, num_connect, player)
    return horrizontal_win or veritcal_win or diagonal_win
