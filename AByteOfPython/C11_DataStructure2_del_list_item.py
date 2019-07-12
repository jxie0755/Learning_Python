zoo = ("python", "elephant", "penguin")
print("Number of animals in zoo is", len(zoo))

new_zoo = ("monkey", "camel", zoo)
print("Number of cages in new zoo is", len(new_zoo))  # new_zoo虽然加了zoo这个元祖，但这只是new_zoo中的一个item，所以仍然是3


print("All animals in new zoo are", new_zoo) # print会展开元组中的子元组
print("Animals brought from old zoo are", new_zoo[2])
print("Last animal brought from old zoo is", new_zoo[2][2])
print("Number of animals in the new zoo is", len(new_zoo)-1+len(new_zoo[2]))

# del zoo("elephant") 不会成功，这把zoo当成函数了
# del "elephant" 也不会成功
# 实际上，元组内的内容是不能变动的！！！！！！
print("\nNumber of animals in zoo is", len(zoo))
print("All animals in new zoo are", new_zoo)
