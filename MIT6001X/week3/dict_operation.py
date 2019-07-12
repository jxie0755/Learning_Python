# Introduce a number of operation to dict

grades = {"Ana": "B", "John": "A+", "Denise": "A", "Katy": "A", "Lindsay": ("a", "b", "c")}

grades["Cindy"] = "A"

del grades["John"]

print("Denise" in grades)

print(list(grades.keys()))       # only return value, don't forget to list()

print(list(grades.values()))     # only return value, don't forget to list()

# True
# dict_keys(["Ana", "Denise", "Katy", "Lindsay", "Cindy"])
# dict_values(["B", "A", "A", ("a", "b", "c"), "A"])
