# CS61A CSM 04: OOP and Orders of Growth


# Q1 (H)OOP What Would Python Display?
class Baller:
    all_players = []
    def __init__(self, name, has_ball=False):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)

    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            return False

class BallHog(Baller):
    def pass_ball(self, other_player):
        return False

if __name__ == '__main__':
    ajay = Baller('Ajay', True)
    surya = BallHog('Surya')
    print(len(Baller.all_players))   # >>> 2  # Sub-classd is also an instance of parent class.

    # print(Baller.name)  # >>> Error

    print(len(surya.all_players))  # >>> 2     # class attribute can be accessed by instance

    # print(ajay.pass_ball() Error

    print(ajay.pass_ball(surya))  # >>> True

    print(ajay.pass_ball(surya))  # >>> False

    print(BallHog.pass_ball(surya, ajay))  # >>>  False

    print(surya.pass_ball(ajay))  # >>> False

    # print(surya.pass_ball(surya, ajay)  # Error


# Q2
# Write TeamBaller, a subclass of Baller.
# An instance of TeamBaller cheers on the team every time it passes a ball

class TeamBaller(Baller):
    """
    >>> cheerballer = TeamBaller('Thomas', has_ball=True)
    >>> cheerballer.pass_ball(surya)
    Yay!
    True
    >>> cheerballer.pass_ball(surya)
    I don't have the ball
    False
    """
    # No need to rewrite the whole function.
    def pass_ball(self, other_player):
        did_pass = Baller.pass_ball(self, other_player)
        print('Yay!' if did_pass else "I don't have the ball")
        return did_pass

# Q3 Pingpong OOP
# As a reminder, the ping-pong sequence counts up starting from 1 and is always either
# counting up or counting down.
# At element k, the direction switches if k is a multiple of 7 or contains the digit 7.
# The first 30 elements of the ping-pong sequence are listed below, with direction swaps
# marked using brackets at the 7th, 14th, 17th, 21st, 27th, and 28th elements:
# 1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4
# [5] [4] 5 6
# Assume you have a function has seven(k) that returns True if k contains the digit
# 7.

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.
    """
    return '7' in str(k)

class PingPongTracker:
    def __init__(self):
        self.current = 0
        self.index = 1
        self.add = True

    def next(self):
        self.current = self.current + 1 if self.add else self.current - 1

        if has_seven(self.index) or self.index % 7 == 0:
            if self.add == True:
                self.add = False
            elif self.add == False:
                self.add = True

        self.index += 1

        return self.current
