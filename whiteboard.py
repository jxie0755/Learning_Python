user = ['Denis', {'A': ['A', 5], 'B': ['B', 6], 'C': ['C', 7]}]


reviews_by_user = {review[0]: review[1] for review in user[1].values()}

print(reviews_by_user)
# >>>
# {'A': 5, 'B': 6, 'C': 7}