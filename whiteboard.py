def make_review(restaurant_name, rating):
    """Return a review data abstraction."""
    return [restaurant_name, rating]

soda_reviews = [make_review('Soda', 4.5),make_review('Soda', 4)]
print(soda_reviews)