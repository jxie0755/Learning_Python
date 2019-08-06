"""
Sequoia's notes - Function practice

Plot environmental diagram
"""

# 1. Stories
def quest(sword, robot):
    ogre = print(sword)
    sword,ogre = ogre,sword+robot
    robot /= 2
    return str(robot) > str(ogre)
robot = min(8, 8.0)   # whichever come first
sword = int("5"+str(robot))
hero = quest(robot, sword)


# 2. Painting
def paint(color):
    print(color)
    return color + str(print(color))
paint("Blue")

def print(paper):
    return max(paper * 2, "Purple")
paint("Red")

import builtins
print = builtins.print

# 3. Farm Business
tomato = "pear"
def cost(fruit):
    return int(bool(fruit))
def pair(pear, fare):
    loss = max(cost(pear), fare)
    profit = bool(pear) * float(10 * fare // loss)
    return profit - loss
pear = 100 % pair(tomato, 3)
pumpkin = pair(pear, 4)
print(pear, pumpkin)


# Write what would be displayed from running the following line of code.
print(print("61A", "is"), print(61), "A")
# >>>
# 61a is
# 61
# None, None, "A"
