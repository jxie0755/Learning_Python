# This is to write to logic for the game flow

from connect_n_logic import *

# python3 -i connect_n_game.py

def start_game():
    # Game Header
    print('Welcome to play Connect N!!!')
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


start_game()

