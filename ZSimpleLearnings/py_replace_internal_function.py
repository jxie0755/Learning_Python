"""To repalce the internal functions in python, we can create another name for the function first before create a new version"""

_list = list  # change the original list() to _list()

# define the new list funciton
def list(x):
    """return the last item of a list"""
    a = _list(x)
    # you can still use the original method, with the new name _list

    return a[-1]

print(list((1,2,3)))
# >>>
# 3
