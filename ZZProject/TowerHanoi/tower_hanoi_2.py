
def hanoi_solver(n):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.
    """

    move = 0

    def print_move(origin, destination):
        """Print instructions to move a disk."""
        print("Move the top disk from", origin, "-->", destination)

    def move_stack(n, start=1, mid=2, end=3):
        """n -- number of disks
        start = 1 #  a pole position, labelled as 1
        mid = 2 #  a temporary rod, labelled as 2
        end = 3 # a pole position, labelled as 3
        """
        nonlocal move
        if n == 1:
            print_move(start, end)   # 若只有一张,直接移动
            move += 1
        else:
            # 把一堆disk分为上下两部分,下部分bot是最下面的一个disk,其他为上部分top
            move_stack(n-1, start, end, mid)  # 把top从start移动到mid,让出bot
            move_stack(1, start, mid, end)    # 把bot从start移动到end
            move_stack(n-1, mid, start, end)  # 最后把top从mid移到end (放到bot之上)

    move_stack(n, 1, 2, 3)
    return move

if __name__ == "__main__":
    print(hanoi_solver(1))
    # >>>
    # Move the top disk from 1 --> 3
    # 1

    print(hanoi_solver(2))
    # >>>
    # Move the top disk from 1 --> 2
    # Move the top disk from 1 --> 3
    # Move the top disk from 2 --> 3
    # 3

    print("\n3 disks:")
    print(hanoi_solver(3))
    # >>>
    # Move the top disk from 1 --> 3
    # Move the top disk from 1 --> 2
    # Move the top disk from 3 --> 2
    # Move the top disk from 1 --> 3
    # Move the top disk from 2 --> 1
    # Move the top disk from 2 --> 3
    # Move the top disk from 1 --> 3
    # 7
