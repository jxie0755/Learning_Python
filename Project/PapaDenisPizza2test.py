base_list = {'thin': 7.99, 'regular': 8.99, 'pan': 9.99, 'stuffed': 10.99}
cheese_list = {'light': 0.99, 'regular': 1.99, 'extra': 2.99}
vegi_list = {'green pepper': 0.49, 'onion': 0.49, 'olive': 0.49, 'tomato': 1.99, 'spinach': 0.99, 'mushroom': 0.99}
meat_list = {'beef': 2.99, 'steak': 3.99, 'chicken': 1.99, 'pepperoni': 1.99, 'sausage': 1.99}
total_list = {**base_list, **cheese_list, **vegi_list, **meat_list}

base_order = ['thin']
cheese_order = ['extra']
meat_order = ['beef', 'steak', 'chicken']
vegi_order = ['spinach', 'tomato', 'onion']
final_order = base_order + cheese_order + meat_order + vegi_order

final_price = []
for item in final_order:
    if item in total_list:
        final_price.append(total_list[item])
final_total_price = sum(final_price)
print(round(final_total_price, 2))

