# This is to write to logic for the game flow
# Version 2, simplify the game to fixed board 6 * 7, and to connect 4 as the classic


from connect_n_logic_classic import *
import itertools

# python3 -i connect_n_game.py

def start_game():
    # Game Header
    print('\nWelcome to play Connect N!!!\n')
    print('Player [X]\n    vs.\nPlayer [O]')

    # Create the board
    rows, cols = 6, 7
    board = create_board(rows, cols)
    num_connect = 4
    print_board(board, rows, cols)

    # Start gaming logic

    # Setup player logic
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
            try:
                move = int(input(f'Player [{player_to_move}] move, choose the column number:'))
            except:
                print('must input an integer')
                continue
            if move == 999:
                game_running = False
                print('Game quited')
                break
            elif move >= cols or move < 0:
                print('please choose the column number again')
                continue
            else:
                index, board = make_move(board, cols, move, player_to_move)
                if index == -1:
                    print('This column is full! Please re-pick!')
                    continue
                else:
                    break

        # put on the board then print
        total_moves += 1
        if move != 999:
            print_board(board, rows, cols)

        # check win
        if check_win(board, num_connect, rows, cols, player_to_move):
            print(f'Play [{player_to_move}] wins!')
            game_running = False
        elif not check_win(board, num_connect, rows, cols, player_to_move) and total_moves == rows * cols:
            print('Tie Game!')
            game_running = False
        else:
            continue

start_game()

# Starting the game by running:
# python3 -i C:/Users/jxie0/Documents/GitHub/Learning_Python/zzproject/connectn/connect_n_game_classic.py
