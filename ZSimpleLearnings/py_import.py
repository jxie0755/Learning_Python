# Direct import a module built-in or in python
import itertools
import functools

# import a sub-directory
# directory find the subdirectory because current folder in in sys.path
from ToImport.to_be_imported import foo_to_be_imported

# import a different directory in another folder

# Wrong way
# from ZStandardLibrary.learn_time import time_spent
# >>> No module named 'ZStandardLibrary'

# Correct way
import sys
print(sys.path)

# This used absolute directory
# sys.path.insert(0, 'c:\\Users\\jxie0\\Documents\\GitHub\\Learning_Python\\ZStandardLibrary')

# This is simpler because sys.path already
sys.path.insert(0, 'ZStandardLibrary')  # include the project folder
from learn_time import time_spent

sys.path.insert(0,'ZCodeSnippets')
from fibonacci import fib_gen_r

time_spent(fib_gen_r, 35)
