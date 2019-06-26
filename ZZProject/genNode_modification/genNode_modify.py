# This is a practice to revise all genNode function for Leetcode LinkedList question
# The orignal genNode function supports *nodes as a number of parameter or nodes as a List
# It is later decided that to remove *nodes option and force to use single List[int] parameter.

# Therefore there is a need to add '[' and ']' to all previous finished questions with genNode implemented with *nodes.
# This is a good chance to practice regular expression and file reading / modification.

import re
# to match find the genNode in application
to_match = r'([g][e][n][N][o][d][e][(])([[][0-9\,\s]*[]])([)])'



