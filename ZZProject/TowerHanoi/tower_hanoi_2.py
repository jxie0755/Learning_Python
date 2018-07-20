
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
            move_stack(n-1, start, end, mid)  # 假设去掉最下面一个,剩下上面的需要从start移动到mid
            print_move(start, end)            # 然后把最下面从start移动到end
            move += 1
            move_stack(n-1, mid, start, end)  # 最后把mid的上层移动到end

    move_stack(n, 1, 3)
    return move

if __name__ == '__main__':
    print('\n1 disk:')
    print(hanoi_solver(1))
    print('\n2 disks:')
    print(hanoi_solver(2))
    print('\n3 disks:')
    print(hanoi_solver(3))
