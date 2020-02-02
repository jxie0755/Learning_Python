shoplist = ["apple", "mango", "carrot", "banana"]

print("I have", len(shoplist), "items to purchase.")
print("These items are:", end=" ")

# for in 本来是每行罗列, 以end=" " 命令取消
for item in shoplist:
    print(item, end=" ")

print("\nI also have to buy rice.")
shoplist.append("rice")
print("My shopping list is now", shoplist)

# sort会按字幕顺序排列
print("I will sort my list now")
shoplist.sort()
print("Sorted shopping list is", shoplist)

print("The first item I will buy is", shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("I bought the", olditem)
print("My shopping list is now", shoplist)
