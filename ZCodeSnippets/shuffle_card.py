# from https://zhuanlan.zhihu.com/p/38850888
# 一副从1到n的牌，每次从牌堆顶取一张放桌子上，再取一张放牌堆底，
# 直到手上没牌，
# 最后桌子上的牌是从1到n有序，
# 请设计程序，输入n，输出牌堆的顺序数组

def restore_card(n):
    """card sequence restore by rules

    The card sequence will do two steps:
    1. put one to the bottom
    2. put one on the desk

    keep doing untill all cards are on the desk
    on the desk it shoud look like from small to large

    n: number of cards from 1 to n
    return: a list of card as the intial sequen of numbers,
    where first element is on top last is at the bootm
    """

    initial = []
    end = list(range(1, n+1))

    while len(end) != 0:
        initial = [end.pop()] + initial
        if len(initial) > 1 and len(initial) != n:
            initial = [initial.pop()] + initial

    return initial

def move_card(seq):
    """move card as the rule in restore_card()
    seq: intial card sequence
    return: end sequence, should be a list from 1 to n
    """
    result = []
    while len(seq) != 0:
        result.append(seq.pop(0))
        if len(seq) != 0:
            seq = seq[1:] + [seq[0]]
    return result

if __name__ == "__main__":
    a = restore_card(4)
    print(move_card(a))
    # >>>
    # [1, 2, 3, 4]

    b = restore_card(13)
    print(move_card(b))
    # >>>
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
