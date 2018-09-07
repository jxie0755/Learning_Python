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

