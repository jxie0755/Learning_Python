# This is to write to logic for the game flow
# Version 2, simplify the game to fixed board 6 * 7, and to connect 4 as the classic


from connect_n_logic_classic_CN import *
import itertools

# python3 -i connect_n_game.py

def start_game():
    # Game Header
    print("\n欢迎来到立体4子棋!!!\n")
    print("玩家 [X]\n    vs.\n玩家 [O]\n")
    print("请双方交替下子, 实现 横/竖/斜 4子相连, 分出胜负!\n")

    # Create the board
    rows, cols = 6, 7
    board = create_board(rows, cols)
    num_connect = 4
    print_board(board, rows, cols)

    # Start gaming logic

    # Setup player logic
    players = itertools.cycle("XO")

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
                move = int(input(f"请玩家 [{player_to_move}] 下子, 输入(1-7)来选择纵列:")) - 1
            except:
                print("输入的必须是数字")
                continue
            if move == 999:
                game_running = False
                print("游戏中途退出!")
                break
            elif move >= cols or move < 0:
                print("请选择合适的范围(1-7)!")
                continue
            else:
                index, board = make_move(board, cols, move, player_to_move)
                if index == -1:
                    print("此纵列已满,不能再下子了!!")
                    continue
                else:
                    break

        # put on the board then print
        total_moves += 1
        if move != 999:
            print_board(board, rows, cols)

        # check win
        if check_win(board, num_connect, rows, cols, player_to_move):
            print(f"玩家 [{player_to_move}] 胜出!!")
            game_running = False
        elif not check_win(board, num_connect, rows, cols, player_to_move) and total_moves == rows * cols:
            print("平局!! 握手言和!!")
            game_running = False
        else:
            continue

start_game()
input("游戏结束!!")

# Starting the game by running:
# python3 -i C:/Users/jxie0/Documents/GitHub/Learning_Python/zzproject/connectn/connect_n_game_classic.py
