# This is to write to logic for the game flow

from connect_n_logic import *
import itertools

# python3 -i connect_n_game.py

def start_game():
    # Game Header
    print('Welcome to play Connect N!!!\n')
    print('Please create a game board:')

    # Create the board
    def board_parameter():
        while True:
            parameter = int(input('please choose a positive integer:'))
            if parameter <= 0 or type(parameter) != int:
                print('\nyou must pick a positive integer')
                continue
            else:
                break
        return parameter

    print('How may rows?')
    rows = board_parameter()
    print('How may columns?')
    cols = board_parameter()
    board = create_board(rows, cols)

    # set the rules:
    print('\nhow many to connect? usually it is 4:')
    while True:
        num_connect = board_parameter()
        if num_connect <= rows or num_connect <= cols:
            break
        else:
            print('\nyou must pick a number smaller than rows or cols')
            continue

    print_board(board, rows, cols)

    # Start gaming logic

    # Setup player logic
    print('Player 1 is X\nPlayer 2 is O')
    players = itertools.cycle('XO')

    # Game status
    game_running = True
    total_moves = 0

    # Move Logics
    while game_running:

        # assign play to move by cycling
        player_to_move = next(players)

        # check move
        while True:
            move = int(input(f'Player {player_to_move} move, choose the column number:'))
            if move >= cols or move < 0:
                print('please choose the column number again')
                continue
            else:
                index, board = make_move(board, rows, cols, move, player_to_move)
                if index == -1:
                    print('This column is full! Please re-pick!')
                    continue
                else:
                    break

        # put on the board then print
        total_moves += 1
        print_board(board, rows, cols)

        # check win

        if check_win(board, rows, cols, num_connect, rows, cols, player_to_move):
            print(f'Play {player_to_move} wins!')
            game_running = False
        elif not check_win(board, rows, cols, num_connect, rows, cols, player_to_move) and total_moves == rows * cols:
            print('Tie Game!')
            game_running = False
        else:
            continue
