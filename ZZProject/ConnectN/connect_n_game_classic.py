# This is to write to logic for the game flow
# Version 2, simplify the game to fixed board 6 * 7, and to connect 4 as the classic
# Add a player name system

from connect_n_logic import *
import itertools

# python3 -i connect_n_game.py

def start_game():
    # Game Header
    print('Welcome to play Connect N!!!\n')

    # Create the board
    rows, cols = 6, 7
    board = create_board(rows, cols)
    num_connect = 4
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





start_game()

