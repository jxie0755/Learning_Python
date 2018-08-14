# Direct import a module built-in or in python
import itertools
import functools

# import a sub-directory
from ToImport.to_be_imported import foo_to_be_imported

# import a different directory in another folder

# Wrong way
# from ZStandardLibrary.learn_time import time_spent
# >>> No module named 'ZStandardLibrary'

# Correct way
import sys

sys.path.insert(0, 'c:\\Users\\jxie0\\Documents\\GitHub\\Learning_Python\\ZStandardLibrary')

from learn_time import time_spent
