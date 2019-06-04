# p657 Judge Route Circle
# Easy

# Initially, there is a Robot at position (0, 0).
# Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
# The move sequence is represented by a string. And each move is represent by a character.
# The valid robot moves are R (Right), L(Left), U (Up) and D (down).
# The output should be true or false representing whether the robot makes a circle.

# """
# :type moves: str
# :rtype: bool
# """

class Solution:
    def judgeCircle(self, moves):
        # Based on moves of coordinates
        # this method is slow, but can easily be used for telling the coordinate from any movement.
        x, y = 0, 0
        for i in moves:
            if i == 'U':
                y += 1
            elif i == 'D':
                y -= 1
            elif i == 'L':
                x -= 1
            elif i == 'R':
                x += 1
        return (x, y) == (0, 0)

    def judgeCircle(self, moves):
        # Based on count of compensating movements: 'U' and 'D', 'L' and 'R'
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

    def judgeCircle(self, moves):
        # good answer from online(use map() and a dictionary)
        return not sum(map({'U': 1, 'D': -1, 'L': 1, 'R': -1}.get, moves))


if __name__ == '__main__':
    assert Solution().judgeCircle('UDUD') == True, 'regular up and down'
    assert Solution().judgeCircle('UDU') == False, 'regular False'
    assert Solution().judgeCircle('UULDDR') == True, 'regular circcle'
    print('all passed')
