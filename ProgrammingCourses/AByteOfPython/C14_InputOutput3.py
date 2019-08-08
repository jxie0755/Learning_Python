import pickle

# The name of the file where we will store the object
shoplistfile = "D_D_shoplist.data"
# The list of things to buy
shoplist = ["apple", "mango", "carrot"]

# write to the file
f = open(shoplistfile, "wb")

# Dump the object to a file
pickle.dump(shoplist, f)

# Destroy the shoplist variables
del shoplist
# print(shoplist)   ---------原数据已不存在(NameError: name "shoplist" is not defined)

# Read back from the storage.
f = open(shoplistfile, "rb")

# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
